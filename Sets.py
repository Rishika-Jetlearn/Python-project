num=[4,2,8,5,3,1,1,4,3]
print(num)
print(type(num))
#converting list to set
num_set=set(num)
print(num_set)
print(type(num_set))
if 4 in num_set:
    print("Yes")
#add item
num_set.add(10)
print(num_set)
#remove item
num_set.remove(10)
print(num_set)

fruits={"strawberry","apple","banana","lemon","mango","orange"}
citrusfruits={"orange","lemon","lime","grapefruit"}
#union
print(fruits.union(citrusfruits))
print(fruits | citrusfruits)
#intersection
print(fruits.intersection(citrusfruits))
print(fruits & citrusfruits)
#difference
print(fruits.difference(citrusfruits))
print(fruits - citrusfruits)
print(citrusfruits - fruits)
#symmetric 
print(fruits.symmetric_difference(citrusfruits))
print(fruits ^ citrusfruits)