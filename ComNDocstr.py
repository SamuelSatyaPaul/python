# list1 = [1,2,3,4,5,6,7,8,9,10]
# def sumoflists(seq):
#     sum = 0
#     for num in seq:
#         sum += num
#     return(sum)

# print(sumoflists(list1))


# def prime(num):
#     for i in range(2,(num//2)+1):
#         if num%i == 0:

#             print("Not Prime")
#             break
#     else:
#         print("Pirme")
# prime(7)



##String-Revarsal

# str1 = "Samuel"
# rev = ""
# for char in str1:
#     rev = char+rev
# print(rev)



names = ["samuel","satya","paul"]
reversed_names = []

for name in names:
    rev = ''  # start empty for each new name
    for char in name:
        rev = char + rev  # place each new char before the existing text
    reversed_names.append(rev)  # store the reversed name

print(reversed_names)


##Using ::-1
names = ["samuel", "satya", "paul"]
rev_names = []

for name in names:
    rev = name[::-1]   # reverse each string
    rev_names.append(rev)

print(rev_names)



##Perfect-Squares

def PerSq(num) :
    ptsq=(num) ** 0.5
    if ptsq == int(ptsq):
        print(f'{num} is a perfect square')
    else:
        print(f'{num} is not a perfect square')

PerSq(3)



def perSq(num) :
    for num1 in range(1,num):
        if num1*num1 == num:
            print('It is a perfect squaare')
            break
    else:
        print('not perfect square')

perSq (9)