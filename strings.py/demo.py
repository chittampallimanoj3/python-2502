#strings

s1 = 'hello'
# print(s1)

s2 = "hello"
print(s2)

s3 = '''hello'''
print(s3)

s4 = """hello"""
print(s4)

# Above are the single line strings

# Below are the multi line strings
# address = "house no 90
#  zip is 505528
#  city is hyderabd"

address = """house no 90
zip is 505528
city is hyderabad"""
print(address)

# access whole string
text ="python" 
# print(text)

# slicing - slice[start: stop: step]
text = "python"
print(text[:]) #python
print(text[::]) #python
print(text[0:3]) #pyt
print(text[1:3]) #yt
print(text[1:3:1]) #yt
print(text[0:5:2]) #pto


#   0 1 2 3 4 5 (positive indexing) (forward)
#   p y t h o n
#  -6-5-4-3-2-1 (negative indexing) (backward)

print(text[-4:-1]) # tho
print(text[-4:-1:1]) #tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) #ty
print(text[1:4:-1]) #empty

# slicing
print(text[::-1]) #nohtyp