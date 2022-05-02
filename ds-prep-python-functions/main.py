# exercise 1:

bool_to_int = lambda value: int(value == True)
print(f"bool_to_int(True): {bool_to_int(True)}")
print(f"bool_to_int(False): {bool_to_int(False)}")

# exercise 2:

get_smaller = lambda a, b: min(a, b)
print(f"The smaller value of get_smaller(16, 31): {get_smaller(16, 31)}")
print(f"The smaller value of get_smaller(253, 223): {get_smaller(253, 223)}")

# exercise 3:

def cube(base):
  """This function is for calculating the cube value of
     a given number.

     Parameters:
     ----------

     base: int or float
          a given number for calculating the cube value
     Returns:
     -------
     base**3, int or float
          return the cube value of the base number
  """

  return base**3

print(f"the cube of 2 is: {cube(2)}")
print(f"the cube of 5 is: {cube(5)}")

# exercise 4:

def absolute_difference(a, b):
  """This function is for calculating the absolute value of
     the difference of 2 given numbers

     Parameters:
     ----------

     a: int or float
        a number
     b: int or float
        a number

     Returns:
     --------
     abs(a-b), int or float
        return the absolute value of the difference of a & b

  """
  return abs(a-b)

print(f"absolute_difference(14, 11): {absolute_difference(14, 11)}")
print(f"absolute_difference(13, 40): {absolute_difference(13, 40)}")

# exercise 5:

def squared_difference(a, b):
  """This function is for calculating the square value of
     the difference of 2 given numbers.

     Paramaters:
     ----------

     a: int or float
        a number
     b: int or float
        a number

     Returns:
     --------
     (a-b)**2, int or float
        return the square value of the difference of a and b
  """
  return (a-b)**2

print(f"squared_difference(14, 11): {squared_difference(14, 11)}")
print(f"squared_difference(13, 40): {squared_difference(13, 40)}")

# exercise 6:

def hours_to_minutes(hours):
  """This function is to convert hours into minutes.

    Paramters:
    ---------

    hours: int or float
      the hours need to be converted

    Returns:
    -------
    hours*60, int or float
      return the number of minutes

  """
  return hours*60

print(f"hours_to_minutes(hours = 3.5): {hours_to_minutes(hours = 3.5)}")
print(f"hours_to_minutes(hours = 12): {hours_to_minutes(hours = 12)}")

# exercise 7:

def get_circumference(radius):
  """This function is for calculating the circumference by
     a given radius.

     Paramaters:
     ----------

     radius: int or float
      the radius of a circle

     Returns:
     --------
     2*(np.pi)*(radius), float
      the circumference of a circle

  """
  pi = 3.141592653589793238
  return 2*(pi)*(radius)

print(f"get_circumference(radius = 1): {get_circumference(radius = 1)}")
print(f"get_circumference(radius = 9.2): {get_circumference(radius = 9.2)}")

# exercise 8:

def linear_transform(x, slope, intercept):
  """This function is to get y value from a linear eq (y = ax + b).

    Parameters:
    ----------

    x: float
      the x position
    slope: float
      the slope of a linear equation
    intercept: float
      the y intercept of a linear equation

    Returns:
    -------

    slope*x + intercept, float
       return the y value of a linear equation
  """
  return slope*x + intercept

print(f"linear_transform(x=5.0, slope=3.0, intercept=-8.5): {linear_transform(x=5.0, slope=3.0, intercept=-8.5)}")
print(f"linear_transform(slope=-2.1, intercept=17.0, x=2.5): {linear_transform(slope=-2.1, intercept=17.0, x=2.5)}")

# exercise 9:

def standardize(x, x_center, scale_size):
  """This function is to standardize the number.

     Parameters:
     -----------

     x: float
      the number to be standardized
     x_center: float
      the central value
     scale_size: float
       the value to be divided, should be a positive value

     Returns:
     --------
     (x-x_center)/scale_size, float
        the standardized value
  """
  return (x-x_center)/scale_size

print(f"standardize(x=8.2, x_center=13.8, scale_size=4.83): {standardize(x=8.2, x_center=13.8, scale_size=4.83)}")
print(f"standardize(scale_size=24.63, x=2.89, x_center=-72.813): {standardize(scale_size=24.63, x=2.89, x_center=-72.813)}")
