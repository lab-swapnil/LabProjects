# list comprehension in Python

# Syntax-2
# L= [exp for var in sequence if cond]

# Example-1
l= [a for a in range(5) if a>2]
print(l)

# Example-2
l= [a*10 for a in range(5) if a>2]
print(l)

# Example-3
l=[a for a in 'HeLlO' if a.isupper()]
print(l)

# Example-4
l=[a for a in (1,2,3,4,5) if not a%2 ]
print(l)

# Example-5
l= [a-1 for a in (1, 3, 5) if True]
print(l)