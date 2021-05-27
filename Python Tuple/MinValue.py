"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.Visit my Lab to 
    learn more.
"""

# Python Tuple Exercises
# {1} Minimum value in Tuple



# Using min()
T = (1, 4, 7, 2, 8, 9, 5)
print(min(T))

# Using sorted()
l = sorted(T)
print(l[0])

# Without min() & sorted()
Min = T[0]
for e in T:
    if e<Min:
        Min=e
print(Min)

''' Sample Output '''
# 1
# 1
# 1