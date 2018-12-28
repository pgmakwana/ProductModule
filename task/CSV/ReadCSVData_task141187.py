# Task  141187 date 13/12/2018
import csv
#this class create for read the data from csv file
class CSV_data_reading:
        
    csv_file=""
    csv_data_dict=dict()
    def __init__(self,csv_file_path):
        """
            func:- this function just initialize csv file path in one variable to use in this class
            param:-    one parameter is csv file path and it's datatype is string
            return:-
        """
        self.csv_file=csv_file_path
        
    def readData(self):
        """
            func:- read the data from csv file and store in dictionary throughout the all file data  
            param:-    
            return:-
        """
        #get the file or csv file data
        _line=[]
        csv_data=csv.reader(open(self.csv_file,"r"))
        for _index,_line in enumerate(csv_data):
            
            if _index == 0:
                #get the heading of csv file to set heading in dictionary
                title_name=_line
                continue
                        
            #create dictionary for new customer are found
            if not _line[4] in self.csv_data_dict.keys():
                self.csv_data_dict.update({_line[4]:{title_name[5]:'' ,title_name[6]:'',title_name[7]: '', title_name[8]: '', title_name[9] :'', title_name[10]: '',title_name[0]:'', 'PURCHASE_LIST' : []}})
                #store one by one row data in dictionary                
                self.csv_data_dict[_line[4]]['PURCHASE_LIST'].append(str([title_name[1]])+":"+str(_line[1])+","+str([title_name[2]])+":"+str(_line[2])+","+str([title_name[3]])+":"+str(_line[3]))
                self.csv_data_dict[_line[4]][title_name[0]]=_line[0]
                self.csv_data_dict[_line[4]][title_name[5]]=_line[5]            
                self.csv_data_dict[_line[4]][title_name[6]]=_line[6]
                self.csv_data_dict[_line[4]][title_name[7]]=_line[7]
                self.csv_data_dict[_line[4]][title_name[8]]=_line[8]            
                self.csv_data_dict[_line[4]][title_name[9]]=_line[9]
                self.csv_data_dict[_line[4]][title_name[10]]=_line[10]
            else:
                self.csv_data_dict[_line[4]]['PURCHASE_LIST'].append(str([title_name[1]])+":"+str(_line[1])+","+str([title_name[2]])+":"+str(_line[2])+","+str([title_name[3]])+":"+str(_line[3]))
                        
        for _key,_value in sorted(self.csv_data_dict.items()):
            print(_key,":",self.csv_data_dict[_key])
            
        
#created 'csv_data_reading_obj' object to access CSV_data_reading class function. 
csv_data_reading_obj=CSV_data_reading("/home/emipro/workspace/prakashm/task/CSV/import_sale_order_Final.csv")

#call read data function to read the data from csv and store it in dictionary
csv_data_reading_obj.readData()
