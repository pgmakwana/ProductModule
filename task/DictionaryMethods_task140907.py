# Task  140907 date 08/12/2018
import datetime
import calendar
from collections import Counter
from time import strptime
from audioop import reverse

sell_product={'APR':'200', 'MAY':'200', 'jun':'230', 'JUL':'210', 'aug':'190', 'sep':'200', 'oct':'230', 'NOV':'230', 'DEC':'210', 'jan':'200','FEB':'230','mar':'210'}
purchase_product={'APRIL':'200', 'may':'230', 'JUN':'200', 'july':'220', 'august':'190', 'SEPTEMBER':'200', 'october':'210', 'NOVEMBER':'230', 'december':'210', 'january':'200','FEBRUARY':'230','march':'210'}

#this loop use for menu system
while 1:    
    
    print("\n0]Sort by nested dictionary value\n1]Sort by Month alphabetically \n2]Sort by it's Value \n3]Get Key by sorting Values\n4]Sort by lower and upper key Value \n5]Sort it by most Repeats Value \n6]Sort it by Even and odd number of month.\n7]Sort it By Number of Days of month. \n8]Exit")
    
    option_select=input("Select: ")
    
   
    #sorted by sub dictionary value
    if(option_select=='0'):
        
        product_quantity={'APR':{'qty':200}, 'MAY':{'qty':250}, 'jun':{'qty':150}, 'JUL':{'qty':230}, 'aug':{'qty':200}, 'sep':{'qty':350}, 'oct':{'qty':190}, 'NOV':{'qty':260}, 'DEC':{'qty':215}, 'jan':{'qty':210},'FEB':{'qty':195},'mar':{'qty':250}}
        
        def sort_by_quantity(quantity):
            """
                func:-    sort quantity as increasing order or decreasing order from by month.
                param:-    key is a name of month and it's datatype is string.
                return:-    return the available quantity from the month and datatype is integer.
            """
            key,quantity_value=quantity            
            return product_quantity[key]['qty']
        
        #pass the month name to find available quantity to sort it.
        print(sorted(product_quantity.items(), key = sort_by_quantity,reverse=True))
        
        continue
    
    #1]Sort by Month alphabetically
    if(option_select=='1'):
        #Sort product by Month in ascending order  
        sell_product=sorted(sell_product.keys(),key=str.upper)
        print("Sorted By dictionary key:",sorted(sell_product,key=str.upper))
        #Sort product by Month in descending order
        print("Sorted By dictionary key in reverse order:",sorted(sell_product,reverse=True))

    #2]Sort by it's Value                      
    elif(option_select=='2'):
        #Sort product by product in ascending order
        print("Sorted By dictionary key:",sorted(sell_product.keys()))
        ##Sort product by product in descending order
        print("Sorted By dictionary key in reverse order:",sorted(sell_product.keys(),reverse=True))
     
    #3]Get Key by sorting Values    
    elif(option_select=='3'):
        #Get the sorted month name from sorted product
        print("Get key by sorted value",sorted(sell_product,key=sell_product.__getitem__))
    
    #4]Sort by lower and upper key Value   
    elif(option_select=='4'):
        #Sort product by month in upper case
        print(sorted(sell_product.keys()))
        #Sort product by month in lower case
        print(sorted(sell_product.keys(),reverse=True))
    
    #5]Sort it by most Repeats Value    
    elif(option_select=='5'):
        
        #Get the most repeated product from the stock
        total_product_count = Counter(sell_product.values())        
        max_value=max(total_product_count,key=total_product_count.get)
        find_max_value=-1
        #from the total_product_count to get max value and show the most repeated product
        for key,value in total_product_count.items():
            if find_max_value==value:
                print(key)
            if key==max_value :
                print(key)
                find_max_value=value
    
    #6] Sort by Even and odd number of month.     
    elif(option_select=='6'):        
        print(sell_product)
        
        def oddEvenCheck(key):
            """
                func:- Get the month and check it's even or odd as per user needed and return it.  
                param:- key and it's datatype is string. In this key get the name of month
                return:- return the value even,odd or 2,1 
            """
            if(strptime(key,'%b').tm_mon) % 2 == 0:
                return "even" or 2
            else:
                return "odd" or 1
            
        #from this print method to print odd/even month and it can use calling for key in sorted method. 
        print(sorted(sell_product,key=oddEvenCheck,reverse=False))
    
    #7]Sort it By Number of Days of month.    
    elif(option_select=='7'):
        
        def dayOfMonth(key):
            """
                func:- Get the day of month from month name and sort by day.  
                param:- key and it's datatype is string. In this key get the name of month
                return:- return number of day in month in integer.
            """
            now = datetime.datetime.now()
            return calendar.monthrange(now.year,strptime(key,'%b').tm_mon)[1]
            
        #from this print method sort number of day in month of all month. 
        print(sorted(sell_product,key=dayOfMonth,reverse=False))        
                    
    #exit
    elif(option_select=='8'):
        break

    else:
        #When user input wrong option.
        print("\nSomething Is Wrong!!! Retry...")
        