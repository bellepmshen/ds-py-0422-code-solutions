# exercise 1-4:

person = {
  "first_name": "Belle",
  "last_name": "Shen",
  "hobby": "reading books"
}
print(person)

# exercise 5-9:

first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(f"first name: {first_name}, middle name: {middle_name},last name: {last_name}")

# exercise 10-15:

person["job"] = "DS TA"
print(person["job"])
person["hobby"] = "baking"
print(person["hobby"])

# exercise 16-18:

person.pop("last_name")
print(person)
