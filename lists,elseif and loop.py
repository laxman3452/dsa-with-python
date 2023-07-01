# x = input("What is your name \t")
# y = int(input("Input a number"))
# print("Hello " + x+" !")
# print("Your number is " + str(y) + "!")
# print(y*6)


# immutable and mutable
# x=1
# y=x
# z=1
# a=0
# a = a+1

# id(x) all will point to same address.
# strings are immutable but lists is mutable.
# like when changing string value it's id will change but on lists it's id i.e memory reference doesn't change on changing it's item. 
# lists
# cars = [1,2,4,4,"BMW","supra"]
# cars[0]
# type(cars[1])
# cars.append([5,6])
# cars.append(1)
# cars.pop()
# cars.pop(1)
# # max(cars)
# # min(cars)
# print(cars)

# bikes =["bmw","ninja h2r"]

# if ("bmw" in bikes) and ("ninja h2r" in bikes):
#     print("nice")
# elif 1 in cars:
#     print("nice second")
# else:
#     print("nice third")


bikes =["bmw","ninja h2r"]

for bike in bikes:
    print(bike)

numbers = [1,2,3,4,5]
i=0
sum=0
while(i<len(numbers)-1):
    if (numbers[i]%2 == 0):
        sum+=numbers[i]
    i+=1

print(sum)

# break stops all the remaining iteration
# continue makes the ongoing iteration finish and move to the next iteration.

# this is just a blueprint.
