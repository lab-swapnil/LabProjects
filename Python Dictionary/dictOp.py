"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""
# Python Dictionary
# {7} Operations on Values

D = { 'a':10, 'b':15, 'c':20 }

# create a view object to view dict values
vo = D.values()

# list of values
print('dict_Values : ', list(vo) )

# sum of values
print('Sum : ', sum(vo) )

# minimum value
print('Min : ', min(vo) )

# maximum value
print('Max : ', max(vo) )

# number of values
print('Len : ', len(vo) )

# average of values
print('Avg : ', sum(vo) / len(vo) )

''' Sample Output '''
# dict_Values :  [10, 15, 20]
# Sum :  45
# Min :  10
# Max :  20
# Len :  3
# Avg :  15.0