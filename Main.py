message = 'hello world'
print(message)

message = "hello python world"
print(message.upper())

age = '23'
# print('Happy'+ " " + str(age) +'rd Birthday')

print(age)

print(int(age) + 10)

name_list = ['Emma', 'Anne', 1997]
popped_name = name_list.pop()
name_list.sort()
print(name_list)
print(popped_name)

for i in name_list:
 print(i)

a = list(range(2,11,2))
print(a)

w=[]
for num in a:
 w.append(num**2)
 print(w)

print(w)

square = [value+1 for value in range(1,11)]
print(len(square))
print(square[-3:])

dimension =(200,20)
print(dimension[0])
print(dimension[1])

dimension = (300, 10, 30)
print(dimension[2])

if square[1] == 8 or square[2] >= 4:
 print('Number is 2, followed by 3')

print(14 not in square)

car = 'mazda'

print("Is " + str(car=='mazda') + " I predict true")

emma = {'color': 'blue', 'size': 20}
emma['x_position'] = 23
print(emma)

array = [1,2,3,4]
reverse_array = []

for val in array:
 reverse_array.insert(0, val)
 
print(reverse_array)

user_0 = {
 'first': 'emma',
 'last': 'okorie',
 'score': 'emma'
}

for key,value in user_0.items():
 print('\n key: ' + key)
 print('\n value: ' + value)

print(set(user_0.values()))

alien = []

for chr in range(30):
 new_obj = {'color': 'green', 'speed': 'slow', 'points': 10,}
 alien.append(new_obj)

for aliens in alien[:3]:
 if aliens['color'] == 'green':
  aliens['color'] = 'yellow'
  aliens['speed'] = 'medium'
  aliens['points'] = 20
 elif aliens['color'] == 'yellow':
  aliens['color'] = 'red'
  aliens['speed'] = 'fast'
  aliens['points'] = 30

for fr in alien[:5]:
 print(fr)

message = ""
while message != 'quit':
 message = input('Give me your height in ft:  ')
 
 if message != 'quit':
  print(message)
# message = int(float(message))

# if message >= 6:
#  print('You are tall o boss')
# elif message < 6:
#  print('see mini traffic light')

