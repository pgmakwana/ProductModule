# Task  140996 date 11/12/2018

class TaxCalculation:
    
    def get_tax(self,product_price,transactiona_type,product_type):
        """
            func:- Calculate the GST from the get price and check it's purchase or sell     
            param:- product price is the amount to calculate the GST and it's datatype is float.
            param:-  transaction_type to check it's puchase or sell and it's datatype is string. 
            return:-   total of CGST and SGST and it's datatype is float.
        """
        #check the transaction type is purchase or not
        if transactiona_type == "PURCHASE":
            #CGST = 10% & SGST = 12%
            CGST_tax=product_price*(10/100)
            SGST_tax=product_price*(12/100)
            
            return CGST_tax+SGST_tax
        
        #check the transaction type is sell and stock type or not
        elif transactiona_type == "SELL" and product_type=="STOCK":
            #CGST = 18% & SGST = 12%
            CGST_tax=product_price*(18/100)
            SGST_tax=product_price*(12/100)
            
            return CGST_tax+SGST_tax
        
        #at the transaction type is sell and not stock type
        else:
            #CGST = 18% & SGST = 12%
            CGST_tax=product_price*(13/100)
            SGST_tax=product_price*(15/100)
            
            return CGST_tax+SGST_tax