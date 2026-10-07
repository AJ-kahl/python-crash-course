'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

'''
motorcycles = ['honda', 'yamaha', 'suzuki']
'''
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('103')
print(motorcycles)

motorcycles = []

motorcycles.append('ducati')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0 ,'honda')
print(motorcycles)

del motorcycles[3]
print(motorcycles)


last_owened = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owened.title()}.")

motorcycles.remove('honda')
print(motorcycles)


too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
'''

motorcycles.sort(reverse=True)
print(motorcycles)

print("\nHere is the sorted list:")
print(sorted(motorcycles))