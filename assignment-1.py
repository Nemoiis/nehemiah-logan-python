#Section 1
name = "Nehemiah"
age = 20
height = 5.11
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name = input("Name? ")
birth_year = input("Year were you born? ")

birth_year = int(birth_year)
age = 2026 - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")

#section 3
numOne = float(input("Enter first number: "))
numTwo = float(input("Enter second number: "))

print(f"{numOne} x {numTwo} = {numOne * numTwo}")

#Section 4
item = "Python Textbook"
price = 19.99
quantity = 3
total = price * quantity

print(f"""
=========================
         Receipt
=========================
Item: {item}
Price: ${price}
Quantity: {quantity}
-------------------------
Total: ${total}
=========================
""")

#Section 5
name = input("Enter Name: ")
city = input("Enter City")
state = input("Enter State (abbreviated): ")
hobby = input("Enter Hobby: ")
funfact = input("Enter Fun Fact: ")
birth_year = input("Enter Year of Birth: ")
age = 2026 - int(birth_year)

print(f"""
╔══════════════════════════════╗
         PROFILE:{name}
╚══════════════════════════════╝
City:       {city}, {state}
Hobby:      {hobby}
Fun fact:   {funfact}
Age:        {age}
""")
