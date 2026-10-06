''''
name = "john doe"
msg = f"Hello {name.title()}, would you like to learn some Python today?"
print(msg)

name = 'John doe'
print(name.upper())
print(name.lower())
print(name.title())

quote = '\tAlbert Einstein once said, "A person who never made a mistake never \n\ttried anything new."'
print(quote)\

name_person = "\tjohn doe\n"
print(name_person)
print(name_person.lstrip())
print(name_person.rstrip())
print(name_person.strip())


filename = "python_notes.txt"
print(f"File name without file extension is : {filename.removesuffix(".txt")}")


print("Addition that results in the number 8: 5 + 3 =", 5 + 3)
print("Subtraction that results in the number 8: 11 - 3 =", 11 - 3)
print("Multiplication that results in the number 8: 4 * 2 =", 4 * 2)
print("Division that results in the number 8: 24 / 3 =", 24 / 3)

fav_num = 3
print(f"My favorite number is : {fav_num}")
'''