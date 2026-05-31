from flask import Flask

app = Flask(__name__)

class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat, fiber, goal):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.goal = goal

def load_data():
    return [
        FoodItem("Chicken breast",165,31,0,3.6,0,"gain"),
        FoodItem("Brown rice",111,2.6,23,0.9,1.8,"gain"),
        FoodItem("Apple",52,0.3,14,0.2,2.4,"loss"),
        FoodItem("Broccoli",34,2.8,7,0.4,2.6,"loss")
    ]

@app.route("/")
def home():
    return """
    <h1>Food Recommendation App</h1>

    <a href='/foods/gain'>Weight Gain Foods</a><br>
    <a href='/foods/loss'>Weight Loss Foods</a>
    """

@app.route("/foods/<goal>")
def foods(goal):

    data = load_data()

    filtered = [item for item in data if item.goal == goal]

    result = f"<h1>{goal.upper()} Foods</h1><ul>"

    for item in filtered:
        result += f"<li>{item.name} - {item.calories} calories</li>"

    result += "</ul>"

    return result

app.run(host="0.0.0.0", port=123)
