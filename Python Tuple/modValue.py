"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Tuples
# {5} Modifying Tuple Elements


T = (11,12,13,14,15)
index = 2
value = 31,
p1 = T[ : index]
p2 = T[index+1 : ]

New = p1 + value + p2

print(T)
print(New)

''' Sample Output '''
# (11, 12, 13, 14, 15)
# (11, 12, 31, 14, 15)