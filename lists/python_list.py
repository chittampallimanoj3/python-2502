# numbers =[10,0,-1,7]
# print(numbers)

# names = ['manoj','sai','ram']
# print(names)
# mix_list = [1,'manoj',true,10.10]
# print(mix_list)

#List slicing

# numbers =[10,0,-1,7]
# print(numbers[0:4])
# print(numbers[:])

# #string slicing

# numbers =[10,0,-1,7]
# print(numbers[1:3])

# numbers=[10,0,-1,7,8,10,-67]
# print(numbers[1:4])
# print(numbers[:5])

#Extended slicing

numbers=[10,0,-1,7,8,10,-67]
print(numbers[0:5:1])
print(numbers[0:5:2])
print(numbers[0:5:3])
print(numbers[0::3])

#if we want to sort the list

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))

#Append function

numbers.append(45)
print(numbers)

#insert function

numbers.insert(2,45)
print(numbers)

#extend function

numbers.extend([46,47,48,78,79])
print(numbers)

#To replace
numbers[1]=45
print(numbers)

#pop method

numbers.pop()
print(numbers)