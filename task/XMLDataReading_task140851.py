# Task  140851 date 07/12/2018
import os
import xml.etree.ElementTree as ET

class XML_data_manage:
   
    def get_xml_data(self,xml_filea_path): 
        """
            func:- In this function get xml data from xml file and information about the inputed id from user
            param:- xml_file_path and it's datatype should be string and it's xml file            
            return:- 
        """                
        xml_document = ET.parse(xml_filea_path)
        root_dir=xml_document.getroot()
        
        inputed_tag=input("\nInput tag to get information:")
        check_id=0
        for sub_dir in root_dir.findall('template'):
            if sub_dir.attrib['id']==inputed_tag:
                check_id=1            
                for node in sub_dir.getiterator():                
                    if node.tag == 'link':
                        print(node.tag,"::  rel:-",node.attrib['rel'],"href:-",node.attrib['href'])
                        
                    if node.tag == 'script':
                        print(node.tag,"::  Type:-",node.attrib['type'],"src:-",node.attrib['src'])       
                break   
            
        if not check_id == 1:
            print("Tag Not Found...")   
        
xml_data_manage_obj=XML_data_manage()
xml_filea_path="item_xml.xml"    
xml_data_manage_obj.get_xml_data(xml_filea_path)

