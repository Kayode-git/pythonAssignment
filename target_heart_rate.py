age = int(input("Enter your Age: "))

max_heart_rate = 220 - age

min_target_heart_rate = (50 / 100) * max_heart_rate

max_target_heart_rate = (85 / 100) * max_heart_rate

print(f"Your Maximum heart rate is: {max_heart_rate}")
print(f"Your Target heart rate range is: {min_target_heart_rate} - {max_target_heart_rate}")
