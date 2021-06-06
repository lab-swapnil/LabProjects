"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Lists
# {6} Counting a specific value


L = [10,20,30,40,30]
value = 30

# Method-1
print(L.count(value))

# Method-2
count = 0
for e in L:
    if e == value:
        count = count + 1
print(count)

''' Sample Output '''
# 2
# 2