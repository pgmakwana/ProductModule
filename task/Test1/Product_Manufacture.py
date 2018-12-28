
#date time is import for we need utc timezone
import datetime
import re

class Manufacture_product:
    
    manufacture_product_data=dict()
    
    def create_manufacture(self,product_name,product_quantity,product_obj,company_name):
        """
            func:-Manufacture the product and store all kind of manufacture data.
            param:-product name to manufacture he product and it's datatype is string
            param:-product quantity to produce the this quantity product and it's datatype is integer
            param:-product object to access the product class data and it's datatype is object 
            return:-if done all the process the Manufacture number and it's datatype is string
        """
        print('draft')
        
        #first time company manufacture the product
        if not product_name in self.manufacture_product_data.keys():            
            self.manufacture_product_data.update({product_name:{}})
            self.manufacture_product_data[product_name].update({'product_items':[]})
            self.manufacture_product_data[product_name].update({'product_quantity':[]})
            self.manufacture_product_data[product_name].update({'manufactured_quantity':[]})
            self.manufacture_product_data[product_name].update({'timezone':datetime.datetime.utcnow().date()})            
            self.manufacture_product_data[product_name].update({'company_name':company_name})     
            self.manufacture_product_data[product_name].update({'manufacture_order_number':[]})   
            self.manufacture_product_data[product_name]['manufactured_quantity'].append(product_quantity)            
            self.manufacture_product_data[product_name]['product_items'].append(product_name)
            self.manufacture_product_data[product_name]['product_quantity'].append(int(product_quantity))         
            self.manufacture_product_data[product_name]['manufacture_order_number'].append(["MO/"+str(int(re.findall('\d+',"1")[0])).zfill(5)])
            #call the start manufacturing method to add manufacture product in product store
            if self.start_manufacturing(Manufacture_product,product_name,product_quantity,product_obj):
                if self.done_manufacturing(Manufacture_product,product_name,product_quantity,product_obj):
                    print("\nProduct Manufacturing successfully...")
                    return self.manufacture_product_data[product_name]['manufacture_order_number'][-1]
            else:
                print("waning: something is wrong...")
                return "waning: something is wrong..."
        else:
            #check the product all ready manufactured or not 
            if not product_name in self.manufacture_product_data[product_name]['product_items']:
                self.manufacture_product_data[product_name]['product_items'].append(product_name)
                self.manufacture_product_data[product_name]['product_quantity'].append(int(product_quantity))
            else:            
                self.manufacture_product_data[product_name]['product_quantity'][self.manufacture_product_data[product_name]['product_items'].index(product_name)] += product_quantity    
            
            self.manufacture_product_data[product_name]['manufacture_order_number'].append(["MO/"+str(int(re.findall('\d+',str(self.manufacture_product_data[product_name]['manufacture_order_number'][-1]))[0])+1).zfill(5)])
            #call the start manufacturing method to add manufacture product in product store
            if self.start_manufacturing(Manufacture_product,product_name,product_quantity,product_obj):
                #call the done manufacturing method to remove raw material product from product store
                if self.done_manufacturing(Manufacture_product,product_name,product_quantity,product_obj):
                    print("\nProduct Manufacturing successfully...")
                    return self.manufacture_product_data[product_name]['manufacture_order_number'][-1]
            else:
                print("waning: something is wrong...")
                return "waning: something is wrong..."
        
    def start_manufacturing(self,product_name,product_quantity,product_obj):
        """
            func:-start the manufacturing and add manufactured product in product store
            param:-product_name and it's data type is string
            param:-product_quantity and it's data type is integer
            param:-product object and it's data type is object            
            return:- true or false. 
        """
        self.manufacture_state='In Progress'                
        product_obj.product_data[product_name]['manufactured_quantity'] += product_quantity
        return True
    def done_manufacturing(self,product_name,product_quantity,product_obj):
        """
            func:-whenever all process complete then remove the raw quantity from product store. 
            param:-product_name and it's data type is string
            param:-product_quantity and it's data type is integer
            param:-product object and it's data type is object            
            return:- true or false. 
        """        
        print('done')           
        product_obj.product_data[product_name]['raw_material_quantity'] -= product_quantity
        return True
    
        
        