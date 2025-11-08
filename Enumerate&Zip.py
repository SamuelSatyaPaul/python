# fruits = ["mango","apple","banana","dragon fruit"]
# for ind,fruit in enumerate(fruits):
#     print(ind,fruit)

# fruits = ["mango","apple","banana","dragon fruit"]
# for ind,fruit in enumerate(fruits,start=101):
#     print(ind,fruit)


# fruits = ["mango","apple","banana","dragon fruit"]
# # print(list(enumerate(fruits)))
# # print(dict(enumerate(fruits)))

# for ind,fruit in enumerate(fruits,start=101):
#     if fruit == "dragon fruit":
#         print(f" index of {fruit} is {ind}")


# details = ["samuel",21,"rajahmundry","aditya university",7.67]
# print(dict(enumerate(details)))

# sam  = {"name" :"samuel","age" : 21,"college" : "Aditya University","cgpa" : 7.67}
# print(type(sam))
# print(dict(enumerate(sam.items())))



# fruits = ["mango","apple","banana","dragon fruit"]
# fruit = enumerate(fruits)
# print(fruit)


#---------------------------------------------------------------------------------------------------
#zip function


# names = ["Chocolates✨","sleeep","iphone","iwatch🫣","aesthetic"]
# fav = ["Love","daily favourite😌","rich🤧","edolee","nijamee😁"]
# new = ["samuel","satya","paul"]

# print(list(zip(names,fav)))

# for name ,favs in zip(names,fav):
#     print(f"Yes {name} is {favs}")





# names = ["Chocolates✨","sleeep","iphone","iwatch🫣","aesthetic"]
# fav = ["Love","daily favourite😌","rich🤧","edolee","nijamee😁"]
# new = ["samuel","satya","paul","n","😌"]
# print(dict(zip(names,zip(fav,new))))



# names = ["Chocolates✨","sleeep","iphone","iwatch🫣","aesthetic"]
# fav = ["Love","daily favourite😌","rich🤧","edolee","nijamee😁"]
# new = ["samuel","satya","paul","n","😌"]
# result = {}
# for i in range(len(names)):
#     # each key in names → pair of (fav, new)
#     result[names[i]] = (fav[i], new[i])
# print(result)


{'Chocolates✨': ('Love', 'samuel'), 'sleeep': ('daily favourite😌', 'satya'), 'iphone': ('rich🤧', 'paul'), 'iwatch🫣': ('edolee', 'n'), 'aesthetic': ('nijamee😁', '😌')}