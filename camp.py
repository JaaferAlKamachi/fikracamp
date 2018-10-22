#Fikracamp
# I'm using slicing method to solve this question here is how i did it :

list1 = [1,2,3] 
list2 = ["a","b","c"] 
result = [None]*(len(list1)+len(list2)) # 1. Make a list of the correct length. 
result[::2] = list1 # 2. Populated the even indexes with the contents of list1.
result[1::2] = list2 # 3. Populate the odd indexes with the contents of list2.
result
[1, 'a', 2, 'b', 3, 'c']