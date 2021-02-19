import os
import subprocess

print('write the name and type ex "file_name file", "foler_name folder", "script_name script"')
name,type_name = input().split()

os.chdir('/')
for root, dirs, files in os.walk('/'): 
    if type_name == 'file':
        for file in files:
            if str(file) == name:
                print(root+'/'+str(file))

    if type_name == 'folder':
        for folder in dirs:
            if str(folder) == name:
                print(root+'/'+str(folder))

    if type_name == 'script':
        for file in files:
            if file.endswith('.sh') and str(file) == name:
                print(root+'/'+str(file))

