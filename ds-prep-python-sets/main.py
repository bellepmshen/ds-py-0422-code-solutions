# exercise 1-4:
trail_mix = {"m&m", "peanuts", "raisins"}
print(trail_mix)

# exercise 5-7:
print(f"Is cashews in trail_mix? {'cashews' in trail_mix}")
print(f"Is peanuts in trail_mix? {'peanuts' in trail_mix}")

# exercise 8-11:
trail_mix.add("pretzels")
trail_mix.update({"peanuts", "banana chips", "bits of jerky"})
print(trail_mix)

# exercise 12-16:
trail_mix.remove("m&m")
trail_mix.discard("raisins")
trail_mix.discard("rat poison")
print(trail_mix)

# exercise 17-19:
nuts = {"peanuts", "cashews", "almonds", "walnuts", "pecans"}
print(f"19.i: {nuts.union(trail_mix)}")
print(f"19.ii: {nuts.intersection(trail_mix)}")
print(f"19.iii: {trail_mix.difference(nuts)}")
print(f"19.iv: {nuts.difference(trail_mix)}")
