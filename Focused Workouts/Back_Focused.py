import random

class Back:
    def __init__(self) -> None:
        back_1 = [
            "Pull-ups (3 sets of 8-12 reps)",
            "Bent-over rows (3 sets of 8-12 reps)",
            "Seated cable rows (3 sets of 8-12 reps)",
            "Dumbbell deadlifts (3 sets of 8-12 reps)",
            "Lat pulldowns (3 sets of 8-12 reps)"
        ]

        back_2 = [
            "Seated cable rows (4 sets of 6-10 reps)",
            "Deadlifts (4 sets of 6-10 reps)",
            "Barbell rows (4 sets of 6-10 reps)",
            "Pulldowns (4 sets of 6-10 reps)",
            "Inverted rows (4 sets of 6-10 reps)"
        ]

        back_3 = [
          "One-arm dumbbell rows (3 sets of 8-12 reps per arm)",
          "Barbell deadlifts (3 sets of 8-12 reps)",
          "Barbell rows (3 sets of 8-12 reps)",
          "Cable pulldowns (3 sets of 8-12 reps)",
          "Hyperextensions (3 sets of 8-12 reps)"
        ]

        back_4 = [
          "Cable pulldowns (3 sets of 8-12 reps)",
          "Hyperextensions (3 sets of 8-12 reps)",
          "Lat pulldowns (3 sets of 8-12 reps)",
          "Renegade rows (3 sets of 8-12 reps)",
          "Seated cable rows (3 sets of 8-12 reps)"
          
        ]

        back_5 = [
          "Barbell rows (3 sets of 8-12 reps)",
          "Pull-ups (3 sets of 8-12 reps)",
          "Dumbbell pullovers (3 sets of 8-12 reps)",
          "Rack pulls (3 sets of 8-12 reps)",
          "Bent-over rows (3 sets of 8-12 reps)"

        ]

        back_6 = [
          "Bent-over rows (3 sets of 8-12 reps)",
          "Seated cable rows (3 sets of 8-12 reps)",
          "Lat pulldowns (3 sets of 8-12 reps)",
          "Reverse grip pull-ups (3 sets of 8-12 reps)",
          "Inverted rows (3 sets of 8-12 reps)"

        ]

        back_7 = [
          "Dumbbell Deadlifts (3 sets of 8-12 reps)",
          "Pull-ups (3 sets of 8-12 reps)",
          "Barbell rows (3 sets of 8-12 reps)",
          "Dumbbell rows (3 sets of 8-12 reps)",
          "Lat pulldowns (3 sets of 8-12 reps)"
          
        ]

        back_8 = [
          "Barbell deadlifts (3 sets of 8-12 reps)",
          "Pull-ups (3 sets of 8-12 reps)",
          "T-bar rows (3 sets of 8-12 reps)",
          "Seated cable rows (3 sets of 8-12 reps)",
          "Reverse Grip Pulldowns (3 sets of 8-12 reps)"
        ]

        back_9 = [
          "Barbell rows (3 sets of 8-12 reps)",
          "Pull-ups (3 sets of 8-12 reps)",
          "Dumbbell pullovers (3 sets of 8-12 reps)",
          "Inverted rows (3 sets of 8-12 reps)",
          "Good mornings (3 sets of 8-12 reps)"
        ]

        back_10 = [
          "Pull-ups (3 sets of 8-12 reps)",
          "Dumbbell rows (3 sets of 8-12 reps per arm)",
          "Cable pulldowns (3 sets of 8-12 reps)",
          "Hyperextensions (3 sets of 8-12 reps)",
          "Barbell deadlifts (3 sets of 8-12 reps)"

        ]

        self.back_focused = {
            1:back_1,
            2:back_2, 
            3:back_3, 
            4:back_4, 
            5:back_5, 
            6:back_6, 
            7:back_7,
            8:back_8, 
            9:back_9,
            10:back_10
        }
    
    def get_b_workout(self):
        ran_index2 = random.randint(1, 10)
        back_workout = ""
        for item in self.back_focused[ran_index2]:
            back_workout += item + "\n"
        return back_workout

Workout2 = Back()
print(Workout2.get_b_workout())
