import os

print(os.path.join('Folder1', 'Folder2', 'File1.png'))

print(os.sep)

print(os.getcwd())

# Absolute and Relative Paths

print(os.path.abspath('File1.png'))

print(os.path.relpath('File1.png'))

print(os.chdir('/home/vishal/'))

print(os.getcwd())

print(os.path.isabs('/Borinf_Stuff_With_Python/'))

