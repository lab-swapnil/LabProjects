"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Lists
# {4} Removing negative values


list = [11, -12, 13, -14]
i = 0
for e in range(len(list)):
    if list[i] < 0:
        del list[i]
    else:
        i=i+1

print(list)

''' Sample Output '''
# [11, 13]