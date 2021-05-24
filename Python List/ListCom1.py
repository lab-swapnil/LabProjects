# list comprehension in Python

# Syntax-1
# List = [ exp for var in sequence ]

# Example-1
l = [a for a in range(5)]
print(l)

# Example-2
l = [a*10 for a in range(5)]
print(l)

# Example-3
l = [a*2 for a in 'hello']
print(l)

# Example-4
l = [a**a for a in (1, 2, 3)]
print(l)

# Example-5
l = [a-1 for a in (1, 3, 5)]
print(l)