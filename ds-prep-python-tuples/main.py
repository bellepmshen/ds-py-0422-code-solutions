# exercise 1-4:

passenger = (12, True, "Bonnell, Miss. Elizabeth", "female", 58)
print(f"passenger: {passenger}")

# exercise 5-8:

name = passenger[2]
age = passenger[-1]
print(f"name: {name}, age: {age}")

# exercise 9-11:
survived_and_name = passenger[1:3]
gender_and_age = passenger[-2:]
print(survived_and_name, gender_and_age)

# exercise 12-14:

is_female = "female" in passenger
is_male = "male" in passenger
print(f"is_female: {is_female}, is_male: {is_male}")

# exercise 15-:

def get_survival_info(passenger):
  """
  This function is for unpacking a tuple and packing a new tuple in return.

  Parameters:
  ----------

  passenger: tuple
      a tuple with passenger's information
  Reutrns:
  --------
  new_passenger, tuple
      a new packed tuple
  """
  # unpack the tuple:
  (id, survived, name, gender, age) = passenger
  # pack the tuple:
  new_passenger = (age, gender, survived)
  return new_passenger

print(f"get_survival_info: {get_survival_info(passenger)}")
print(get_survival_info((11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)))
print(get_survival_info((28, False, "Fortune, Mr. Charles Alexander", "male", 19)))
print(get_survival_info((51, False, "Panula, Master. Juha Niilo", "male", 7)))
