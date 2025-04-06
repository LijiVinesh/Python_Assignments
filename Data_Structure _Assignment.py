c=[1,6,9,4,55]
print(c)
c.append(88)
c.append(23)
c.append(77)
print(c)

for list_item in c:
    print(list_item)
pupil_info = {
        'name': 'John',
        'age': 25,
        'address': 'New York'
    }
print(pupil_info)
pupil_info['phone']=1234567890
print(pupil_info)

Sample_set= {1, 2, 3, 4, 5}
print(Sample_set)
Sample_set.add(6)
print("New_Set:",Sample_set)
Sample_set.remove(3)
print("3 Removed Set:",Sample_set)


Sample_tuple = (1, 2, 3, 4, 5)
print("Tuple:",Sample_tuple)
print("Length of tuple:",len(Sample_tuple))