
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait for the next tricks, {magician.title()}.\n")

print("Thank you, everyone. That was a great performence")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favortie foods are:")
print(friend_foods)


dimensions = (200, 50)
print(dimensions)

dimensions = (400, 20, 40)
print(dimensions)