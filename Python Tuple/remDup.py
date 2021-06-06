"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Tuples
# {6} Removing Duplicate values

# Method-1
T = (1,2,3,2,1,4,5)
New = set(T)
print(tuple(New))

# Method-2
New = []
for e in T:
    if e not in New:
        New.append(e)
print(tuple(New))

''' Sample Output '''
# (1,2,3,4,5)
# (1,2,3,4,5)