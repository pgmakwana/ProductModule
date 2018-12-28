# Task  140996 date 11/12/2018
import re
import datetime
#import TaxCalculation for tax calculating
from TaxCalculation_task140996 import TaxCalculation

class Purchase(TaxCalculation):
    
    purchase_product_data=dict()
       
    def purchase(self,product_name,product_type):
        """
            func:- Insert the product detail like product name,price,vendor name,purchase date,tax,total price,purchase order number    
            param:- product_name to store all detail's in this product detail key
            param:-  product_obj are fate from Product class and it's datatype is object 
            param:-    product type is stock or service to count the tax and it's datatype is string
            return:-   product_quantity and it's datatype is integer.
            return:-    per product price and it's datatype is integer
            return:-     vendor name and it's datatype is string
            return:-       purchase order number and it's datatype is string
        """
        print("\n*-----------------Enter Purchase Detail-----------------*")
        
        vendor_name=input("\nVendor Name         :")
        product_quantity=input("Quantity            :")
        product_price=input("Price(Without Tax)  :")        

        #find the today date in dd/mm/yyyy format    
        now = datetime.datetime.today().strftime('%d/%m/%Y')

        if product_quantity.isdigit()==True and product_price.isdigit()==True:
            one_product_price=round(int(product_price)/int(product_quantity),2)
            if not product_name in self.purchase_product_data.keys():
                #store all product data in stock using product name keyword            
                self.purchase_product_data.update({product_name:{}})
                self.purchase_product_data[product_name][vendor_name]={}
                self.purchase_product_data[product_name][vendor_name].update({'product_purchasing_date':now})
                self.purchase_product_data[product_name][vendor_name].update({'quantity':int(product_quantity)})
                self.purchase_product_data[product_name][vendor_name].update({'vendor_name':vendor_name})
                self.purchase_product_data[product_name][vendor_name].update({'basic_price':one_product_price})
                self.purchase_product_data[product_name][vendor_name].update({'total_price':TaxCalculation.get_tax(self,one_product_price,'PURCHASE',product_type.upper())+one_product_price})
                self.purchase_product_data[product_name][vendor_name].update({'purchase_order_number':[]})
                #update the product purchase number whenever we repeated purchase product
                self.purchase_product_data[product_name][vendor_name]['purchase_order_number'].append(["PO/"+str(int(re.findall('\d+',"0")[0])+1).zfill(5)])
                                
                return int(product_quantity),self.purchase_product_data[product_name][vendor_name]['total_price'],vendor_name,self.purchase_product_data[product_name][vendor_name]['purchase_order_number'][0][0]
                
            elif not vendor_name in self.purchase_product_data[product_name].keys():  
                self.purchase_product_data[product_name][vendor_name]={}
                self.purchase_product_data[product_name][vendor_name].update({'product_purchasing_date':now})
                self.purchase_product_data[product_name][vendor_name].update({'quantity':int(product_quantity)})
                self.purchase_product_data[product_name][vendor_name].update({'vendor_name':vendor_name})
                self.purchase_product_data[product_name][vendor_name].update({'basic_price':one_product_price})
                self.purchase_product_data[product_name][vendor_name].update({'total_price':TaxCalculation.get_tax(self,one_product_price,'PURCHASE',product_type.upper())+one_product_price})
                self.purchase_product_data[product_name][vendor_name].update({'purchase_order_number':[]})
                #update the product purchase number whenever we repeated purchase product
                self.purchase_product_data[product_name][vendor_name]['purchase_order_number'].append(["PO/"+str(int(re.findall('\d+',"0")[0])+1).zfill(5)])
                return int(product_quantity),self.purchase_product_data[product_name][vendor_name]['total_price'],vendor_name,self.purchase_product_data[product_name][vendor_name]['purchase_order_number'][0][0]
                
            else:
                self.purchase_product_data[product_name][vendor_name].update({'quantity':int(product_quantity)+self.purchase_product_data[product_name][vendor_name]['quantity']})
                self.purchase_product_data[product_name][vendor_name].update({'basic_price':(one_product_price+self.purchase_product_data[product_name][vendor_name]['basic_price'])/2})
                self.purchase_product_data[product_name][vendor_name].update({'total_price':(self.purchase_product_data[product_name][vendor_name]['total_price']+TaxCalculation.get_tax(self,one_product_price,'PURCHASE',product_type.upper())+one_product_price)/2})
             
            #update the product purchase number whenever we repeated purchase product
               
            self.purchase_product_data[product_name][vendor_name]['purchase_order_number'].append(["PO/"+str(int(re.findall('\d+',str(self.purchase_product_data[product_name][vendor_name]['purchase_order_number'][len(self.purchase_product_data[product_name][vendor_name]['purchase_order_number'])-1]))[0])+1).zfill(5)])
            return int(product_quantity),self.purchase_product_data[product_name][vendor_name]['total_price'],vendor_name,self.purchase_product_data[product_name][vendor_name]['purchase_order_number'][len(self.purchase_product_data[product_name][vendor_name]['purchase_order_number'])-1]
            
            
        else:
            print("Product quantity and product price is must be in number format not any other")
        
        