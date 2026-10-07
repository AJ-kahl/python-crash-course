
names = ['aj', 'anes', 'fateh', 'alaa']

print(names[0])
print(names[1])
print(names[2])
print(names[3])


msg = f"Hello, {names[0].title()}!"
print(msg)

msg = f"Hello, {names[1].title()}!"
print(msg)

msg = f"Hello, {names[2].title()}!"
print(msg)


guest_list = ['nikola tesla', 'max verstappen', 'dad']

msg = f"Mr {guest_list[0].title()}, you are invited for Dinner."
print(msg)

msg = f"Mr {guest_list[1].title()}, you are invited for Dinner."
print(msg)

msg= f"Mr {guest_list[2].title()}, you are invited for Dinner\n\t Love You <3."
print(msg)

print(f"Mr {guest_list[0].title()} will not be able to attend the dinner party.")
guest_list[0] = 'guido van rossum'

name = guest_list[0].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[1].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[2].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")

print("Aight guys we found a bigger table, I guess we gonna invite more people")
guest_list.insert(0, 'Jack')
guest_list.insert(2, 'lynn')
guest_list.append('fateh')

name = guest_list[0].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[1].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[2].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[3].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[4].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[5].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
print(guest_list)
print(f"The number of people visiting is : {len(guest_list)}")

print("Well sorry guys, the table wouldn't arrive yet gonna invite only 2 persons")
deleted_guest = guest_list.pop(-3)
print(f"Sorry Mr {deleted_guest.title()} you are not invited")
deleted_guest = guest_list.pop(-3)
print(f"Sorry Mr {deleted_guest.title()} you are not invited")
deleted_guest = guest_list.pop(-3)
print(f"Sorry Mr {deleted_guest.title()} you are not invited")
deleted_guest = guest_list.pop(0)
print(f"Sorry Mr {deleted_guest.title()} you are not invited")

name = guest_list[0].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
name = guest_list[1].title()
print(f"Mr {name}, you are invited for AJ's Dinner.")
print(guest_list)

del guest_list[0:2]
print(guest_list)


locations = ['london', 'tokyo', 'makka', 'sf']

print("Original order:")
print(locations)

print("\nAlphabetical order:")
print(sorted(locations))
print("\nOriginal order:")
print(locations)

print("\nReverse-alphabetical order:")
print(sorted(locations, reverse=True))
print("\nOriginal order:")
print(locations)

print("\nReversing the list:")
locations.reverse()
print(locations)
print("\nOriginal order:")
locations.reverse()
print(locations)

locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
