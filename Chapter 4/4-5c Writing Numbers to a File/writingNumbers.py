import random
f = open("./Chapter 4/4-5c Writing Numbers to a File/integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close()
