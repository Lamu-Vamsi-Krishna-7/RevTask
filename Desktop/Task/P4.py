
list = [1, 2, 3, 2]
print("List:", list)
list.append(4)
print(list)
tuple = (1, 2, 3, 2)
print("Tuple:",tuple)
try:
    tuple[0] = 100
except Exception as e:
    print(e)

set = {1, 2, 3, 2}
print("Set",set)
set.add(4)
print(set)

dict = {"a": 1, "b": 2, "a": 3} 
print("Dictionary",dict)
dict["c"] = 4
print(dict)


