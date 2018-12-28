# Task  140552 date 03/12/2018

#C_gst class for central tax calculating
class C_gst:    
   
    def get_tax(self,sale_amount):
        """ 
            func:- This function calculates central tax from the sales amount
            param:- sale_amount and it's datatype is integer
            return:- return central gst and it's datatype is Float
        """
        return sale_amount*(18/100)
    
#S_gst class for State tax calculating and inherit C_gst class
class S_gst(C_gst):    
    
    def get_tax(self,sale_amount):       
        """
            func:- This function calculate central tax from the sales amount
            param:- sale_amount and it's datatype is integer
            return:- return state gst and central gst and it's datatype is Float
        """        
        #call C_gst class method get_tax to get central gst
        c_gst=super().get_tax(sale_amount)
        return c_gst,sale_amount*(12/100)
    
#Sales class create for get cgst and sgst tax amount from the both classes are derived
class Sales(S_gst):    
    
    def sale(self,sale_amount):
        """
            func:- This function use for get calculated tax from the both class C_gst and S_gst and pass amount from to this class
            param:- sale_amount and it's datatype is integer
            return:- return total amount add with a taxable amount and it's datatype is Float 
        """        
        #calling S_gst class method to get cgst and sgst in a Float
        c_gst,s_gst=self.get_tax(sale_amount)        
        print("Central Tax :-",c_gst)
        print("State Tax :-",s_gst)
        return c_gst+s_gst+sale_amount    
    
    def get_tax(self,sale_amount):
        c_gst,s_gst=super().get_tax(sale_amount)
        return c_gst,s_gst
    
  
total_sale_amount=input("Enter Total Sale Amount:")

if total_sale_amount.isdigit()==True and float(total_sale_amount)>=0:
    
    #create 'obj_sale' object of the Sales class 
    sale_obj=Sales()
    
    #calling Sales class get_tax method to get total amount with tax 
    total_payble_amount=sale_obj.sale(float(total_sale_amount))
    print("Total payble amount is:",total_payble_amount)
else:
    print("Enter amount in only numeric format or positive...")




    
    