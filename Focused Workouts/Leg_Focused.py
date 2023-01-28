import random

class Leg:
    
    def __init__(self) -> None:

        leg_1 = [
             "Squat (3 sets of 10 reps)", 
             "Deadlift (3 sets of 12 reps)", 
             "Smith Squats (3 sets of 8 reps)", 
             "Leg Press (3 sets of 10 reps)", 
             "Leg Extension (3 sets of 8 reps)"
             ]

        leg_2 = [
             "Leg Curl (3 sets of 12 reps)", 
             "Calf Raise (3 sets of 10 reps)", 
             "Hip thrusts (3 sets of 8 reps)",
             "Romanian Deadlift (3 sets of 12 reps)", 
             "Single Leg Deadlift (3 sets of 10 reps)"
             ]

        leg_3 = [
             "Smith Squats (3 sets of 12 reps)", 
             "Leg Press (3 sets of 10 reps)", 
             "Leg Extension (3 sets of 8 reps)", 
             "Leg Curl (3 sets of 12 reps)", 
             "Calf Raise (3 sets of 10 reps)"
             ]

        leg_4 = [
             "Hip thrusts (3 sets of 12 reps)", 
             "Romanian Deadlift (3 sets of 10 reps)", 
             "Single Leg Deadlift (3 sets of 8 reps)", 
             "Squat (3 sets of 12 reps)", 
             "Deadlift (3 sets of 10 reps)"
             ]

        leg_5 = [
             "Smith Squats (3 sets of 10 reps)", 
             "Leg Press (3 sets of 12 reps)", 
             "Leg Extension (3 sets of 8 reps)", 
             "Leg Curl (3 sets of 10 reps)", 
             "Calf Raise (3 sets of 12 reps)"
             ]

        leg_6 = [
             "Hip thrusts (3 sets of 10 reps)", 
             "Romanian Deadlift (3 sets of 12 reps)", 
             "Single Leg Deadlift (3 sets of 8 reps)", 
             "Squat (3 sets of 10 reps)", 
             "Deadlift (3 sets of 12 reps)"
             ]

        leg_7 = [
             "Smith Squats (3 sets of 12 reps)", 
             "Leg Press (3 sets of 10 reps)", 
             "Leg Extension (3 sets of 8 reps)", 
             "Leg Curl (3 sets of 12 reps)", 
             "Calf Raise (3 sets of 10 reps)"
             ]

        leg_8 = [
             "Hip thrusts (3 sets of 12 reps)", 
             "Romanian Deadlift (3 sets of 10 reps)", 
             "Single Leg Deadlift (3 sets of 8 reps)", 
             "Squat (3 sets of 12 reps)", 
             "Deadlift (3 sets of 10 reps)"
             ]

        leg_9 = [
             "Smith Squats (3 sets of 10 reps)", 
             "Leg Press (3 sets of 12 reps)", 
             "Leg Extension (3 sets of 8 reps)", 
             "Leg Curl (3 sets of 10 reps)", 
             "Calf Raise (3 sets of 12 reps)"
             ]
             
        leg_10 = [
             "Leg Curl (3 sets of 12 reps)", 
             "Calf Raise (3 sets of 10 reps)", 
             "Hip thrusts (3 sets of 8 reps)",
             "Romanian Deadlift (3 sets of 12 reps)", 
             "Single Leg Deadlift (3 sets of 10 reps)"
             ]
        
        self.leg_focused = {
            1:leg_1,
            2:leg_2,
            3:leg_3,
            4:leg_4,
            5:leg_5,
            6:leg_6,
            7:leg_7,
            8:leg_8,
            9:leg_9,
            10:leg_10
        }

    def get_leg_workout(self):
        ran_index = random.randint(1, 10)
        leg_workout = ""
        for item in self.leg_focused[ran_index]:
            leg_workout += item + "\n"
        return leg_workout

Workout2 = Leg()
print(Workout2.get_leg_workout())
        