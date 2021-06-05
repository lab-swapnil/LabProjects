"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Strings
# {8} Finding longest word


str= 'hello dear friends'
longest = ''
length = 0
for i in str.split():
    if len(i) > length:
        longest = i
        length = len(longest)

print(longest, length)

''' Sample Output '''
# friends 7