# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:48:31 2022

@author: saiom
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import re


#The followring summary provides a brief description of the input file, the process flow of the code and describes the methodolgy in processing the file
#The following code has been written for on the input file provided

#Pre-processing

#We identify the unwanted lines, unwanted set of patterns and remove them from the loaded data

#After sailing through the 2005proposal.pdf.txt (the input file), it is observed that there
#are a varirty line types.

#Type 1: The line contains the following format : MSA
#                                               : Example: Abilene, TX Metropolitan Statistical Area
#                                               : This line is identified using regural expressions with a patterns : 1) r"^([\w|\s|-]+), ([A-Z|-]+) ([\w|\s\-]+)" 
#                                                                                                                   : 2) r"^([\w|\s|-]+), ([A-Z|-]+)"

#Type 2: The line contains the following format : Basename
#                                               : Example: Navy-Marine Corps Reserve Center Akron
#                                               : This type of line is identified by eliminating pure text, eliminating the type 1 lines

#Type 3: THe line contains the following format : Action | Values | Base name | Action | Values 
#                                               : The line is identified by more than 1 %s in the line
#                                               : Example: Close (20) (2) 0 0 (20) (2) 0 (22) (15) (37) 727,010 0.0% Center, Frederick Fort Detrick Gain 0 0 76 43 76 43 (15) 104 81 185 727,010 0.0%


#Type 4: The line contains the following format : Action | Values ending with %
#                                               : The line is identified by only one % in the line
#                                               : Example: Gain 0 0 982 936 982 936 (29) 1,889 1,529 3,418 727,010 0.5%

#Type 5: The line contains the following format : Action | Values | %  | previous basename's residual 
#                                               : The line is identified by only one %, and location of the % is not at the end of the line
#                                               : Example: Close (31) 0 0 0 (31) 0 0 (31) (16) (47) 22,545 -0.2% Center Columbus                                    


#All other types: We either remove them during pre-processing of the file or ignore them, as they are not of use for the purpose of this project


#The code flow is as the following:
    #Load the data
    #Pre-process the data
    #Iterate through all lines in the loaded data
        #Identify the type of line
        #Process the line based on the type of line, as mentioned above
        #Structure the line, Example: remove ',' , remove white spaces
        #Append the line to the final data
    #Write the final data produced above to the output file

pdf_path = r'C:\Users\saiom\OneDrive\Documents\GitHub\homework-3-S-Omkar-K-1'
out_file_name = 'question2.csv'

# Function to load the input file
def read_pdf(file_name):
    file_path = os.path.join(pdf_path, file_name)
    f = open(file_path, mode = 'r', encoding="utf8")
    return f.readlines()


# Function to determine whether the line matches the MSA pattern, using regular expressions.
def get_msa(l):
    l = l.strip()
    pattern1 = r"^([\w|\s|-]+), ([A-Z|-]+) ([\w|\s\-]+)"
    pattern2 = r"^([\w|\s|-]+), ([A-Z|-]+)"
    for pattern in [pattern1, pattern2]:
        match = re.search(pattern, l)
        if pattern == pattern1:
            
            if match:
                name = match.group(1)
                state = match.group(2)
                #print(pattern)
                description = match.group(3)
                msa = name + ',' + ' ' + state + ' ' + description
                return True, msa
            
        if pattern == pattern2:
             
            if match:
                name = match.group(1)
                state = match.group(2)
                #print(pattern)
                msa = name + ',' + ' ' + state + ' ' 
                return True, msa
            else:
                return False, lines


        
# Function to check the type of line
def check_line_type(lines):
    if '%' in lines:
        length_of_lines = len(lines.strip())
        
        if lines.count('%') > 1: #has more than 2 %s in the line, so more than two rows
            line_type = 3
            return line_type, lines
        
        elif lines.count('%') == 1:
            if lines.strip()[length_of_lines - 1] == '%':
                line_type = 4
                return line_type, lines
        
            if lines.strip()[length_of_lines - 1] != '%':
                line_type = 5
                return line_type, lines
        else:
            line_type = 7
            return line_type, lines
        
        
    else:
        is_true_msa, lines = get_msa(lines)
        
        if is_true_msa:
            line_type = 1  #its an MSA line
            return line_type, lines
        else:
            line_type = 2  #basename only line
            return line_type, lines
    
# Function that processes each line based on the type of the line
def process_line(line_type, lines):
    ### process according to the type of line
    ### wirte the line into the file 
    
    if line_type == 1: # MSA type of line
        ### process according to the type of line
        is_true_msa, lines = get_msa(lines)
        if is_true_msa:
            print('processing for MSA only line : ' + lines)            
            return True, lines
        
    elif line_type ==2:
        print('processing for base_name only line : ' + lines)            
        return True, lines
    
    elif line_type == 3: 
                         
        Actions = ['Gain', 'Close', 'Realign', 'Close/Realign']
        #Get the first part of line Action | Values by using splitter %
        splitter = lines.index('%') 
        lines1 = lines[:splitter + 1]


        ##Get the second part of line Base name | Action | Values by using splitter %
        lines2 = lines[splitter+2:]
        count = 0
        found_action = ''
        for i in lines2.split():
            print(i)
            if i in Actions:
                found_action = i
                count = count + 1
        if count >0:
            line_2base_name, line_2values = lines2.split(found_action)
            action = found_action
            return True, lines1, line_2base_name, action, line_2values 
        
        
        

    elif line_type == 4: # here we have the format where  Action | Values ending with %
        Actions = ['Gain', 'Close', 'Realign', 'Close/Realign']
        count = 0
        found_action = ''
        for i in lines.split():
            if i in Actions:
                found_action = i
                count = count + 1
        if count >0:
            action = found_action
            
            if lines.split()[0] in Actions:
                #line_values = lines.split(action)
                line_values = lines.split(action)[1]
                return True, 'old_base_name', action, line_values
            else:
                new_base_name , line_values = lines.split(action)
                return True, new_base_name, action , line_values
    
    elif line_type == 5: # here we have the format  Action | Values | %  | basename residual 
        splitter = lines.index('%') 
        lines1 = lines[:splitter + 1]
        base_name_residual = lines[splitter+2:]
        return True, lines1, base_name_residual
    
    else:
        return False, lines

# Function to write the final data to the file   
def write_file(final_data):
    with open(os.path.join(pdf_path , out_file_name), 'w') as f:
        f.write('msa,base name,action,mil_out,civ_out,mil_in,civ_in,mil_net,civ_net,net_cont,direct,indirect,total,ea_emp,ch_as_perc')
        f.write('\n')
        for each in final_data:
            f.write(each + ',' + '\n' )



file_data = read_pdf('2005proposal.pdf.txt')
file_data = file_data[21:1843]
redundant_list = ['does not include',
                                    'Out In Net Gain/(Loss) Net Mission',
                                    'Economic Installation Action', 'Employment', 'Total*', 'Total',
                                    'Economic Area Installation Action']
removal_list = file_data[40:54]
removal_list.extend(redundant_list)
removal_list
#removal_list = [elem.replace('\n', '') for elem in removal_list]
#file_data = [elem.replace('\n', '') for elem in file_data]
for substring in removal_list:
    print(substring)
    for item in file_data:
        if substring in item:
            file_data.remove(item)
            



# Main class 
final_data = []
for lines in file_data:    
    line_type , lines = check_line_type(lines)    
    if line_type == 1:
        is_line_processed, lines = process_line(line_type, lines)
        msa = lines
    elif line_type == 2:
        is_line_processed, lines = process_line(line_type, lines)
        base_name = lines
    else:
        if line_type == 3:
            print(line_type)
            is_line_processed, lines1, line_2base_name, action, line_2values = process_line(line_type, lines)
            final_data.append('"' + msa.strip() + '"'+ ',' +
                              '"' + base_name.strip() + '"' + ',' +
                             lines1.strip().replace(',', '').replace(' ' , ',') 
                              ) 
            final_data.append('"' + msa.strip() + '"' + ',' + 
                             '"' + line_2base_name.strip() + '"' + ',' +
                             action.strip() + ',' + 
                             line_2values.strip().replace(',', '').replace(' ', ',') 
                             )      
        if line_type == 4:
            is_line_processed, new_base_name, action, line_values = process_line(line_type, lines)        
            if new_base_name == 'old_base_name':
                 final_data.append('"' + msa.strip() + '"' + ',' +
                                  '"' + base_name.strip() + '"' + ',' + 
                                  action.strip() + ',' +
                                  line_values.replace(',', '').strip().replace(' ', ',') 
                                  )
            else:
                final_data.append('"' + msa.strip() + '"' + ',' +
                                 '"' + new_base_name.strip() + '"' + ',' + 
                                 action.strip() + ',' +
                                 line_values.replace(',', '').strip().replace(' ', ',') 
                                 )
            
        if line_type == 5:
            
            is_line_processed, lines, base_name_residual = process_line(line_type, lines)
            
            base_name = base_name + base_name_residual
            final_data.append('"' + msa.strip() + '"' + ',' +
                             '"' + base_name.strip() + '"' + ',' +
                             lines.replace(',', '').strip().replace(' ', ',') 
                             )
        if line_type == 6:
            is_line_processed, lines = process_line(line_type, lines)
        
#Call write_file function to write the final data to the file
write_file(final_data)  
    
        


    
    
  
    
    
    
    
    