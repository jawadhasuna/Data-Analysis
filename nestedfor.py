for i in range (13):
  print(i)
for i in range(3,13,2):
  print(i)
days =['monday','tuesday','wednesday','thursday','friday']
for day in days:
  if(day=='wednesday'):
    print("wednesday is my love")
    continue
  print(day)
fruits=["banana","apple","kiwi"]
for day in days:
  for fruit in fruits:
    print(day,fruits)
persons=[{'name':'jawad','sex':'male','age':21},{'name':'ibrahim','sex':'male','age':32}]
for person in persons:
  for value in person.values():
    print(value)

