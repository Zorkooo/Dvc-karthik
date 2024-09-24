class NutritionRecommender:
    def __init__(self, user_id, age, weight, dietary_preferences, recommended_calories):
        self.user_id = user_id
        self.age = age
        self.weight = weight
        self.dietary_preferences = dietary_preferences
        self.recommended_calories = recommended_calories

    def recommend_meal(self, meal_type):
        # Simple recommendation logic based on dietary preferences
        if self.dietary_preferences == 'Vegetarian':
            if meal_type == 'breakfast':
                return 'Oatmeal with fruits'
            elif meal_type == 'lunch':
                return 'Lentil soup with quinoa'
            elif meal_type == 'dinner':
                return 'Vegetable stir-fry with tofu'
        elif self.dietary_preferences == 'Non-Vegetarian':
            if meal_type == 'breakfast':
                return 'Eggs with whole-grain toast'
            elif meal_type == 'lunch':
                return 'Grilled chicken with vegetables'
            elif meal_type == 'dinner':
                return 'Salmon with brown rice and vegetables'
        else:
            return 'No suitable meal found'

# Example usage
user = NutritionRecommender(1, 25, 70, 'Vegetarian', 2000)
print(user.recommend_meal('breakfast'))
