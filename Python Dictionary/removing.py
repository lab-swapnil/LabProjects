"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {3} Removing an element

D = {1:'one', 2:'two', 3:'three'}
print(D , end='\n\n')

# Method-1
key = 1
del D[key]
print(D , end='\n\n')

#Method-2
key = 2
val = D.pop(key)
print('value:', val)
print(D, end='\n\n')

#Method-3
item = D.popitem()
print('item:', item)
print(D)

''' Sample Output '''
# {1: 'one', 2: 'two', 3: 'three'}

# {2: 'two', 3: 'three'}

# value: two
# {3: 'three'}

# item: (3, 'three')
# {}