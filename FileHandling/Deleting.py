import shutil
import os
print(os.getcwd())

# print(os.rmdir('/home/vishal/Boring_Stuff_With_Python/spamspamspam/'))

# shutil.rmtree('/home/vishal/Boring_Stuff_With_Python/spamspamspam/')

# Dry Run...

for filename in os.listdir() :
    if filename.endswith('.txt'):
        print(filename)
        os.unlink(filename)


