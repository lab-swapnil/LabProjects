"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""
# Python Dictionary
# {2} Inserting an element

D = {1: 'one', 2: 'two'}

key = 3
value = 'three'

# Method-1
D[key] = value
print(D)

# Method-2
D.update({key:value})
print(D)

#Method-3
D.setdefault(key,value)
print(D)

''' Sample Output '''

# {1: 'one', 2: 'two', 3: 'three'}
# {1: 'one', 2: 'two', 3: 'three'}
# {1: 'one', 2: 'two', 3: 'three'}