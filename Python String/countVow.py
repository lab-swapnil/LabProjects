"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Strings
# {7} Counting Vowels




str = 'Hello dear friends'
count = 0
for c in str:
    if c in 'aeiouAEIOU':
        count += 1

print(count)

''' Sample Output'''
# 6