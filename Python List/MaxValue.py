"""
    "Swapnil's Lab" is a YouTube channel            
     based on Programming Experiments.
       Visit my Lab to learn more.
"""

# Python Lists Exercises
# {3} Finding Maximum value in List

# Using max()
List = [12,67,64,31,96,64,12,86,32,98]
print(max(List))

# Without max()
Max = List[0]
for i in List:
    if (i>Max):
        Max = i
print(Max)

'''Sample output'''
# 98
# 98