s="Welcome To The Jungle"
print("length of",s,"is:",len(s))

print(s.lower())   # prints all characters in lower case
print(s.upper())   # prints all characters in upper case

print(s.swapcase())  # prints all characters in swap
print(s.capitalize())  # prints all characters in capitalized
print(s.title())
print(s.lstrip("Welcome"))  #to remove from left side


print("minimum=",min(s))
print("minimum=",max(s))

print(s.count('o',0,len(s)))
print(s.index('e',0,len(s)))
print(s.find('o',0,len(s)))

s='-'
sequence=("hello", "world", "!")
print(s.join(sequence))

s="Welcome To The Jungle"
print(s.replace("W","J"))
txt="welcome to the jungle"
x=txt.split()
print(x)
a="hello world!"
print(a.split(","))
c=a+txt
print(c)
print(a+" "+txt)
y=45
print(a.format(y))
