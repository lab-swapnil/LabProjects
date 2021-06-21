"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {10} Sorting a dictionary by Value

# target dictionary
D = { 'B':3, 'C':1, 'A':2, 'D':4 }

# getting all items
keyList = D.items()

# function that returns comparison key
def getKey( x ):
    return x[1]

# Sorting in ascending order
sortedList = sorted(keyList, key=getKey)

print('ascending:')
print(sortedList)

# Sorting in descending order
print('\ndescending:')
print(sorted(keyList, key=getKey,reverse=True))

# oneliner for ascending
print('\noneliner ascending:')
print(sorted(D.items(),key=getKey))

# oneliner for descending
print('\noneliner descending:')
print(sorted(D.items(),key=getKey,reverse=True))

# oneliner using lambda
print('\noneliner using lambda:')
print(sorted(D.items(), key=lambda x:x[1]))

''' Sample Output '''
# ascending:
# [('C', 1), ('A', 2), ('B', 3), ('D', 4)]

# descending:
# [('D', 4), ('B', 3), ('A', 2), ('C', 1)]

# oneliner ascending:
# [('C', 1), ('A', 2), ('B', 3), ('D', 4)]

# oneliner descending:
# [('D', 4), ('B', 3), ('A', 2), ('C', 1)]

# oneliner using lambda:
# [('C', 1), ('A', 2), ('B', 3), ('D', 4)]