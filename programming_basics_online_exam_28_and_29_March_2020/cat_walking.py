minutes_walk = int(input())
number_of_walks = int(input())
calories_per_day = int(input())

time_walks = minutes_walk * number_of_walks
calories_burned_per_day = time_walks * 5
needed_calories_per_day = calories_per_day / 2
if calories_burned_per_day >= needed_calories_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned_per_day}.")
