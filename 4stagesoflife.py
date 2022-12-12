#Chapter 4 - Exercise 4
#A program to determine a person's stage of life
age = int(input("How old is the person? ")) #asking the age of the person
if age < 2: #If the person's age is less than 2, it's a baby
    print("This person is a baby.")
elif age >= 2 and age < 4: #If the person's age is 2-3, it's a toddler
    print("This person is a toddler.")
elif age >= 4 and age < 13: #If the person's age is 4-12, it's a kid
    print("This person is a kid.")
elif age >= 13 and age < 20: #If the person's age is 13-19, it's a teenager
    print("This person is a teenager.")
elif age >= 20 and age < 65: #If the person's age is 20-64, it's an adult
    print("This person is an adult.")
else: #If the person's age 65+, it's an elder
    print("This person is an elder.")