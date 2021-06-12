"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""
# Python Dictionary
# {1} Printing keys, values & items

D = {1: 'ONE', 2: 'TWO', 3: 'THREE'}
print('dictionary D:')
print(D)

print()

vKeys = D.keys()
print('Keys in dict D:')
for k in vKeys:
    print(k)
    
print()

vValues = D.values()
print('Values in dict D:')
for v in vValues :
    print(v)

print()

vItems = D.items()
print('Items in dict D:')
for k,v in vItems:
    print(k,':',v)

''' Sample Output '''
# dictionary D:
# {1: 'ONE', 2: 'TWO', 3: 'THREE'}

# Keys in dict D:
# 1
# 2
# 3

# Values in dict D:
# ONE
# TWO
# THREE

# Items in dict D:
# 1 : ONE
# 2 : TWO
# 3 : THREE