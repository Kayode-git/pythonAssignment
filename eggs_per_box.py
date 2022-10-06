import math

eggs_per_box = 6
no_of_eggs = 28

no_of_needed_boxes = math.ceil(no_of_eggs / eggs_per_box)
print(f"Numbers of needed boxes = {no_of_needed_boxes}")

no_of_egg_in_last_box = no_of_eggs % eggs_per_box
print(f"Numbers of egg in last box = {no_of_egg_in_last_box}")

no_of_egg_to_fill_last_box = eggs_per_box - no_of_egg_in_last_box
print(f"Numbers of egg to fill the last box = {no_of_egg_to_fill_last_box}")


