tuple=("hi","hello","hola","thing")
print(tuple)
print(type(tuple))
print(tuple[2])
for i in range(len(tuple)):
    print(tuple[i])
for i in tuple:
    print(i)
#unpacking
v1,v2,v3,v4=tuple
print(v1)
print(v2)
print(v3)
print(v4)
#slicing
print(tuple[0:2])
#one item tuple
tup=("bye",)
print(tup)
print(type(tup))
#tuple without brackets
num=6,7,4,2,6,7
print(num)
print(type(num))
num.append(10)