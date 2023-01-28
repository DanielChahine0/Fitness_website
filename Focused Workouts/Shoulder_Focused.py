import random

class Shoulder:
    def __init__(self) -> None:
        shoulder_1 = [
            "Dumbbell Lateral Raises (3 sets of 8-12 reps)",
            "Dumbbell Front Raises (3 sets of 8-12 reps)",
            "Shoulder Press Barbell (3 sets of 8-12 reps)",
            "Dumbbell Push Press (3 sets of 8-12 reps)",
            "Smith Machine Shoulder Press (3 sets of 8-12 reps)"
        ]

        shoulder_2 = [
            "Seated Arnold Press (4 sets of 6-10 reps)",
            "Leaning Lateral Raises (4 sets of 6-10 reps)",
            "Incline Y raises (4 sets of 6-10 reps)",
            "Barbell Carry (4 sets of 6-10 reps)",
            "Single Arm Push Press (4 sets of 6-10 reps)"
        ]

        shoulder_3 = [
          "Alt. Dumbbell Press  (3 sets of 8-12 reps per arm)",
          "Barbell Shoulder Press (3 sets of 8-12 reps)",
          "Resistance Band Raise (3 sets of 8-12 reps)",
          "Leaning Shoulder Raises (3 sets of 8-12 reps)",
          "Seated Row (3 sets of 8-12 reps)"
        ]

        shoulder_4 = [
          "Standing Dumbbell Press  (3 sets of 8-12 reps per arm)",
          "Barbell Shoulder Press (3 sets of 8-12 reps)",
          "Cable Lateral Raise (3 sets of 8-12 reps)",
          "Leaning Shoulder Raises (3 sets of 8-12 reps)",
          "Seated Row (3 sets of 8-12 reps)"

        ]

        shoulder_5 = [
          "Arnold Press (3 sets of 8-12 reps)",
          "Military Press (3 sets of 8-12 reps)",
          "Smith Machine Press (3 sets of 8-12 reps)",
          "Single Arm Push Press (3 sets of 8-12 reps)",
          "Band raises (3 sets of 8-12 reps)"

        ]

        shoulder_6 = [
          "Incline Y Raises (4 sets of 6-10 reps)",
          "Barbell Shoulder Press (3 sets of 8-12 reps)",
          "Band raises (3 sets of 8-12 reps)"
          "Leaning Shoulder Raises (3 sets of 8-12 reps)",
          "Seated Row (3 sets of 8-12 reps)"

        ]

        shoulder_7 = [
          "Dumbbell Reverse Fly (4 sets of 6-10 reps)",
          "Dumbbell External Rotations (3 sets of 8-12 reps)",
          "Band Raises (3 sets of 8-12 reps)"
          "Overhead Press (3 sets of 8-12 reps)",
          "Lighter Overhead Press till failure (3 sets of 8-12 reps)"

          
        ]

        shoulder_8 = [
          "Dumbbell Rear Delt Fly (4 sets of 6-10 reps)",
          "Dumbbell External Rotations (3 sets of 8-12 reps)",
          "Upright Rows (3 sets of 8-12 reps)"
          "Face Pull (3 sets of 8-12 reps)",
          "Behind-the-neck Barbell Press (3 sets of 8-12 reps)"

        ]

        shoulder_9 = [
          "Band raises (3 sets of 8-12 reps)"
          "Incline Y Raises (4 sets of 6-10 reps)",
          "Upright Rows (3 sets of 8-12 reps)"
          "Behind-the-neck Barbell Press (3 sets of 8-12 reps)"
          "Seated Row (3 sets of 8-12 reps)"
          
        ]

        shoulder_10 = [
          "High Pulls (3 sets of 8-12 reps)"
          "Dumbbell Rear-delt Rows (4 sets of 6-10 reps)",
          "Upright Rows (3 sets of 8-12 reps)"
          "Seated Barbell Military Press (3 sets of 8-12 reps)"
          "Front Cable Raise (3 sets of 8-12 reps)"


        ]

        self.shoulder_focused = {
            1:shoulder_1,
            2:shoulder_2, 
            3:shoulder_3, 
            4:shoulder_4, 
            5:shoulder_5, 
            6:shoulder_6, 
            7:shoulder_7,
            8:shoulder_8, 
            9:shoulder_9,
            10:shoulder_10
        }
    
    def get_shoulders_workout(self):
        ran_index2 = random.randint(1, 10)
        shoulder_workout = ""
        for item in self.shoulder_focused[ran_index2]:
            shoulder_workout += item + "\n"
        return shoulder_workout

Workout = Shoulder()
print(Workout.get_shoulders_workout())
