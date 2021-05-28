"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more
"""

# Python Tuple Exercises
# {3} Item deletion in Tuple


T = (4,6,1,7,8,5,3)

index = 3
p1 = T[0 : index]
p2 = T[index+1 : ]
New = p1+p2
print(New)
