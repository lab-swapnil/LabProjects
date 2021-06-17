"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {6} Mapping two Sequences

# sequence-1
keys = (1, 2, 3)

# sequence-2
values = ('one', 'two', 'three')

# using zip() to read two sequences at a time
D = { k:v for k,v in zip(keys,values) }

# printing dictionary D
print(D)

''' Sample Output '''
# {1: 'one', 2: 'two', 3: 'three'}