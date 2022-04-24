# exercise 1-4:
day_of_week = "saturday"

if day_of_week == "saturday" or "sunday":
  print("Have a good weekend!")
else:
  print("It's a weekday!")

# exercise 5-7:
student_1_score = 86

if student_1_score > 70:
  pass_or_fail = "You passed!"
  print(student_1_score, pass_or_fail)

# exercise 8-10:
student_2_score = 92

if student_2_score < 60:
  letter_grade = "F"
elif student_2_score < 70:
  letter_grade = "D"
elif student_2_score < 80:
  letter_grade = "C"
elif student_2_score < 90:
  letter_grade = "B"
elif student_2_score < 100:
  letter_grade = "A"
else:
  letter_grade = "A+"

print(student_2_score, letter_grade)

# exercise 11-12:
def get_season_info(season):

  if season == "summer":
    return "Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though."
  elif season == "spring":
    return "The flowers are blooming while it's spring, but that correlation, not causation."
  elif season == "autumn":
    return "The leaves seem to regress to warmer colors as autumn approaches its end."
  elif season == "winter":
    return "There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater."
  else:
    return "That's not a season. Most likely."

print(f"summer: {get_season_info('summer')}")
print(f"spring: {get_season_info('spring')}")
print(f"autumn: {get_season_info('autumn')}")
print(f"winter: {get_season_info('winter')}")
print(f"others: {get_season_info('others')}")

# exercise 13-15:
age = 42
print("adult") if age > 18 else print("child")
