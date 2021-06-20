"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {9} Sorting a dictionary by Key

# target dictionary
D = { 'B':3, 'C':1, 'A':2, 'D':4 }

# getting all keys
keyList = D.keys()

# Sorting in ascending order
sortedList = sorted(keyList)

print('ascending:')
for k in sortedList:
    print(k, ':', D[k])

# Sorting in descending order
sortedList = sorted(keyList, reverse=True)

print('\ndescending:')
for k in sortedList:
    print(k, ':', D[k])

# oneliner for ascending
print('\noneliner ascending:')
print(sorted(D.items()))

# oneliner for descending
print('\noneliner descending:')
print(sorted(D.items(), reverse=True))

''' Sample Output '''
# ascending:
# A : 2
# B : 3
# C : 1
# D : 4

# descending:
# D : 4
# C : 1
# B : 3
# A : 2

# oneliner ascending:
# [('A', 2), ('B', 3), ('C', 1), ('D', 4)]

# oneliner descending:
# [('D', 4), ('C', 1), ('B', 3), ('A', 2)]