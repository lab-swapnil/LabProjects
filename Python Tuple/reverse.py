"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""
# Python Tuples
# {7} Reverse the tuple

T = (11, 12, 13, 14, 15)

# Method-1
print( T[ : : -1] )

# Method-2
for i in range(len(T)-1, -1, -1):
    print( T[i], end=' ' )

print()

# Method-3
rev = reversed( T )
for e in rev:
    print(e, end=' ')

''' Sample Output '''
# (15, 14, 13, 12, 11)
# 15 14 13 12 11 
# 15 14 13 12 11