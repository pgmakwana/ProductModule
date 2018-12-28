
#import system package
import datetime
import pytz
#import own created class
from Product_Manufacture import Manufacture_product
from PurchaseProduct import Purchase
from Product_Management import Product
from SaleProduct import Sale

class MyCompany:
    
    #store company information Name, City, State, Country, Timezone, Total Profit, Total Investment, Total Sales
    company_information=dict()
    manage_product_obj= False
    
    def __init__(self):
        """
            func:-initialize all data of a new company and product validation like product minimum stock level 
            param:- 
            return:-
        """         
        #enter the some default value to to use in over sale/purchase order
        company_name=input('Enter Company Name: ')
        company_city=input('Enter City: ')
        company_state=input('Enter State: ')
        company_country=input('Enter Country: ')
        while 1:
            company_timezone=input('Enter Timezone: ')   
            if company_timezone in pytz.all_timezones:
                break
            else:
                print('Wrong timezone entered...') 
                
        self.company_information.update({'company_name':company_name,'company_city':company_city,'company_state':company_state,'company_country':company_country,'timezone':company_timezone,'total_profit':0,'total_investemnt':0,'total_sell':0})
        #create the object of product class are imported and assign this five value are inputed
        self.manage_product_obj=Product()        
    
    def create_manufacure_order(self):
        """
            func:-create the product from available raw material in over stock 
            param:-  
            return:-
        """
        print("-"*25+"\n")
        name_of_product=input('Enter Product Name: ')        
        manufacture_quantity=input('Enter Manufacture Quantity: ')
        if name_of_product in self.manage_product_obj.product_data.keys() and manufacture_quantity.isdigit()==True:
            if int(manufacture_quantity) <= self.manage_product_obj.product_data[name_of_product]['raw_material_quantity']:
                #call the manufacture_producrt to manufacture from the available raw material stock
                Manufacture_product.create_manufacture(Manufacture_product,name_of_product,int(manufacture_quantity),self.manage_product_obj,self.company_information['company_name'])
            else:
                print("raw material are to low please enter first more quantity")
        else:            
            print("This kind of raw material are not available in over stock...")
        
    def create_purchase_order(self):
        """
            func:-this method perform purchase the row material and manufacrute it 
            param:-  
            return:-
        """
        print("-"*25+"\n")
        name_of_product=input('Enter Product Name: ')
        product_type=input('Enter Product type[stock/consumable]: ')
        if product_type in ['stock','consumable']:
            #call the purchase product method to purchase the order
            purchase_price=Purchase.purchase_product(Purchase,name_of_product,product_type,self.company_information['company_name'],self.manage_product_obj.max_purchase_price,self.manage_product_obj.purchase_tax)
            #whenever we purchase the product then store in investment price
            self.company_information['total_investemnt'] += purchase_price
            
    def get_product_stock(self):
        """
            func:-this method get the product data from the product stock 
            param:-  
            return:-
        """
        product_name=input("Enter product name to get the product stock:") 
        self.manage_product_obj.get_product_stock(product_name)
    
    def get_most_selling_product(self):
        """
            func:- get the best selling product in list and find maximum selling product 
            param:-
            return:-
        """ 
        product_key_list=[]
        product_value_list=[]
        
        for product_key in Sale.sell_product_data.keys():
            product_key_list.append(product_key)
            product_value_list.append(Sale.sell_product_data[product_key]['sell_quantity'][0])
        
        for index_of_product in range(0,len(product_key_list)-1):
            if max(product_value_list) == product_value_list[index_of_product]:
                print(product_key[index_of_product],":",max(product_value_list)) 
    
    def suggest_purchase(self):
        """
            func:-this method give the suggestion to you have need any product are manufactured 
            param:-
            return:-
        """         
        for key in self.manage_product_obj.product_data.keys():
            #check the minimum set product value if this product are less then give you the suggestion for purchase
            if self.manage_product_obj.product_data[key]['manufactured_quantity'] < self.manage_product_obj.minimum_stock_level:   
                print(self.manage_product_obj.product_data[key]['product_name'],"product for manage stock to manufacture more:",self.manage_product_obj.minimum_stock_level-self.manage_product_obj.product_data[key]['manufactured_quantity'],"quantity")

    def update_company_timezone(self):
        """
            func:-update the timezone when we need 
            param:-
            return:-
        """
        self.company_timezone=input('Enter Timezone: ') 
        self.company_information['timezone']=self.company_timezone
        print("\nTimezone has been updated...\n")    
    
    def get_sale_orders(self):
        """
            prod:-you have get the all sale order from the sell stock as per requirement or filtering the data from starting date,to ending date,customer name,product name
            param:-
            return:-
        """
        product_name=input("Enter Product Name:")
        check_date_wise_sort=input("Get the data as date wise(yes/no):")
        customer_name=input('Enter customer Name: ')
        #whenever user not input any date then put on this condition
        if not check_date_wise_sort=='yes':
            #not input product name or customer name then give you all data
            if product_name=='' and customer_name=='':
                for product_key in Sale.sell_product_data:
                    print(product_key,":",Sale.sell_product_data[product_key]['sell_quantity'][0])
            #when product name and customer name are inputed
            elif not product_name=='' and not customer_name=='':
                if product_name in Sale.sell_product_data.keys() and customer_name in Sale.sell_product_data[product_name]['customer_name']:
                    print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][0])
                else:
                    print("This kind of product are not available in stock")
            #only input the customer name and product are empty then print this stock
            elif product_name=='' and not customer_name=='':
                for product_name in Sale.sell_product_data:
                    if customer_name in Sale.sell_product_data[product_name]['customer_name']:
                        print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][Sale.sell_product_data[product_name]['customer_name'].index(customer_name)])
                    else:
                        print("This kind of product are not available in stock")
            #if only product name are inputed then get this stock
            else:
                if product_name in Sale.sell_product_data.keys():
                    print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][0])
                else:
                    print("This kind of product are not available in stock")
        else:
            #enter date in DD/MM/YYYY format when you want to filter the data from the date 
            try:
                start_date=datetime.datetime.strptime(input("Enter Staring Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                end_date=datetime.datetime.strptime(input("Enter Ending Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                
                #not inputed product name or customer name then give you all data and filter with date
                if product_name=='' and customer_name=='':
                    for product_name in Sale.sell_product_data.keys():
                        if Sale.sell_product_data[product_name]['timezone'] >= start_date and Sale.sell_product_data[product_name]['timezone'] <= end_date:
                            print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity']) 
                #when product name and customer name are inputed with date
                elif not product_name=='' and not customer_name=='':                    
                        if product_name in Sale.sell_product_data.keys() and customer_name in Sale.sell_product_data[product_name]['customer_name']:
                            if Sale.sell_product_data[product_name]['timezone'] >= start_date and Sale.sell_product_data[product_name]['timezone'] <= end_date:
                                print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][0])
                #only input the customer name and product are empty then print this stock
                elif product_name=='' and not customer_name=='':
                    for product_name in Sale.sell_product_data:
                        if Sale.sell_product_data[product_name]['timezone'] >= start_date and Sale.sell_product_data[product_name]['timezone'] <= end_date:
                            if customer_name in Sale.sell_product_data[product_name]['customer_name']:
                                print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][Sale.sell_product_data[product_name]['customer_name'].index(customer_name)])
                #if only product name are inputed then get this stock
                else:
                    if product_name in Sale.sell_product_data.keys():
                        if Sale.sell_product_data[product_name]['timezone'] >= start_date and Sale.sell_product_data[product_name]['timezone'] <= end_date:
                            print(product_name,":",Sale.sell_product_data[product_name]['sell_quantity'][0])        
            except:
                print("Incorrect date format, should be DD-MM-YYYY")
                return 0 
    def get_manufacturing_orders(self):
        """
            prod:-you have get the all manufactured order from the manufactured stock as per requirement or filtering the data
            param:-
            return:-
        """
        product_name=input("Enter Product Name:")
        check_date_wise_sort=input("Get the data as date wise(yes/no):")       
        if not check_date_wise_sort=='yes':
            if product_name=='':
                for product_key in self.manage_product_obj.product_data:
                    print(product_key,":",self.manage_product_obj.product_data[product_key]['manufactured_quantity'])
            else:
                if product_name in Sale.sell_product_data.keys():
                    print(product_name,":",self.manage_product_obj.product_data[product_key]['manufactured_quantity'])
                else:
                    print("This kind of product are not available in stock")  
        else:
            #enter date in DD/MM/YYYY format when you want to filter the data from the date 
            try:
                start_date=datetime.datetime.strptime(input("Enter Staring Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                end_date=datetime.datetime.strptime(input("Enter Ending Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                
                #not inputed product name or customer name then give you all data and filter with date
                if product_name=='':
                    for product_key in self.manage_product_obj.product_data.keys():
                        if end_date >= self.manage_product_obj.product_data[product_key]['timezone'] >=start_date:  
                            print(product_key,":",self.manage_product_obj.product_data[product_key]['manufactured_quantity'])
                        
                else:
                    #if only product name are inputed then get this stock
                    if product_name in Sale.sell_product_data.keys():
                        if end_date >= self.manage_product_obj.product_data[product_key]['timezone'] >=start_date:
                            print(product_name,":",self.manage_product_obj.product_data[product_key]['manufactured_quantity'])
                    else:
                        print("This kind of product are not available in stock")        
            except:
                print("Incorrect date format, should be DD-MM-YYYY")
                return 0 
    def get_purchase_orders(self):
        """
            prod:-you have get the all purchased raw material order from the raw material  stock as per requirement or filtering the data
            param:-
            return:-
        """
        product_name=input("Enter Product Name:")
        check_date_wise_sort=input("Get the data as date wise(yes/no):")
        supplier_name=input("Enter Supplier Name:")
        #whenever not inputed any date then put on this condition
        if not check_date_wise_sort=='yes':
            #not input product name or supplier name then give you all data
            if product_name=='' and supplier_name=='':
                for product_index in range(0,len(Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'])):
                    print(Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'][product_index],":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][product_index])
            #when product name or user name and customer name are inputed
            elif not product_name=='' and not supplier_name=='':                
                if product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'] and supplier_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name']:
                    print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)])
                else:
                    print("This kind of product are not available in stock")
            #only input the customer name and product are empty then print this stock
            elif product_name=='' and not supplier_name=='':
                for product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items']:
                    if supplier_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name']:
                        print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)])
                    else:
                        print("This kind of product are not available in stock")
            #if only product name are inputed then get this stock
            else:
                if product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items']:                    
                    print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'].index(product_name)])
                else:
                    print("This kind of product are not available in stock")  
        else:
            #enter date in DD/MM/YYYY format when you want to filter the data from the date 
            try:
                start_date=datetime.datetime.strptime(input("Enter Staring Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                end_date=datetime.datetime.strptime(input("Enter Ending Date(DD/MM/YYYY):"),'%d/%m/%Y').date()
                
                #not input product name or supplier name then give you all data
                if product_name=='' and supplier_name=='':
                    for product_index in range(0,len(Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'])):
                        if end_date >= Purchase.purchase_product_data[company_obj.company_information['company_name']]['timezone'][product_index] >=start_date: 
                            print(Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'][product_index],":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][product_index])
                #when product name and supplier are inputed
                elif not product_name=='' and not supplier_name=='':                
                    if product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'] and supplier_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name']:
                        if end_date >= Purchase.purchase_product_data[company_obj.company_information['company_name']]['timezone'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)] >=start_date:
                            print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)])
                    else:
                        print("This kind of product are not available in stock")
                #only input the supplier name and product are empty then print this stock
                elif product_name=='' and not supplier_name=='':
                    for product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items']:
                        if supplier_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name']:
                            if end_date >= Purchase.purchase_product_data[company_obj.company_information['company_name']]['timezone'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)] >=start_date:
                                print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['supplier_name'].index(supplier_name)])
                        else:
                            print("This kind of product are not available in stock")
                #if only product name are inputed then get this stock
                else:
                    if product_name in Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items']:                    
                        if end_date >= Purchase.purchase_product_data[company_obj.company_information['company_name']]['timezone'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'].index(product_name)] >=start_date:
                            print(product_name,":",Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_quantity'][Purchase.purchase_product_data[company_obj.company_information['company_name']]['purchase_items'].index(product_name)])
                    else:
                        print("This kind of product are not available in stock")
                           
            except:
                print("Incorrect date format, should be DD-MM-YYYY")
                return 0 
    def sale_purchase_account_data(self):
        """
            func:-get the sale or purchase account data or profit of over product from selling or purchasing the product 
            param:-
            return:-
        """
        print("Total Investment: ",self.company_information['total_investemnt'])
        print("Total Selling: ",self.company_information['total_sell'])
        #check for we are in profited or loss
        if not self.company_information['total_profit'] < 0:
            print("Total Profit: ",self.company_information['total_profit'])
        else:
            print("We are loss: ",self.company_information['total_profit']," RS.")
            
    def create_sale_order(self):
        """
            func:-this method sell the product are available ib product stock 
            param:-  
            return:-
        """
        print("-"*25+"\n")
        name_of_product=input('Enter Product Name: ')
        #check the product name are available or not in over stock        
        if not name_of_product in self.manage_product_obj.product_data.keys():
            print("This kind of raw material are not available in over stock...")            
        else:            
            print('\navailable quantity: ',self.manage_product_obj.product_data[name_of_product]['manufactured_quantity'],"\n")
            #enter the quantity for sell from over stock and it's enter in only number format
            sell_quantity=input('Enter Sell Quantity: ')
            if sell_quantity.isdigit()==False:
                print("Enter Only numeric value...")                    
            else:
                sell_quantity=int(sell_quantity)
                if int(sell_quantity) > self.manage_product_obj.product_data[name_of_product]['manufactured_quantity'] :
                    print(name_of_product,"Product stock are to low please manufactured",sell_quantity,"quantity to sell the product")                
                else:
                    if self.manage_product_obj.product_data[name_of_product]['product_type']=='stock' and Product.product_data[name_of_product]['manufactured_quantity']-int(sell_quantity) <= self.manage_product_obj.minimum_stock_level:
                        print("Selling not stop but you have need more quantity are manufacturing...\n")
                        
                    #call the sale product method to sell the product from available stock and get the sell price to sell the product 
                    sale_price=Sale.sale_prodcut(Sale,name_of_product,int(sell_quantity),self.manage_product_obj,self.company_information['company_name'],self.manage_product_obj.max_sale_discount)
                    
                    #add sale amount in sale price to get any time total sell amount when we need this
                    self.company_information['total_sell'] += sale_price
                    if sale_price > self.manage_product_obj.product_data[name_of_product]['purchase_price']*sell_quantity:                        
                        self.company_information['total_profit'] += sale_price - (self.manage_product_obj.product_data[name_of_product]['purchase_price']*sell_quantity)                   
                    elif sale_price < self.manage_product_obj.product_data[name_of_product]['purchase_price']*sell_quantity:
                        self.company_information['total_profit'] -= (self.manage_product_obj.product_data[name_of_product]['purchase_price']*sell_quantity) - sale_price         
        
#create company_obj of mtcompany class to access it all data             
company_obj=MyCompany()    
    
#this loop create for menu
while 1:
    
    print("*"+"-"*35+"*"+"\n1]Purchase \n2]Sale \n3]Manufacture Product \n4]Get Sale Purchase Account Data \n5]Get Most Selling Product \n6]Product Stock \n7]Get Purchase Order \n8]Get Sale Order \n9]Get Manufacturing Order \n10]Purchase Suggestion \n11]Update Company Date \n12]Exit\n"+"*"+"-"*35+"*")
    option_select=input("Select: ")
     
    if(option_select=='1'): company_obj.create_purchase_order()
    elif(option_select=='2'):company_obj.create_sale_order()
    elif(option_select=='3'):company_obj.create_manufacure_order()
    elif(option_select=='4'):company_obj.sale_purchase_account_data()
    elif(option_select=='5'):company_obj.get_most_selling_product()
    elif(option_select=='6'):company_obj.get_product_stock()
    elif(option_select=='7'):company_obj.get_purchase_orders()
    elif(option_select=='8'):company_obj.get_sale_orders()    
    elif(option_select=='9'):company_obj.get_manufacturing_orders()
    elif(option_select=='10'):company_obj.suggest_purchase()
    elif(option_select=='11'):company_obj.update_company_timezone()        
    elif(option_select=='12'):   break
    else:
        print("Wrong Selection...") 
        
        
        
