
import datetime
import re
from Product_Management import Product

class Purchase:
    
    purchase_product_data=dict()
    purchase_state=''
        
    def purchase_product(self,product_name,product_type,company_name,max_purchase_price,purchase_tax):
        """
            func:-It will create new purchase order, set datetime(Set current time in UTC timezone), total_price, supplier_name,list of  purchase_items and its quantity, purchase number and state to draft. company_name, returns new purchase order or warning message
            param:-company_name it's name of product and it's datatype is string.
            param:-prooduct_type is stock or consumable and it's datatype is string.
            param:-company name and it's datatype is string.
            param:-current time and it's datatype is date.
            param:-purchase_tax use for tax counting when purchase the product and it's datatype is integer
            return:-purchase price and it's datatype is integer or warning message if occur any error.
        """
        
        self.purchase_state='draft'
        
        product_quantity=input('Enter Product quantity: ')
        total_rupies=input('Enter RS(as one quantity): ')        
        if product_quantity.isdigit()==False or total_rupies.isdigit()==False:
            print("Warning: Wrong data are input...")
            return 0 
        
        if max_purchase_price < int(total_rupies) :
            print("Warning: Wrong data are input...")            
            return 0
        supplier_name=input('Enter Supplier name: ')        
        total_rupies=int(total_rupies)
        #first time company purchase the product
        if not company_name in self.purchase_product_data.keys():     
            
#         self.max_purchase_price=input('Enter Maximum Purchase Price: ')
#         self.max_sale_discount=input('Maximum Sale Discount(in percentage): ')
#         self.purchase_tax=input('Purchase Tax(in percentage): ')
#         self.sale_tax=input('Sale Tax(in percentage): ')
#         self.minimum_stock_level=input('Minimum Stock Level(only for stockable): ')
            
                   
            self.purchase_product_data.update({company_name:{}})
            self.purchase_product_data[company_name].update({'purchase_items':[]})
            self.purchase_product_data[company_name].update({'purchase_quantity':[]})
            self.purchase_product_data[company_name].update({'supplier_name':[]})
            self.purchase_product_data[company_name].update({'timezone':[]})            
            self.purchase_product_data[company_name].update({'total_rupies':total_rupies})            
            self.purchase_product_data[company_name].update({'company_name':company_name})
            self.purchase_product_data[company_name].update({'product_name':product_name})
            self.purchase_product_data[company_name].update({'product_type':product_type})
            self.purchase_product_data[company_name].update({'purchase_order_number':[]}) 
            self.purchase_product_data[company_name]['supplier_name'].append(supplier_name)
            self.purchase_product_data[company_name]['purchase_items'].append(product_name)
            self.purchase_product_data[company_name]['timezone'].append(datetime.datetime.utcnow().date())
            self.purchase_product_data[company_name]['purchase_quantity'].append(int(product_quantity))           
            self.purchase_product_data[company_name]['purchase_order_number'].append(["PO/"+str(int(re.findall('\d+',"1")[0])).zfill(5)])

        else:
            #check the product all ready purchased or not         
            if not product_name in self.purchase_product_data[company_name]['purchase_items']:
                self.purchase_product_data[company_name]['purchase_items'].append(product_name)
                self.purchase_product_data[company_name]['supplier_name'].append(supplier_name)           
                self.purchase_product_data[company_name]['timezone'].append(datetime.datetime.utcnow().date())     
                self.purchase_product_data[company_name].update({'product_name':product_name})
                self.purchase_product_data[company_name]['purchase_quantity'].append(int(product_quantity))
            else:            
                self.purchase_product_data[company_name]['purchase_quantity'][int(self.purchase_product_data[company_name]['purchase_items'].index(product_name))] += int(product_quantity)            
            self.purchase_product_data[company_name]['total_rupies'] = (total_rupies+self.purchase_product_data[company_name]['total_rupies'])//2
            self.purchase_product_data[company_name].update({'supplier_name':supplier_name})
            self.purchase_product_data[company_name]['purchase_order_number'].append(["PO/"+str(int(re.findall('\d+',str(self.purchase_product_data[company_name]['purchase_order_number'][-1]))[0])+1).zfill(5)])
            #add purchase tax in purchasable price as one product
        total_purchase_price=int(total_rupies*(purchase_tax/100)+total_rupies)    
        #call the confirm purchase method to store all the product in product store
        if self.confirm_purchase_order(Purchase,product_name,int(product_quantity),total_purchase_price,product_type,company_name):
            print("raw material purchase successfully...")
            return total_purchase_price*int(product_quantity)
        else:
            print("waning: something is wrong...")
            return 0
        
    def confirm_purchase_order(self,product_name,product_quantity,total_rupies,product_type,company_name):
        """
            func:-get the data from purchase_product method and it's all data set in Product class.
            param:-product_name and it's data type is string
            param:-product_quantity and it's data type is integer
            param:-total_rupies and it's data type is integer
            param:-product_type and it's data type is string
            param:-company_name and it's data type is string
            return:-if state done return true or else false 
        """                
        Product.insert_product(Product,product_name,product_quantity,total_rupies,product_type,company_name)
        self.purchase_state='done'
        return True
        
        
        
        