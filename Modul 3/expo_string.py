name = 'samim\'s khan' #escape
name2 = "kona shinha"
name3 = """ 
homayon
karim
"""
print(name3)

for char in name2:
    print(char)

print(name[2])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# name2[0] = 'r'   dont do that
if 'kona' in name2:
    print('exists')

print(name2.upper())