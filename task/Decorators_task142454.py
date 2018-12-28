
#A decorator takes in a function, adds some functionality and returns it.
  
def is_called():
    """
        func:just print the hello when create the is_called function.
        param:
        return:in return line call the is_returned function to call it.
    """
    def is_returned():
        """
            func:print the hello whenever call the is_returned method from the return line of is_called function.
            param:
            return:
        """
        print("Hello")
        
    return is_returned
 
 
new = is_called()
print(new(),'a')

##############################################################################################################################
 

def inc(x):
    """
        func:get the x value and increment it one by one.
        param:x parameter and it's datatype is integer.
        return:add one in x and return it and it's datatype is integer.
    """
    return x + 1
 
def dec(x):
    """
        func:get the x value and decrement it one by one.
        param:x parameter and it's datatype is integer.
        return:decrement one from x and return it and it's datatype is integer.
    """
    return x - 1
 
def operate(function_name, x):
    """
        func:set function and value to performed which kind of functionality you want to use and return performed value.
        param:function name and it's datatype is function.
        param:x parameter and it's datatype is integer.
        return:return performed value in integer datatype.
    """
    #assign function name and parameter in result variable.
    result = function_name(x)
    return result
 
#call the operate function and pass the functionality name to performed it and get the value from operation 
print(operate(dec,20))
print(operate(inc,20))
   
##############################################################################################################################
   

def make_pretty(function_name):
    """
        func:whenever call make_pretty function then it's called inner function whenever return line are compile and then inner function call ordinary function     
        param:function_name get the name of function and call it from inner method and datatype is method.
        return:in return call the inner method. 
    """
    def inner():
        """
            func:this inner method just print the 'i got decorated' and call the function are gated in make_pretty method.
            param:
            return:
        """
        print("I got decorated")
        function_name()
    return inner
 
def ordinary():    
    print("I am ordinary")
     
#make_pretty() is a decorator assign it self in make_pretty method to call it self from make_pretty method
ordinary=make_pretty(ordinary)
#call the ordinary method but in this a make_pretty method so first call it and after call ordinary method.
print(ordinary())
##############################################################################################################################
   
def smart_divide(function_name):
    """
        func:this method check the divider is zero or not, from the inner method if not then call divide method we just get in parameter..  
        param:function name,this parameter get the name of function and it's datatype is function.
        return:return in call the function we get in parameter with both integer argument. 
    """
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return function_name(a,b)    
    return inner
 
#We can use the @ symbol along with the name of the decorator function 
def divide(a,b):
    """
        func:division of two value and return the answer of this value.but we can get the argument from the smart_divide method.
        param:a is divisor value and it's datatype is integer.
        param:b is divider and  it's datatype is integer.
        return:return the answer of division value and it's datatype is float
    """
    return a/b
divide=smart_divide(divide)
#call the divide method but first call the smart_devide and check the divider is zero or not after checking divide the value and print the answer. 
print(divide(int(input("enter value for no 1: ")),int(input("enter value for no 2: ")))) 
     
##############################################################################################################################     
    
    
    
    
    
    
    
    
    
    
    
    