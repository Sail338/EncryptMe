from simplecrypt import encrypt,decrypt as crypt
import simplecrypt
import hashlib
import sys
import os
import shutil
import argparse
#
listOfFiles = []
password = ""
def setPass(args):
    file = open("user_config.conf\n","w")

    password = args
    file.write(password)

    file.close()

def encrypt_f(args):
    #add files
     password = open("user_config.conf","rb").read()
     if password == '':
         print("Please set password")
     else:
        if(args !=''):
            listOfFiles.append(args)
        for file in listOfFiles:
            rey = hashlib.sha256(password).digest()
            for i in range (10000):
                rey = hashlib.sha256(rey).hexdigest()
            with open(file, 'rb') as fo:
                plaintext = fo.read()
                enc = encrypt(rey, plaintext)
            with open(file, 'wb') as fo:
                fo.write(enc)
                fo.close()
def decrypt_f(args):
    cyper = open(args,'rb').read()
    rey = hashlib.sha256(password).digest()
    for i in range (10000):
        rey = hashlib.sha256(rey).hexdigest()
    l = simplecrypt.decrypt(rey,cyper)
    x = open(args,'wb')
    x.write(l)

def help():
    print("Usage encrypt('key',filename)")
    print("if its a directory u can encrypt all all files within those direcories with -r arg, or s specfic directory with -r [directories]")
def recursiveHelper(args):
    print "doing something"
    print (args[0])
    if os.path.isdir(args):
        for root,dirs,files in os.walk(args):
            for file in files:
                if(file == ".DS_Store"):
                    continue
                if(file == "encrypt.py"):
                    continue
                if(file == ".tern-project"):
                    continue
                filepath = os.path.join(root,file)
                listOfFiles.append(filepath)
        return listOfFiles
#("../cmds")


#pars args
parser = argparse.ArgumentParser()
parser.add_argument("-e",type = encrypt_f)
parser.add_argument("-d",type = decrypt_f)
parser.add_argument("-re",type = recursiveHelper)
parser.add_argument("-k",type = setPass)
args = parser.parse_args()
print (args)
