import os

for folderName, subfolders, filenames  in os.walk('/home/vishal/Boring_Stuff_With_Python/File') :

    print('The Folder is ' + folderName)
    print('The Demo is ' + subfolders)
    for filename in filenames :
        print('The current file is ' + filename)
        print('The Subfolder in ' + folderName + 'are: ' + str(subfolders))
        print('The Filename in ' + folderName + ' are: ' + str(filename))
        print()