

import datetime
import re

class Sale:
    
    sell_product_data=dict()
    sell_status=''
    
    def sale_prodcut(self,product_name,sell_quantity,manage_product_obj,company_name,max_discount):
        """
            func:-this method sell the product are available in stock and give the discount when sell the product
            param:-product name and it's datatype is string
            param:-sell quantity and it's datatype is integer
            param:-product object this object access the product class data and it's datatype is object.
            param:-company name and it's datatype is string.
            param:-sell_tax use for tax counting when sell the product and it's datatype is integer
            return:-sell price and it's datatype is integer or warning message if occur any error.
        """
        
        print("\nIn process")
        
        customer_name=input('Enter customer name: ') 
        selling_price=input('Enter Sell Price(per quantity): ') 
        sell_discount=input('Enter Sell Discount(in percentage): ')
        if selling_price.isdigit()==False or sell_discount.isdigit()==False:
            print("enter only numeric value in price...")
            return 0
        selling_price=int(selling_price)
        sell_discount=int(sell_discount)
        
        #add the discount on price from set'ed discount
        if not sell_discount > max_discount:
            selling_price=selling_price-int((selling_price*(sell_discount/100)))
        else:
            print("Discount Is very high please enter between only 1-",max_discount)
            return 0
            
            
        #first time company sell the product
        if not product_name in self.sell_product_data.keys():            
            self.sell_product_data.update({product_name:{}})
            self.sell_product_data[product_name].update({'product_items':[]})
            self.sell_product_data[product_name].update({'sell_quantity':[]})
            self.sell_product_data[product_name].update({'selling_price':[]})
            self.sell_product_data[product_name].update({'sell_order_number':[]})
            self.sell_product_data[product_name].update({'timezone':datetime.datetime.utcnow().date()})            
            self.sell_product_data[product_name].update({'company_name':company_name})            
            self.sell_product_data[product_name].update({'customer_name':[]})
            self.sell_product_data[product_name]['customer_name'].append(customer_name)
            self.sell_product_data[product_name]['selling_price'].append(selling_price)
            self.sell_product_data[product_name]['product_items'].append(product_name)
            self.sell_product_data[product_name]['sell_quantity'].append(int(sell_quantity))         
            self.sell_product_data[product_name]['sell_order_number'].append(["SO/"+str(int(re.findall('\d+',"1")[0])).zfill(5)])
            
        else:            
            self.sell_product_data[product_name]['selling_price'][0] += selling_price
            self.sell_product_data[product_name]['sell_quantity'][0] += sell_quantity
            self.sell_product_data[product_name]['timezone']=datetime.datetime.utcnow().date()
            self.sell_product_data[product_name]['customer_name'].append(customer_name)
            self.sell_product_data[product_name]['sell_order_number'].append(["SO/"+str(int(re.findall('\d+',str(self.sell_product_data[product_name]['sell_order_number'][-1]))[0])+1).zfill(5)])
                   
    #call the start confirm sell order method to sell from product store
        if self.confirm_sale_order(Sale,product_name,int(selling_price),int(sell_quantity),manage_product_obj):
            print("\nProduct Sell successfully...")
            return int(selling_price*(manage_product_obj.sale_tax/100)+selling_price)*sell_quantity
        else:
            print("waning: something is wrong...")
            return 0
        
    def confirm_sale_order(self,product_name,selling_price,sell_quantity,manage_product_obj):
        """
            func:-remove the sell product from the manufactured quantity store and add total sale quantity
            param:-product name and it's datatype is string
            param:-selling price and it's datatype is integer
            param:-sell quantity and ir's datatype is integer
            param:-manage product object and it's manage the store of product and it's datatype is object
            return:-return true when performed this work
        """        
        print("\nDone")
        manage_product_obj.product_data[product_name]['sale_price'] += selling_price
        manage_product_obj.product_data[product_name]['total_sale_quantity'] += sell_quantity
        manage_product_obj.product_data[product_name]['manufactured_quantity'] -= sell_quantity
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        