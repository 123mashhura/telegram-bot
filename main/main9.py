

thetuple= ("apple", "banana", "cherry")
print(thetuple[1])


thetuple=("apple", "banana", "cherry")
print(thetuple[-1])


x=("apple","banan","cherry")
y=list(x)
y[1]="kivi"
x=tuple(y)
print()


tuple1 = ("appel", "banana" , "cherry")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(y)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)