"""
    "Swapnil's Lab" is a YouTube channel            
    based on Programming Experiments.
       Visit my Lab to learn more.
"""

# Python String Exercises
# {3} Counting Specific Characters in String


str="Don't 4get 2 Subscribe."
u=l=d=s=0
for c in str:
    if c.isupper():
        u += 1
    elif c.islower():
        l += 1
    elif c.isdigit():
        d += 1
    else:
        s += 1
print(str)
print('upper :', u)
print('lower:', l)
print('digits'' :', d)
print('special :', s)

'''Sample Output'''
# Don't 4get 2 Subscribe.
# upper : 2
# lower: 14
# digits : 2
# special : 5