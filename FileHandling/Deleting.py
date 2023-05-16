import shutil
import os
print(os.getcwd())

# print(os.rmdir('/home/vishal/Boring_Stuff_With_Python/spamspamspam/'))

# shutil.rmtree('/home/vishal/Boring_Stuff_With_Python/spamspamspam/')

# Dry Run...

for filename in os.listdir() :
    if filename.endswith('.py'):
        print(filename)
        os.unlink(filename)

# print(os.listdir())
# os.unlink('spam.txt')
# print(os.listdir())
