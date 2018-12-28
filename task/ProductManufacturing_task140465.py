# Task 140465  date 01/12/2018

from reportlab.lib.validators import isNumber

class Manufacturing:  
    
     
    def __init__(self,name="material_1",quantity=0):
        """
            func:- This function use for initialization of raw material quantity ,raw material name
            param:- manufacturing raw material name and it's datatype shoud be string
            param :- manufacturing raw material quantity and it's datatype shoud be integer
            return:- 
        """         
        self.raw_material_name=name
        self.raw_material_quantity=quantity
    
    
    def get_stock(self):
        """ 
            func:- This function is used for get the total stock of raw material
            param:- 
            return:- return available stock of raw material quantity and it's datatype should be integer
        """
        return self.raw_material_quantity
    
    
    def qty_purchase(self,item_name,qty):
        """
            func:- Purchase raw material item from other customer for manufacturing 
            param:- Purchase raw material name and it's datatype should be string
            param:-  Purchase raw material quantity and it's datatype should be integer
            return:- 
        """
        self.raw_material_quantity += qty
    
    def produce_item(self,item_name,qty):
        """
            func : -Produce item or manufacture from the available raw material 
            param :-  name of produce item and it's datatype should be string 
            param:-       produce item quantity and it's datatype should be integer
            retrun:-     
        """         
        if(self.raw_material_quantity < qty ):
            print ("\nYou have not enough raw material for manufacturing add more",qty-self.raw_material_quantity,"raw material.")
        else:
            self.raw_material_quantity -= qty    


      
#Get the raw material name  
raw_material_name=input("Product name: ")

#get the raw material quantity to use in produce the product
raw_material_quantity=input("Total available raw material quantity: ")

#if raw material quantity are empty then set the by default '0' quantity
if(raw_material_quantity==""):
    raw_material_quantity=0
    
#check the quantity are enter in numeric or not    
if(isNumber(raw_material_quantity)):
    
    #check raw material quantity entered is positive or negative
    if(int(raw_material_quantity) >= 0):
                    
        #create "product_manufactuing" object of a Manufacturing class
        product_manufactuing=Manufacturing(raw_material_name,int(raw_material_quantity))
        
        #this loop use for menu
        while 1:    
            
            try:        
                print("\nCheck Item Stock Enter 1]\nPurchase Raw Material 2]\nProduce Item 3]\nExit 4]")
                    
                option_select=int(input("Select: "))        
                
                if(option_select==1):
                    item_stock=product_manufactuing.get_stock()
                    print("\nRaw Material Stock Is ",item_stock)
                    
                elif(option_select==2):
                    purchase_raw_quantity=int(input("\nInput Quantity For Purchase Raw Material: "))
                    product_manufactuing.qty_purchase(raw_material_name,purchase_raw_quantity)
                        
                elif(option_select==3):
                    produce_quantity=int(input("\nInput Quantity For Produce Item: "))
                    product_manufactuing.produce_item(raw_material_name,produce_quantity)
                    
                elif(option_select==4):
                    break
            
                else:
                    print("\nSomething Is Wrong!!! Retry...")
                    
            except:
                    print("\nSomething Is Wrong!!! Retry...")
    else:
        print("\nNegative quantity are not acceptable.")
else:    
    print("Quantity are enter in only numeric values")
    
print("\nThank You...")
