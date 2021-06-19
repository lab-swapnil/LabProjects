"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {8} Frequency of Characters

# target string
string = "hello dear friends"
print(string)

# dictionary to store frequency
D = {}

# loop over string
for char in string:

    # checks if char is not a key in dict D
    if char not in D:
        
       # add char as key with value 1 in dict D
        D[char] = 1
        
    else:
    # if char is already a key in dict D

        # increase its value by 1
        D[char] += 1

# print frequency of characters
for k,v in D.items():
    print(k, ':',v)

''' Sample Output '''
# hello dear friends
# h : 1
# e : 3
# l : 2
# o : 1
#   : 2
# d : 2
# a : 1
# r : 2
# f : 1
# i : 1
# n : 1
# s : 1