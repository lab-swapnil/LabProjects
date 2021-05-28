"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""
# Python Strings Exercises
# {4} Reverse of String

string = "hello dear"

# Using slice
print( string[::-1] )

# Using index
i = len(string)-1
while i>=0:
    c = string[i]
    print(c, end='')
    i -= 1

print()

# Using reversed()
r = reversed(string)
for c in r:
    print(c, end='')

''' Sample Output '''
# raed olleh
# raed olleh
# raed olleh