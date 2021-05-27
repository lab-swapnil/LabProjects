"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.Visit my Lab to 
    learn more.
"""

# Python Tuple Exercises
# {2} Item insertion in Tuple


T = (4,6,1,7,8,5,3)
item = 0,
index = 3
p1 = T[0:index]
p2 = T[index: ]
New = p1+item+p2
print(New)

''' Sample output '''
# (4, 6, 1, 0, 7, 8, 5, 3)