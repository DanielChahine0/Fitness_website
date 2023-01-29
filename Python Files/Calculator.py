class Person:
    # Gender (Male or Female)
    # Age (In Years)
    # Height (in Meters)
    # Weight (in Kilograms)
    def __init__(self, gender, age, height, weight) -> None:
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
    
    # This method will calculate your BMI (Body Mass Index)
    # This is usually used to measure the physical fitness of a person
    def calculateBMI(self):
        # Under 18.4 -> Underweight
        # Between 18.5 and 24.9 -> Normal
        # Between 25.0 and 39.9 -> Overweight
        # Over 40.0 -> Obese

        # BMI formula
        self.BMI = (self.weight) / ((self.height)**2)
        return round(self.BMI, 2)

    # Body Metabolic Rate Method
    def calculateBMR(self):
        weight = self.weight
        age = self.age
        height = self.height
        # Since there is more than one formula for the BMR, I will use
        # --- more than one formula and then calculate the average between them.
        if self.gender == "female":
            BMR1 = 655.1 + (9.563 * weight) + (1.850 * height * 100) - (4.676 * age)
            BMR2 = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.33 * age)
            BMR3 = (10 * weight) + (6.25 * height * 100) - (5 * age) - 161
        
        elif self.gender == "male":
            BMR1 = 66.5 + (13.75 * weight) + (5.003 * height * 100) - (6.75 * age) 
            BMR2 = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
            BMR3 = (10 * weight) + (6.25 * height * 100) - (5 * age) + 5

        else:
            return "Invalid"
        
        self.BMR = (BMR1 + BMR2 + BMR3) / 3
        return round(self.BMR, 2)

    # Calories Burnt by Day Method
    def BurningCalories(self, activity:int=3):
        # This calculator will use numbers (1, 2, 3, 4, 5) to determine
        # --- how many calories are being burnt in a day
        
        # If the person is sedentary (little to no exercise)
        if activity == 1:
            calories = self.BMR * 1.2
        
        # if the person is lightly active (light exercise 1-3 days/week)
        elif activity == 2:
            calories = self.BMR * 1.375
        
        # if the person is modertly active (moderate exercise 3-5 days/week)
        elif activity == 3:
            calories = self.BMR * 1.55
        
        # if the person is very active (hard exercise/sports 6-7 days a week)
        elif activity == 4:
            calories = self.BMR * 1.725
        
        # if the person is extra active (very hard daily exercise and a physical job)
        elif activity == 5:
            calories = self.BMR * 1.9
        
        # if none of the options were chosen
        else:
            calories = 0
        
        return round(calories, 2)