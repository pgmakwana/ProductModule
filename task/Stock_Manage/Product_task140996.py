# Task  140996 date 11/12/2018

import csv
import xlrd
import xlwt
#import two classes for product sale purchase
from Sale_task140996 import Sale
from Purchase_task140996 import Purchase
from xlwt.Workbook import Workbook

#create Product class and inherit given two class
class Product(Sale,Purchase):
    
    #In this dictionary store the product detail.
    product_detail=dict() 

    def check_profit_loss(self,product,sub_product,product_quantity,sell_price,max_purchase_price):
        """
            func:- find the profit and loss from the purchase price and sell price different and store in dictionary    
            param:- product is main product of stock and it's datatype is string.
            param:-  sub product is sub product of main product and it's datatype is string. 
            param:-    product quantity to find the purchase price to multiply with an quantity and it's datatype is integer.
            param:-     sell price are price of all quantity to sell and it's datatype is integer 
            return:-    return success message to sale successfully in string type.
            
        """
        #count purchase price to number of sell product quantity * per product purchase price  
        purchase_price=product_obj.product_detail[product][sub_product]['product_price']*product_quantity
        print(purchase_price)
        print(sell_price)
        if purchase_price < sell_price:
            product_obj.product_detail[product][sub_product]['profit'] += sell_price-(purchase_price+product_obj.product_detail[product][sub_product]['loss'])
        elif purchase_price == sell_price:
            return "product sell successfully"
        else:
            product_obj.product_detail[product][sub_product]['loss'] = purchase_price-(sell_price+product_obj.product_detail[product][sub_product]['profit'])
            
        return "product sell successfully"        
    
    def saveProduct(self):
        """
            func:- this function save the purchase or sell data in csv file whenever user are sell or purchase data    
            param:- 
            return:-    
            
        """
        workbook=Workbook()
        worksheet=workbook.add_sheet("Product_detail")
        
        '''
       csv_file = open('csv_file/product_detail.csv','w')        
        writer = csv.writer(csv_file)
        row=1
        col=1
        for key, value in self.product_detail.items():
            col=1            
            worksheet.write(row,col,key)
            col=2
            row+=1
            worksheet.write(row,col,str(self.product_detail[key]))
            row+=1            
        workbook.save('csv_file/product_detail.csv')'''
###############################################################################################################

#create 'product_obj' of Product class 
product_obj=Product()
while 1:    
    
    print("\n*"+"~"*20+"*")
    print("1]Purchase Product \n2]Sale Product \n3]Available Stock\n4]Save Data\n5]Exit")
    print("*"+"~"*20+"*")
    
    option_select=input("\nSelect Option : ")
    
    #1]1]Purchase Product
    if(option_select=='1'):
        
        product=input("\nEnter Product Name                          :")
        product_type=str(input("Product Type STOCK Or SERVICE Or CONSUMABLE :"))
        if product_type not in ("stock","service","consumable"):
            print("\nWarning: Enter type only from three listed product type...") 
            continue        
        #call the Purchase class method to purchase the product
        product_quantity,one_product_price,product_name,purchase_number=product_obj.purchase(product,product_type)
        
        #main product purchase first time
        if not product in product_obj.product_detail.keys():
            product_obj.product_detail.update({product:{}})
            product_obj.product_detail[product].update({product_name:{}})
            product_obj.product_detail[product][product_name].update({'product_name':product_name})
            product_obj.product_detail[product][product_name].update({'product_quantity':product_quantity})
            product_obj.product_detail[product][product_name].update({'product_type':product_type})
            product_obj.product_detail[product][product_name].update({'product_price':one_product_price})
            product_obj.product_detail[product][product_name].update({'profit':0})
            product_obj.product_detail[product][product_name].update({'loss':0})
            product_obj.product_detail[product][product_name].update({'purchase_order_number':[]})
                
        #main product purchased but sub product purchase first time
        elif not product_name in product_obj.product_detail[product].keys():
            product_obj.product_detail[product].update({product_name:{}})
            product_obj.product_detail[product][product_name].update({'product_name':product_name})
            product_obj.product_detail[product][product_name].update({'product_quantity':product_quantity})
            product_obj.product_detail[product][product_name].update({'product_type':product_type})
            product_obj.product_detail[product][product_name].update({'product_price':one_product_price})
            product_obj.product_detail[product][product_name].update({'profit':0})
            product_obj.product_detail[product][product_name].update({'loss':0})
            product_obj.product_detail[product][product_name].update({'purchase_order_number':[]})
            
        #Re-purchase any product 
        else:
            product_obj.product_detail[product][product_name].update({'product_quantity':product_quantity+product_obj.product_detail[product][product_name]['product_quantity']})
            product_obj.product_detail[product][product_name].update({'product_price':one_product_price})
            
        product_obj.product_detail[product][product_name]['purchase_order_number'].append(purchase_number)
                
        print("\nProduct Purchasing Successfully...")
        
        
    #2]Sale Product                     
    elif(option_select=='2'):
        
        #check product available in stock or not
        if len(product_obj.product_detail) == 0:
            print("\nWarning: Product is not available in stock please check it...")
            continue
        
        #get the available product in stock from dictionary
        print("\n---Main Product List---")        
        for product_list in sorted(product_obj.product_detail.keys()):     
            print(product_list)
        
        product=input("\nWhich product purchased:")
        
        if not product in sorted(product_obj.product_detail.keys()):
            print("\nWarning: That's wrong selection")
            continue
        
        print("\n---In",product,"this product are available---")
        for sub_product in product_obj.product_detail[product].keys():
            print(sub_product)
        
        sub_product=input("\nEnter Product Name:")
        
        if not sub_product in sorted(product_obj.product_detail[product].keys()):
            print("\nWarning: That's wrong selection")
            continue
        
        product_quantity=input("\nEnter Product Quantity:")
        
        if not product_quantity.isdigit() == True :
            print("\nWarning: Enter quantity in only number format not any other")
            continue
        if not int(product_quantity) < product_obj.product_detail[product][sub_product]['product_quantity']:
            print("\nWarning: There is only",product_obj.product_detail[product][sub_product]['product_quantity'],"product please add more product to sell")
            continue
        
        product_type=product_obj.product_detail[product][sub_product]['product_type']
        
        #call the sale method to sell product and get sell price or sell product number
        sell_price,sell_product_number=product_obj.sale(product,sub_product,int(product_quantity),product_type)
        product_obj.product_detail[product][sub_product]['product_quantity'] -= int(product_quantity)
        
        #create sell order number in dictionary when we sell first time
        if 'sell_product_number' not in product_obj.product_detail[product][sub_product].keys():
            product_obj.product_detail[product][sub_product].update({'sell_order_number':[]})
            
        product_obj.product_detail[product][sub_product]['sell_order_number'].append(sell_product_number) 
        
        #call to count profit loss and get the status of counting success or not
        sell_status=product_obj.check_profit_loss(product,sub_product,int(product_quantity),sell_price*int(product_quantity))
                
        print(sell_status)
    #3]Available Stock 
    elif(option_select=='3'):
        
        #check product available in stock or not
        if len(product_obj.product_detail) == 0:
            print("\nWarning: Product is not available in stock please check it...")
            continue
        
        #get the available product in stock from dictionary
        print("\n---Main Product List---")        
        for product_list in sorted(product_obj.product_detail.keys()):     
            print(product_list)
        
        product=input("\nEnter Product Name:")
        
        #check product available in stock or not
        if not product in sorted(product_obj.product_detail.keys()):
            print("\nWarning: Product is not available in stock please check it...")
            continue
        
        #get the available product in stock from dictionary        
        for product_list in sorted(product_obj.product_detail[product]):     
            print(product_obj.product_detail[product][product_list])
            
    #save data in csv file
    elif(option_select=='4'):
        product_obj.saveProduct()
        print("\ndata saved successfully...\n")
    
    #exit
    elif(option_select=='4'):
        break

    else:
        #When user input wrong option.
        print("\nWarning: Something Is Wrong!!! Retry...")
        
        
    
    
    