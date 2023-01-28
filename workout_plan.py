import random
chest_focused = {1:"Barbell bench press - 3 sets of 8-12 reps\nDumbbell flyes - 3 sets of 8-12 reps\nIncline barbell press - 3 sets of 8-12 reps\nPush-ups - 3 sets of 12-15 reps\nCable crossover - 3 sets of 12-15 reps", 2:"Dumbbell Press - 3 sets of 8-12 reps\nBarbell Incline Press - 3 sets of 8-12 reps\nDumbbell Pullover - 3 sets of 8-12 reps\nDips - 3 sets of 8-12 reps\nDumbbell Chest Fly - 3 sets of 8-12 reps\nCable Crossover Fly - 3 sets of 8-12 reps", 3: "Dumbbell Bench Press - 3 sets of 8-12 reps\nPec Deck Fly - 3 sets of 8-12 reps\nDumbbell Pullover - 3 sets of 8-12 reps\nClose-Grip Bench Press - 3 sets of 8-12 reps\nPush-Up - 3 sets of 8-12 reps"}

# list contains the number which shows however many workouts there are
workout_chest = [1,2,3]
# shuffle the list to increase randomness
random.shuffle(workout_chest)
# randomly select indexes
index = random.randint(0,2)
print(chest_focused[workout_chest[index]])
