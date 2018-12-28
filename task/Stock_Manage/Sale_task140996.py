# Task  140996 date 11/12/2018
import re
import datetime
#import TaxCalculation for tax calculating
from TaxCalculation_task140996 import TaxCalculation

class Sale(TaxCalculation):
    
    sale_product_data={}
    
        
    def sale(self,product_name,sub_product,product_quantity,product_type):
        """
            func:- sell the product from available stock in product class and store sell date,number,quantity price,tax,total price    
            param:- product_name to store all detail's in this product detail key
            param:-  sub produdct to store sub product detail's of main product
            param:-   product_qty to sell product and it's datatype is integer. 
            return:-    per product sell price and it's datatype is integer.
            return:-      sell order number and it's datatype is string  
        """
        print("*--------------------Enter Selling Detail's--------------------*")
        
        
        customer_name=input("Customer Name       :")
        product_price=input("Price(Without Tax)  :")

        #find the today date in dd/mm/yyyy format    
        now = datetime.datetime.today().strftime('%d/%m/%Y')

        if product_price.isdigit()==True:            
            one_product_price=round(int(product_price)/int(product_quantity),2)
            
            #any product sell first time or check this product sell first time or not
            if not product_name in self.sale_product_data.keys():
                #store all product data in stock using product name keyword
                self.sale_product_data.update({product_name:{}})
                self.sale_product_data[product_name][sub_product]={}
                self.sale_product_data[product_name][sub_product].update({'product_purchasing_date':now})
                self.sale_product_data[product_name][sub_product].update({'quantity':int(product_quantity)})
                self.sale_product_data[product_name][sub_product].update({'sub_product':sub_product})
                self.sale_product_data[product_name][sub_product].update({'customer_name':customer_name})
                self.sale_product_data[product_name][sub_product].update({'basic_price':one_product_price})
                self.sale_product_data[product_name][sub_product].update({'total_price':TaxCalculation.get_tax(self,one_product_price,'SELL',product_type.upper())+one_product_price})
                self.sale_product_data[product_name][sub_product].update({'sell_order_number':[]})
                #update the product purchase number whenever we repeated purchase product
                self.sale_product_data[product_name][sub_product]['sell_order_number'].append(["SO/"+str(int(re.findall('\d+',"0")[0])+1).zfill(5)])
                
            
            #any product sell first time or check this product sell first time or not but it's for sub product
            elif not sub_product in self.sale_product_data[product_name].keys():  
                self.sale_product_data[product_name][sub_product]={}
                self.sale_product_data[product_name][sub_product].update({'product_purchasing_date':now})
                self.sale_product_data[product_name][sub_product].update({'quantity':int(product_quantity)})
                self.sale_product_data[product_name][sub_product].update({'sub_product':sub_product})
                self.sale_product_data[product_name][sub_product].update({'customer_name':customer_name})
                self.sale_product_data[product_name][sub_product].update({'basic_price':one_product_price})
                self.sale_product_data[product_name][sub_product].update({'total_price':TaxCalculation.get_tax(self,one_product_price,'SELL',product_type.upper())+one_product_price})
                self.sale_product_data[product_name][sub_product].update({'sell_order_number'.append([str(int(re.findall('\d+',"0")[0])+1).zfill(5)])})
                return self.sale_product_data[product_name][sub_product]['total_price'],self.sale_product_data[product_name][sub_product]['sell_order_number'][0]
            #re-sell any sub product then use it
            else:
                self.sale_product_data[product_name][sub_product].update({'quantity':int(product_quantity)+self.sale_product_data[product_name][sub_product]['quantity']})
                self.sale_product_data[product_name][sub_product].update({'basic_price':(one_product_price+self.sale_product_data[product_name][sub_product]['basic_price'])/2})
                self.sale_product_data[product_name][sub_product].update({'customer_name':customer_name})
                self.sale_product_data[product_name][sub_product].update({'total_price':(self.sale_product_data[product_name][sub_product]['total_price']+TaxCalculation.get_tax(self,one_product_price,'SELL',product_type.upper())+one_product_price)/2})
            
            
            self.sale_product_data[product_name][sub_product]['sell_order_number'].append(["SO/"+str(int(re.findall('\d+',str(self.sale_product_data[product_name][sub_product]['sell_order_number'][len(self.sale_product_data[product_name][sub_product]['sell_order_number'])-1]))[0])+1).zfill(5)])
            return self.sale_product_data[product_name][sub_product]['total_price'],self.sale_product_data[product_name][sub_product]['sell_order_number'][len(self.sale_product_data[product_name][sub_product]['sell_order_number'])-1]
                
        else:
            print("product price is must be in number format not any other")
        
        
        