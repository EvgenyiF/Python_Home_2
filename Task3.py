# 18. Реализовать алгоритм перемешивания списка

import random
mylist = [1,2,3,4,5,6]
print(mylist)

# Первый способ перемешивания списка
for i in range(len(mylist)-1):
    j = random.randint(0,(len(mylist)-1))
    mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)

# Второй способ перемешивания списка
random.shuffle(mylist)
print(mylist)