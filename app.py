from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

app = Flask(__name__)
database = {}
with open('foods.json') as fp:
    database = json.load(fp)
print(database)


@app.route('/foods')
def foods_list_page():
    return render_template('foods.template.html', foods=database)


@app.route('/foods/add')
def show_foods_list_add():
    return render_template('add_foods.template.html')


@app.route('/foods/add', methods=["POST"])
def process_foods_list_add():
    print(request.form)
    food_name = request.form.get('food_name')
    calories = request.form.get('calories')
    meal = request.form.get('meal')
    when_eaten = request.form.get('when_eaten')
    # generate a random number as our customer_id
    # but usually, we will get the database to generate for us
    food_id = random.randint(4, 1000000)

    new_food = {}
    new_food['id'] = food_id
    new_food['food_name'] = food_name
    new_food['calories'] = calories
    new_food['meal'] = meal
    new_food['when_eaten'] = when_eaten

    database.append(new_food)

    # save the entire list into the json file. write the file
    with open('database.json', 'w') as fp:
        json.dump(database, fp)

    return "data received"

    # "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
