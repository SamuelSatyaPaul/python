#Without Lambda
# def add(a,b):
#     return a+b

# print(add(3,4))


#With lambda
# add_num  = lambda a,b: a+b
# print(add_num(3,4))

# num = lambda a:a*a
# print(num(7))


# celTofar = lambda c: c*(9/5)+32
# print(celTofar(37))


# evenodd = lambda a: "Even" if  a%2 ==0 else "Odd"
# print(evenodd(5))


# num = lambda a,b: "Greaterst" if a > b else "Smallest"
# print(num(4,6))


# names = ["samuel","satya","paul"]
# names.sort(key= lambda name:(len(name)))
# print(names)


# num = [111,92,3,4,55,66,777,8888]
# num.sort(key=lambda nums:nums)
# print(num)


##Map

# list1 = [1,2,3,4,5]
# sqlist = list(map(lambda num: num **2,list1))
# print(sqlist)



##Filter

# list2= [1,2,3,4,5,6,7,8,9,10]
# filterfunc = list(filter(lambda num: num %2==0 ,list2))
# print(filterfunc)


##Reduce
# from functools import reduce

# list3 = [1,2,3,4,5,6,7,8,9]
# reducefunc = reduce(lambda num1,num2 : num1 - num2,list3)
# print(reducefunc)




names = ["Ajith Kumar", "Vishwa Teja", "Naga swaroop", "Samuel Satya Paul", "Vishnu vardhan"]
list1 = []

for name in names:
    parts = name.split()          # Split the full name into words
    initials = ""                 # Initialize empty string for initials
    for p in parts:
        initials += p[0]          # Take the first letter as it is (no case change)
    list1.append(initials)

print(list1)
