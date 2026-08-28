def multiplication_table(number):
    for i in range(1,11,1):
        print(f"{number}*{i}={number*i}")
name=input("Enter your name:")
age=int(input("Enter your age:"))
nbr=int(input("Enter any number:"))
print(f"Name: {name}\nYou are {age} year old")
print(f"Multiplication table of {nbr}")
multiplication_table(nbr)


