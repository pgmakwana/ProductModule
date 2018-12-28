# Task  140592 date 04/12/2018

#This class create for inventory management to purchase,sale and get total available stock 
class Product:
    
    def __init__(self,defult_product_quantity):
        """
            func:- use for only assign product stock as user inputed first time 
            param:- defult_product_quantity and it's datatype is integer 
            return:-
        """
        self.product_1=defult_product_quantity
        
    def purchase(self,purchase_product_quantity):
        """
            func:- whenever we purchase product quantity to add in product stock
            param:- purchase_product_quantity and it's datatype is integer
            return:- 
        """       
        self.product_1 += purchase_product_quantity
        
    def sales(self,sale_product_quantity):
        """
            func:- whenever we sale a product then remove the product quantity from the product stock
            param:- sale_product_quantity and it's datatype is integer
            return:- 
        """
        if sale_product_quantity > self.product_1:
            print("\n\nPlease add more product quantity for sale because product stock are to less...")
        else:
            self.product_1 -= sale_product_quantity
        
    def total_stock(self):
        """
            func:- this function use for only return the available product stock
            param:- 
            return:- return the available product stock and it's datatype is integer 
        """
        return self.product_1
    
   
#First time product stock initialization
initilize_product=input("Enter Available Stock Quantity : ")
if not initilize_product.isdigit()==True:
    print("\nEnter Quantity in only Integer format not any else other")
else:
    #create 'product_obj' object of the Product class      
    product_obj=Product(int(initilize_product))

#This loop use for menu
while 1:    
              
    print("\nPurchase Product 1]\nSale Product 2]\nProduct Stock3]\nExit 4]")        
    option_select=input("Select: ")        
    
    #purchase product
    if(option_select=='1'):     
        purchase_product=input("Enter Total Quantity To Purchase: ")
        if not purchase_product.isdigit()==True:
            print("\nnEnter Quantity in only Integer format not any else other")
            break
        
        #call the purchase method to purchase stock and add in main product stock
        product_obj.purchase(int(purchase_product))
       
    #sale product 
    elif(option_select=='2'):
        sale_product=input("Enter Total Quantity To Sale: ")
        if not sale_product.isdigit()==True:
            print("\nnEnter Quantity in only Integer format not any else other")
            break
        
        #call the sales method to sale product from the available product stock
        product_obj.sales(int(sale_product))
     
    #get product stock       
    elif(option_select=='3'):
        
        #call total_stock method to get available product stock
        available_product=product_obj.total_stock()
        print("\n\nAvailable Product Stock Is:",available_product)
        
    #exit
    elif(option_select=='4'):        
        break

    else:
        print("\nSomething Is Wrong!!! Retry...")
       
                