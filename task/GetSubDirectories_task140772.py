# Task  140772 date 03/12/2018 
import os
#this class create for get sub directory from given directory
class ManageDirectory:

    def get_directory(self,directory_path,counter):
        """
            func:- This get sub directory from the main directory but in this method we will use a function recursion to call it self to the last of sub directory and
            param:- directory_path and it's datatype should be string
            param:-   counter and it's datatype should be integer it's use for tab intent
            return:-  
        """
        for sub_directory in os.listdir(directory_path):
            if os.path.isdir(directory_path+"/"+sub_directory):
                tab_intent=' '* 4 *(counter)                
                counter += 1
                print(tab_intent+"'--/"+os.path.basename(sub_directory))                 
                #this place to call this function it self to the last sub directory from the main directory            
                self.get_directory(directory_path+"/"+sub_directory, counter)
                #whenever we back from directory then intent are minus one tab to decrement it
                counter -= 1
            else:
                tab_intent=' '* 4 *(counter)
                #print leaf directory file at the end
                print(tab_intent+"'-->"+os.path.basename(sub_directory))                    
                            
#create 'directory_manage_obj' object of ManageDirectory class         
directory_manage_obj=ManageDirectory()
directory_string=input("\nEnter Directory: ")

#this condition check to directory are empty or not    
if directory_string=='':
    print("\nPlease enter directory it's empty")                
else:
    #check the directory available or not in your system
    if os.path.isdir(directory_string) == True:        
        #call to this method to get directory tree form from given this directory  
        print(os.path.basename(directory_string))      
        directory_manage_obj.get_directory(directory_string,1)      
    else:
        print("This directory is not available in your system")
        
        