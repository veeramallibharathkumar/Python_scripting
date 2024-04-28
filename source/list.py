""" list are used to store the series of items in a particular order """
''' list are mutable and they are accessed by indexing '''
''' list are defined as square brackets and comma separated  and it is named as pulars'''
''' pairs = ['a','b','c','d','e','f','g','h','i','j'] '''

users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

''' Adding elements to a list '''
''' append will only add one element to the end of the list'''
''' extend method will extend the list '''
''' additional operator also does the same functionality like extend '''
''' insert method will insert an element at the specified position '''
users.append('bharath')
users.extend([1, 2, 3, 5])
users.insert(7, 'bharath')

# print("These are the items in the list: ", users)

''' indexing method will return the index of the element '''
a = users[6]
# print('This is the 6th index in the list : ', a)

''' modifying the list '''

users[2] = 'bharath'
# print(users)

""" removing the element from the list """
""" pop removes the items with specified index from the list """

users.remove('bharath')
# print(users)

users.pop(1)
# print(users)

del users[6]

# print(users)

''' sorting the list '''
'''reverse the list method will reverse the order of the elements/items in the list if it is reverse = true it will 
has permanent impact'''
sort_lists = [1, 2, 4, 5, 3, 4, 3, 2, 1]
sort_lists.sort()
# print(sort_lists)
# sort_lists.sort(reverse=True)
# print("This is the reverse order", sort_lists)

sort_lists.reverse()
# print(sort_lists)

''' Loops with the list '''
''' for loop '''
''' when iterating the items in the list  the python will store the temporary variable in the name of the 
variable you have given '''

for_users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for user in for_users:
# print("Hey this is the looping, " + user + " , lets go to next item in the list")

''' length method will return the length of the list '''

# len(for_users)

# print(len(for_users))

''' Range() function will return the range of the list with default value as zero and one minus the upper limit value '''

# for number in range(1, 20):
#     print(number)

''' to store this elements within a list '''

test = list(range(1, 20))

# print(test)

''' statistics min,max,sum'''

print("This is the minimum number in the list :", min(test))

print("This is the maximum number in the list : ", max(test))

print("This is the total sum from the list : ", sum(test))

''' slicing list '''
''' copying of an list is done with slicing without updating the first and last position '''

middle_slice = test[1:3]
copy = test[:]
print(copy)
print(middle_slice)

''' list comprehenssion are used instead reduce the multiple code and it is defined as experssion and loop'''

emptys = []

for empty in range(1, 1000):
    emptys.append(empty)

print(emptys)

emptys = [empty for empty in range(1, 1000)]
print(emptys)
