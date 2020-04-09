#!/usr/bin/env python
# coding: utf-8

# In[1]:


import zipfile
def extractfile(zfile, password):
    try:
        zfile.extractall(pwd=password)
        return password
    except:
        return
def main():
    zfile = zipfile.ZipFile('/root/adcd/fayaz/test.zip')
    passfile = open('/root/adcd/fayaz/wordlist.txt')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess = extractfile(zfile,password)
        if guess:
            print 'Password = ' + password + '\n'
if __name__ == '__main__':
    main()


# In[ ]:





