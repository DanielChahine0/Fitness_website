import random

class Arms:
    def __init__(self) -> None:
        
        arms_1 = [
            "Bicep Curl (3 sets, 10 reps)", 
            "Tricep Dip (3 sets, 12 reps)", 
            "Hammer Curl (3 sets, 8 reps)", 
            "Tricep Pushdown (3 sets, 10 reps)", 
            "Barbell Curl (3 sets, 8 reps)"
            ]

        arms_2 = [
            "Dumbbell Curl (3 sets, 12 reps)", 
            "Tricep Extension (3 sets, 10 reps)", 
            "EZ Bar Curl (3 sets, 8 reps)", 
            "Tricep Pulldown (3 sets, 12 reps)", 
            "Preacher Curl (3 sets, 10 reps)"
            ]

        arms_3 = [
            "Cable Curl (3 sets, 10 reps)", 
            "Tricep Kickarms (3 sets, 12 reps)", 
            "Concentration Curl (3 sets, 8 reps)", 
            "Tricep Dips (3 sets, 10 reps)", 
            "Reverse Curl (3 sets, 8 reps)"
            
            ]
        
        arms_4 = [
            "Incline Dumbbell Curl (3 sets, 12 reps)", 
            "Tricep Pushdown (3 sets, 10 reps)", 
            "Barbell Curl (3 sets, 8 reps)", 
            "Tricep Extension (3 sets, 12 reps)", 
            "Hammer Curl (3 sets, 10 reps)"
            ]

        arms_5 = [
            "Dumbbell Curl (3 sets, 10 reps)", 
            "Tricep Dip (3 sets, 12 reps)", 
            "EZ Bar Curl (3 sets, 8 reps)", 
            "Tricep Pulldown (3 sets, 10 reps)", 
            "Preacher Curl (3 sets, 8 reps)"
            ]

        arms_6 = [
            "Cable Curl (3 sets, 12 reps)", 
            "Tricep Kickarms (3 sets, 10 reps)", 
            "Concentration Curl (3 sets, 8 reps)", 
            "Tricep Dips (3 sets, 12 reps)", 
            "Reverse Curl (3 sets, 10 reps)"
            ]

        arms_7 = [
            "Incline Dumbbell Curl (3 sets, 10 reps)", 
            "Tricep Pushdown (3 sets, 12 reps)", 
            "Barbell Curl (3 sets, 8 reps)", 
            "Tricep Extension (3 sets, 10 reps)", 
            "Hammer Curl (3 sets, 8 reps)"
            ]

        arms_8 = [
            "Dumbbell Curl (3 sets, 12 reps)", 
            "Tricep Dip (3 sets, 10 reps)", 
            "EZ Bar Curl (3 sets, 8 reps)", 
            "Tricep Pulldown (3 sets, 12 reps)", 
            "Preacher Curl (3 sets, 10 reps)"
            ]

        arms_9 = [
            "Cable Curl (3 sets, 10 reps)", 
            "Tricep Kickarms (3 sets, 12 reps)", 
            "Concentration Curl (3 sets, 8 reps)", 
            "Tricep Dips (3 sets, 10 reps)", 
            "Reverse Curl (3 sets, 8 reps)"
            ]
            
        arms_10 = [
            "Incline Dumbbell Curl (3 sets, 12 reps)", 
            "Tricep Pushdown (3 sets, 10 reps)", 
            "Barbell Curl (3 sets, 8 reps)", 
            "Tricep Extension (3 sets, 12 reps)", 
            "Hammer Curl (3 sets, 10 reps)"
            ]

        self.arms_focused = {
            1:arms_1,
            2:arms_2,
            3:arms_3,
            4:arms_4,
            5:arms_5,
            6:arms_6,
            7:arms_7,
            8:arms_8,
            9:arms_9,
            10:arms_10
        }

    def get_arms_workout(self):
        ran_index2 = random.randint(1, 10)
        arms_workout = ""
        for item in self.arms_focused[ran_index2]:
            arms_workout += item + "\n"
        return arms_workout

Workout2 = Arms()
print(Workout2.get_arms_workout())
        