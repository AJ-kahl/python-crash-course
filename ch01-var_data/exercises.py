
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