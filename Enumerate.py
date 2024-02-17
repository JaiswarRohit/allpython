# Enumerate in List
'''
l1 = ["apple", "banana", "cherry", "date"]
for index, item in enumerate(l1):
    print(f'Index: {index}, item: {item}')

l1 = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "coconut"}

for index, (key, value) in enumerate(l1()):
    print(f'Index :{index}, key: {key}, value: {value}')
    '''

my_dict = {'a': 1, 'b': 2, 'c': 3}

for index, (key, value) in enumerate(my_dict.items()):
    print(f'Index: {index}, Key: {key}, Value: {value}')





