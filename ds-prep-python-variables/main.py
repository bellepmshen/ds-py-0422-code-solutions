# exercise 1-10
first_name = 'Belle'
last_name = "Shen"

full_name = first_name + " " + last_name
print(full_name)

# exercise 11-14
height_in_inches = 61
print(f"My height in inches: {height_in_inches}")
print(f"type of the variable height_in_inches: {type(height_in_inches)}")

# exercise 15-17
height_in_inches_float = float(height_in_inches)
print(f"My height in inches (in float): {height_in_inches_float}")
print(f"type of the variable height_in_inches_float: {type(height_in_inches_float)}")

# exercise 18-20
height_in_meters = (height_in_inches_float*2.54)/100
print(f"height in meters: {height_in_meters}")

# exercise 21-28
eats_plant = True
eats_animal = False
is_animal = eats_plant or eats_animal
print(f"is_animal = {is_animal}")

is_omnivore = eats_plant and eats_animal
print(f"is_omnivore = {is_omnivore}")

is_plant = not(is_animal)
print(f"is_plant = {is_plant}")

# exercise 29-31
mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860

is_mean_height = (height_in_meters == mean_height_in_meters)
print(f"is_mean_height = {is_mean_height}")

is_short = (height_in_meters < short_threshold_in_meters)
print(f"is_short = {is_short}")

is_tall = (height_in_meters >= tall_threshold_in_meters)
print(f"is_tall = {is_tall}")

is_normal_height = (height_in_meters >= short_threshold_in_meters) & \
                   (height_in_meters < tall_threshold_in_meters)
print(f"is_normal_height = {is_normal_height}")

# exercise 32-34
nothing = None
print(nothing, type(nothing))
