"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {5} dict comprehension-2

# Example-1
L = [1, 2, 3, 4, 5]
D = { i:i**2 for i in L if i%2==0 }
print(D)

# Example-2
D = { i:i*100 for i in range(1,6) if i>=3}
print(D)

# Example-3
T = tuple('hello')
D = { i:i.upper() for i in T if i=='l' }
print(D)

''' Sample Output '''
# {2: 4, 4: 16}
# {3: 300, 4: 400, 5: 500}
# {'l': 'L'}