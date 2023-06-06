for enteros in range (0,151):
    print(enteros)

print ("-------------")

for x in range (5,1001,1):
    if x % 5 == 0:
        print (x)


print ("-------------")


for divisible in range(1, 101, 1):
    if divisible % 10 == 0:
        print( "Coding Dojo" )
    elif divisible % 5 == 0:
        print( "Coding" )


print ("-------------")


sum = 0
for i in range(0, 500001, 1):
    if i % 2 == 1:
        sum += i
print(sum)


print ("-------------")

for regr in range(2018, -1, -4):
    print(regr)


print ("-----------------")

lowNum = 5
highNum = 24
mult = 5

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)