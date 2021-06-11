"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Tuples
# {8} Sorting tuple values

# Method-1
T = (30, 10, 40, 20)
L = list(T)
L.sort()
print(tuple(L))

# Method-2
print(tuple(sorted(T)))

#Method-3
L = list(T)
for i in range(0, len(T)-1):
    for j in range(i+1, len(T)):
        if L[i] > L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
print(tuple(L))

''' Sample Output'''
# (10, 20, 30, 40)
# (10, 20, 30, 40)
# (10, 20, 30, 40)