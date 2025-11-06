# a = 28
# b = 26

# if a > b:
#     print("Greatest")
# else:
#     print("smallest")
# result = "greatest" if a > b else "samllest"
# print(result)

##MajororMinor
# def age(num):
#     return "Major" if num>18 else "Minor"

# print(age(28))


# ##EvenorOdd
# def Check(num):
#     return "Even" if num%2==0 else "Odd"
# print(Check(27))


# ##UsingLoops
# list1 = [1,2,3,4,5,6,7,8,9,0]
# evenodd = ["Even" if n%2 ==0 else "Odd" for n in list1 ]
# print(evenodd)


# l2 = ["samuel","satya","paul"]
# # emp = ['Greater than 5 words' if len(n)>=5 else "Not greater than 5" for n in l2]
# emp = [n for n in l2 if len(n) >= 5]
# print(emp)


# num = int(input())
# result = "Positive" if num > 0 else "Negative" if num < 0 else "Equal"


# marks=int(input()) 
# grade =['A grade' if marks>90 else 'B grade' if marks> 80 else 'C grade' if marks>70 else "Fail"]
# print(grade)


def Morning():
    return "Good Morning"
def Afternoon():
    return "Good Afternoon"
def Evening():
    return "Good Evening"
def Night():
    return "Good Night"
time = int(input("Ent Time : "))

greetings = Morning() if time >= 1 and time <= 11 else Afternoon() if time >= 12 and time <= 15 else Evening() if time >= 16 and time <= 20 else Night()

print(greetings)
