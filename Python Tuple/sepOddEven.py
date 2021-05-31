"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Tuples
# {4} Separating Odd_Even values


T = (11, 12, 13, 14)
Even = []
Odd = []
for e in T:
    if e%2==0:
        Even.append(e)
    else:
        Odd.append(e)

print(tuple(Even))
print(tuple(Odd))

''' Sample Output '''
# (12, 14)
# (11, 13)