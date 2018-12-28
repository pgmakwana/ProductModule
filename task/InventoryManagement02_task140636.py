# Task  140636 date 04/12/2018

#this class create for product management using dictionary
class Product_managenent:
    
    #create dictionary for store the product quantity and product price
    product_dict=dict()
    
    def purchase(self,product_quantity,product_price):
        """
            func:- In this function store quantity and price in nested dictionary 
            param:- product_quantity and product_price and it's datatype is integer   
            return:- 
        """
        product_qty_length=len(self.product_dict)+1
        #count the price in per product and store it so whenever need we will get it
        product_price=round(product_price/product_quantity,2)    
        self.product_dict[product_qty_length]={'quantity':product_quantity,'price':product_price}       
        print("\nProduct Insert: {",self.product_dict[product_qty_length]['quantity']," : ",self.product_dict[product_qty_length]['price'],"}")           
    
    def sales(self,sale_quantity):
        """
            func:- sale product item from available stock in fifo(first in first out) method wise if product stock are empty then get the message
            param:- one parameter sale_quantity and it's datatype is integer
            return:- 
        """
        #store temporary product quantity for use in display message at last to product are sale or not         
        prosuct_quantity_temp=sale_quantity
        
        #this condition are checking dictionary is empty or not 
        product_qty_length=len(self.product_dict)
        if not product_qty_length > 0:
            print("\nThere is no Product are available please first add product")                                  
        else:
            #this loop iterate to the length of dictionary
            for i in range(1,product_qty_length+1):                 
                if not self.product_dict[i]['quantity']==0:
                    #this condition checking product quantity are more than availability product or not
                    if self.product_dict[i]['quantity'] >= sale_quantity:
                        #remove from the item stock to sale item quantity
                        self.product_dict[i]['quantity'] -= sale_quantity
                        print("\n",sale_quantity,"product sale successfully...")                        
                        sale_quantity=0
                        break
                    else:
                        sale_quantity -= self.product_dict[i]['quantity']
                        self.product_dict[i]['quantity'] = 0                                            
        if sale_quantity > 0:            
            print(prosuct_quantity_temp-sale_quantity,"product sale successfully but Add more ",sale_quantity," quantity to sale because prodect stock is now empty")
            product_qty=input("\nEnter Total Quantity To Purchase  : ")
            product_price=input("Enter Total Price Of Quantity     : ")
            #this condition check to product quantity and price is number format or not        
            if not product_qty.isdigit()==True or not product_price.isdigit()==True or not type(int(product_qty))==True:
                print("\nEnter Quantity and price in only Number format not any else other")                
            else:
                #call to this method to purchase and add product in over product stock
                product_manage_obg.purchase(int(product_qty),int(product_price)) 


    def valuation(self,product_valuation):
        """
            func:- get the product stock price from dictionary to inputed by user product and return one product price
            param:- product_valuation and it's datatype is integer   
            return:-  return one product price and it's datatype is integer     
        """
        product_valuation_price=self.product_dict[product_valuation]['price']
        if self.product_dict[product_valuation]['quantity'] == 0:            
            return 0
        else:
            return product_valuation_price 
     
    def get_valuation(self,product_valuation):
        """
            func:- get the product number and send it in get_valuation method for processing
            param:- product_valuation and it's datatype is integer   
            return:-  return one product price and it's datatype is integer   
        """
        #this method calling for process of calculating valuation price for per product 
        product_valuation_price=self.valuation(int(product_valuation))
        return product_valuation_price
        
    def product_stock(self):
        """
            func:- just display available all product stock and price from dictionary
            param:-    
            return:-  
        """
        for product_number in range(1,len(self.product_dict)+1):         
            if not self.product_dict[product_number]['quantity'] == 0:
                print("Product Stock",product_number,":{",self.product_dict[product_number]['quantity']," : ",self.product_dict[product_number]['price'],"}")


#create 'product_manage_obg' of Product_management class
product_manage_obg=Product_managenent()

while 1:    
    
    print("\n1]Purchase Product\n2]Sale Product\n3]Valuation\n4]Available Stock\n5]Exit")        
    option_select=input("\nSelect: ")        
    
    
    #purchase product
    if(option_select=='1'):    
        product_qty=input("\nEnter Total Quantity To Purchase  : ")
        product_price=input("Enter Total Price Of Quantity     : ")     
        #this condition check to product quantity and price is number format or not   
        if not product_qty.isdigit()==True or not product_price.isdigit()==True or not type(int(product_qty))==int:
            print("\nEnter Quantity and price in only Number format not any else other")                
        else:
            #call to this method to purchase and add product in over product stock
            product_manage_obg.purchase(int(product_qty),int(product_price)) 
           
    #sale product 
    elif(option_select=='2'):
        sale_product=input("Enter Total Quantity To Sale: ")
        if not sale_product.isdigit()==True or int(sale_product)<=0:
            print("\nEnter Quantity in only Integer format a string or enter one or more quantity")
        else:                
            #this calling to sale product from over available product stock
            product_manage_obg.sales(int(sale_product))        
     
    #get valuation of product     
    elif(option_select=='3'):
        product_valuation=input("Which product item valuation you want to get? :")
        if not product_valuation.isdigit()==True or int(product_valuation)<=0:
            print("\nEnter product number in only Integer format a string or enter one or more product")
        else:
            product_valuation=product_manage_obg.get_valuation(product_valuation)
            if not product_valuation == 0:
                print("\nThis Product Valuation is:",product_valuation)
            else:
                print("\nAll product are sale there is no product are available")
                        
    #get valuation of product     
    elif(option_select=='4'):        
        product_manage_obg.product_stock()
        
    #exit
    elif(option_select=='5'):        
        break

    else:
        print("\nSomething Is Wrong!!! Retry...")  
    
        
        
        