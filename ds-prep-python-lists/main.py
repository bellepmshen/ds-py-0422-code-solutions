# exercise 1-4:
ages = [29, 19, 17, 26, 32, 16, 21]
print(f"ages: {ages}")

# exercise 5-11:
print(f"The 5th element in the ages list: {ages[4]}")
print(f"The 2nd-to-last element in the ages list: {ages[-2]}")
print(f"The 3rd to 6th elements in the ages list: {ages[2:6]}")
print(f"The first 4 elements in the ages list: {ages[:4]}")

print(f"Is 17 stored in the ages list? {17 in ages}")
print(f"Is 42 stored in the ages list? {42 in ages}")

# exercise 12-15:
ages[2] = 18
print(ages)
temp = ages[4]
ages[4] = ages[3]
ages[3] = temp
print(ages)

# exercise 16-20:
ages.append(45)
ages.insert(0, 32)
ages.insert(4, 37)
print(ages)

# exercise 21-:
ages.pop()
ages.pop(2)
print(ages)
