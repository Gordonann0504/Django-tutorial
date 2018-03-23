print('this line will be printed')
x=1
if x == 1:
     print('x is 1')

print('Goodbye,World')

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring2 = "Don't worry about apostrophes"
print(mystring2)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)

#fixxed this
one = 1
two = 2
hello = "hello"

three = one + two
print(str(three) + str(hello))

#original
# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# change this code
mystring = hello
myfloat = float(10)
myint = int(20)

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if myfloat == 10.0:
    print("Float: %f" % myfloat)
if myint == 20:
    print("Integer: %d" % myint)