##Robert Fernandez
##Complete
##This program will count the letters and concatenate them together. 

first = input("Enter your first name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name: ")

full_name = first + " " + middle + " " + last

a_count = 0
e_count = 0
s_count = 0

for char in full_name.lower():
    if char == 'a':
        a_count += 1
    elif char == 'e':
        e_count += 1
    elif char == 's':
        s_count += 1


print(f'a: {a_count}')
print(f'e: {e_count}')
print(f's: {s_count}')
