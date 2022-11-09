fruits=["apple", "banana", "mango"]
x,y,z =fruits
print(x)
print(y)
print(z)

#scope of a variables
a=10
def func():
 print(a)
func()

b=10
def func():
    a=100
    print("inside value of a is:",a)
    print("outside value of b is:",b)
func()

a=10
b=20
def func():
    a=1000
    global b                            #globally defined
    b=200
    print("inside value of a is:",a "and b is:",b)
func()
print("outside value of a is:",a "and b is:",b)
