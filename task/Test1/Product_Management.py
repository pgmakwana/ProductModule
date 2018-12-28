import sys
#class Product Management to manage the product and store all record
class Product:
    
    #create dictionary to store the all product data    
    product_data=dict()  
    
    max_purchase_price=0
    max_sale_discount=0
    purchase_tax=0
    sale_tax=0
    minimum_stock_level=0
    
    
    def __init__(self):
        """
            func:-initialize dictionary default value for key using
            param:-
            return:-
        """

#         
#         if not self.max_purchase_price.isdigit()==True or not self.max_sale_discount.isdigit()==True or not self.purchase_tax.isdigit()==True or not self.sale_tax.isdigit()==True or not self.minimum_stock_level.isdigit()==True:
#             print("PLease Enter This all value in number format")
#             sys.exit(0)
#             
#         self.max_purchase_price=int(self.max_purchase_price)
#         self.max_sale_discount=int(self.max_sale_discount)
#         self.purchase_tax=int(self.purchase_tax)
#         self.sale_tax=int(self.sale_tax)
#         self.minimum_stock_level=int(self.minimum_stock_level)
#             
    def get_product_stock(self,product_name):
        """
            func:-Get the available stock in stock to inserted name if name is empty then give you all product stock  
            param:- product name to get the stock and it's datatype is string
            return:-  
        """
        if not product_name == '' :
            if not product_name in self.product_data.keys():
                print("This kind of product are not available in over stock...")
            else:
                print(product_name,"stock in raw material is:",self.product_data[product_name]['raw_material_quantity']," and manufactured product: ",self.product_data[product_name]['manufactured_quantity'])
        else:
            for product_name in self.product_data.keys():
                print(product_name,"stock in raw material is:",self.product_data[product_name]['raw_material_quantity']," and manufactured product: ",self.product_data[product_name]['manufactured_quantity'])
                
                
    def insert_product(self,product_name,product_quantity,total_rupies,product_type,company_name):
        """
            func:-store the data when purchase any product and re-purchase any product then update it's quantity 
            param:- product name and it's datatype is string
            param:- product quantity and it's datatype is integer 
            param:- total rupies and it's datatype is integer
            param:- product type check the product type stock or consumable and it's datatype is string 
            param:- company name are give the company name and it's datatype is string
            return:- if successfully purchased the product when return true           
        """
        #when first time product are purchased        
        if not product_name in self.product_data.keys():                        
            self.product_data.update({product_name:{}})
            self.product_data[product_name].update({'sale_price':0})
            self.product_data[product_name].update({'product_name':product_name})
            self.product_data[product_name].update({'product_type':product_type})
            self.product_data[product_name].update({'raw_material_quantity':product_quantity})
            self.product_data[product_name].update({'purchase_price':total_rupies})
            self.product_data[product_name].update({'total_sale_quantity':0})
            self.product_data[product_name].update({'company':company_name})
            self.product_data[product_name].update({'manufactured_quantity':0})
            return True
        #second time purchase the product
        else:            
            self.product_data[product_name]['raw_material_quantity'] += product_quantity 
            self.product_data[product_name]['purchase_price'] = (total_rupies+self.product_data[product_name]['purchase_price'])//2
            return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            