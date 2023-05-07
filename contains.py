
# Check if a value is contained in a list

L = ['One', 'Two', 'Three', 'Four', 'Five']

if 'Two' in L:
    print('Two is in the list.')
else:
    print('Two is not in the list.')
    

# OK version 🤔 - For loop and a equality check ❌


L = ['One', 'Two', 'Three', 'Four', 'Five']

V = 'Two'

for i in range(len(L)) :
    if V == L[i] :
        print(f'{V} is Contains in the List')
