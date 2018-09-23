'''
Version 0.1
Author : Anil Sharma
Description: This script checks transactions and update position on daily basis.

'''


import json
import csv
from pprint import pprint
import os
import os
#########  Check Files ############
if os.path.exists("Input_StartOfDay_Positions.txt"):
  pass
else:
  print("The file Input_StartOfDay_Positions.txt does not exist")
  exit (0)
##########  Check if transaction file is avl
if os.path.exists("Input_Transactions.txt"):
  pass
else:
  print("The file Input_Transactions.txt does not exist")
  exit (0)
  
#### Load Daily Transaction File jason file into dictionary 
with open('Input_Transactions.txt') as f:
    Trn_data = json.load(f)
#pprint(Trn_data)
############## Processing ########

line_count = 0

input_position=open('Input_StartOfDay_Positions.txt','r')
EOD_position=open('Input_ENDOfDay_Positions.txt','w')
for positions in input_position:
    for Trn in Trn_data:
      if line_count == 0:
         #   print(f'{",".join(row)}')
             print("Header of file ",positions,end='')
             line_count += 1
      else:
             list_file=positions.strip().split(",")
            # print("lower",Trn['Instrument'])
           #  print ("hi")
             if Trn['Instrument'] in list_file:
                 if Trn['TransactionType'] =='B':
                       if list_file[2] =='E':  
                            line=Trn['TransactionType'] + ',' + Trn['Instrument'] + ',' + list_file[1] +',' + list_file[2] + ','+ str((int(list_file[3]) + int(Trn['TransactionQuantity']))) +'\n'
                            EOD_position.write(str(line))
                           # Quantity=Quantity + TransactionQuantity
                          
                       elif list_file[2] =='I':
                             line=Trn['TransactionType'] + ',' + Trn['Instrument'] + ',' + list_file[1] +',' + list_file[2] + ','+ str((int(list_file[3]) - int(Trn['TransactionQuantity']))) +'\n'
                             EOD_position.write(str(line))
                            # Quantity=Quantity - TransactionQuantity
                       else:
                            print ("Unknown Accoun Type")
                 elif Trn['TransactionType'] =='S':
                       if list_file[2] =='E':  
                            line=Trn['TransactionType'] + ',' + Trn['Instrument'] + ',' + list_file[1] +',' + list_file[2] + ','+ str((int(list_file[3]) - int(Trn['TransactionQuantity']))) +'\n'
                            EOD_position.write(str(line))
                            # Quantity=Quantity - TransactionQuantity
                       elif list_file[2] =='I':
                            line=Trn['TransactionType'] + ',' + Trn['Instrument'] + ',' + list_file[1] +',' + list_file[2] + ','+ str((int(list_file[3]) + int(Trn['TransactionQuantity']))) +'\n'
                            EOD_position.write(str(line))
                            # Quantity=Quantity + TransactionQuantity
                       else:
                            print ("Unknown Account Type")
                 else:
                            print ("Unknown Transaction Type") 
             line_count += 1
             # print ("hello")
        
EOD_position.close()
input_position.close()


 

