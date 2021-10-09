data = "Python rules!"

# Assume the variable data refers tot he string "Python rules!". USe a string methond to perform the following task
print(data.split())
print(data.upper())
print(data.find("rules"))
print(data.replace('!', '?'))

# Using the value of data form Exercise 1, write the values of the following expressions:
print(data.endswith("i"))
print(" totally ".join(data.split()))
