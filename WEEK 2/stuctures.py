my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list[1] = 15
dum = [50,60,70]
my_list.extend(dum)
my_list.remove(70)
my_list.sort()
print(my_list.index(30))


