n = int(input())
people = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    people.append({'age': age, 'name': name})

people.sort(key= lambda x: x['age'])

for i in people:
    print(f"{i['age']} {i['name']}")