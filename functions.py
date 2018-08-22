import sys
import re
from tables import  *

label_table, user_def_var = {}, {}
nxt_program_address = 0
nxt_memory_adddress = 16

def assembler() :
  f = open(sys.argv[1]).readlines()
  for line in f :
    if line.strip():
       if not line.startswith("//"):
          first_pass(line.strip())
  for line in f :
    if line.strip():
       if not line.startswith("//"):
          second_pass(line.strip())
  print("machine code saved in file output.hack")            






def first_pass(line):
 global label_table
 global nxt_program_address
 token = re.split('(\(|\)|=|;|@)',line)
 if token[1] == '(':
     if token[2] not  in label_table:
       label_table[token[2]]  = nxt_program_address
       
 nxt_program_address  += 1






def second_pass(line):
  global nxt_memory_address
  global user_def_var
  f =  open("outputfile.hack",'a')
  token = re.split('(\(|\)|=|;|@)',line)
  if token[1] ==  '(' :
    return
  if token[1] == '=':
    a = '111' + comp_table[token[2]] + dest_table[token[0]] + '000' + '\n'
    f.write(a)
    return
  if token[1] ==  ';':
    a  =  '111' + comp_table[token[0]] + '000' + jump_table[token[2]] + '\n'
    f.write(a)
    return
  if token[1] == '@':
     if token[2].isdigit():
       a  = '0' + format(int(token[2]),'015b') +'\n'
       f.write(a)
       return
     if token[2] in label_table:
       a = '0' + format(label_table[token[2]], '015b') + '\n'
       f.write(a)
       return    
     if token[2] in predef_table:
       a = '0' + format(predef_table[token[2]], '015b') + '\n'
       f.write(a)
       return
     if token[2] in user_def_var: 
       a = '0' + format(user_def_var[token[2]], '015b') +'\n'
       f.write(a)
       return
     user_def_var[token[2]] = next_memory_address
     a = '0' + format(next_memory_address,  '015b') + '\n'
     f.write(a)
     next_memory_address  += 1
     return
  else:
     return        
              

def assembler() :
  f = open(sys.argv[1]).readlines()
  for line in f :
    if line.strip():
       if not line.startswith("//"):
          first_pass(line.strip())
  for line in f :
    if line.strip():
       if not line.startswith("//"):
          second_pass(line.strip())
  print("machine code saved in file output.hack")     



















 

