"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Lists
# {5} Searching a value

L = [10,20,30,40,50]
search = 30

# Method-1
if L.count(search)>0:
    print('found at index',L.index(search))
else:
    print('not found')

# Method-2
for i in range(len(L)):
    if L[i]==search:
        print('found at index',i)
        break
    
''' Sample Output '''
# found at index 2
# found at index 2