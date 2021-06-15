"""
    "Swapnil's Lab" is a YouTube         
    channel based on Programming 
    Experiments.
    Visit my Lab to learn more.
"""

# Python Dictionary
# {4} dict comprehension

# Example-1
L = [1, 2, 3, 4, 5]
D = { i:i**2 for i in L }
print(D)

# Example-2
D = { i:i*100 for i in range(1,6) }
print(D)

# Example-3
T = tuple('hello')
D = { i:i.upper() for i in T }
print(D)

''' Sample Output '''
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
# {'h': 'H', 'e': 'E', 'l': 'L', 'o': 'O'}