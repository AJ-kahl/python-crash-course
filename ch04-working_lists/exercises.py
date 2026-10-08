pizzas = ['pepperoni', 'hawaiian', 'veggie']

for pizza in pizzas:
    print(f'Pizza kind : {pizza.title()}.')
    print(f'I like {pizza.title()} pizza.')

for pizza in pizzas:
    print(f'I really love {pizza.title()} Pizza.')

print("\nI love pizza!")

animals = ['tiger', 'lion', 'cheetah']

for animal in animals:
    print(animal.title())
    print(f'A {animal.title()} would make a great pet.')

print("\nThose animals belong in the same familly, Felidae.")


for num in range(1, 21):
    print(num)


numbers = list(range(1, 1_000_001))


for num in numbers:
    print(num)


print(min(numbers))
print(max(numbers))
print(sum(numbers))



odd_nums = list(range(1,20,2))
for num in odd_nums:
    print(num)

threes = list(range(3,31,3))
for num in threes:
    print(num)

numbers = []
for num in range(1,11):
    value = num**3
    numbers.append(value)
    print(value)

cubes = [num**3 for num in range(1,11)]
print(cubes)


my_foods = ['falafel', 'carrot cake', 'pepperoni', 'hawaiian']
print('The first three items in the list are:')
for food in my_foods[:3]:
    print(food.title())

print('The last three items in the list are:')
for food in my_foods[1:]:
    print(food.title())

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append('cheese')
friend_pizzas.append('fungi')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )
for item in menu_items:
    print(f'We offer : {item.title()}')

