from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

story = ''

stories = {
    'dragons': {
        'name': 'Dragons',
        'prompts': ['Color', 'Superlative', 'Adjective', 'Body Part (plural)', 'Body Part', 'Noun', 'Animal (plural)', 'Adjective2', 'Adjective3', 'Adjective4'],
        'text': """The {Color} Dragon is the {Superlative} Dragon of all. 
                It has {Adjective} {body part (Plural)}, and a {Body Part} shaped like a {Noun}. 
                It loves to eat {Animal (plural)}, although it will feast on nearly anything. 
                It is {Adjective2} and {Adjective3}. You must be {Adjective4} around it, 
                or you may end up as it`s meal!"""
    },
    'wash-face': {
        'name': 'How to Wash Your Face',
        'prompts': ['Adverb', 'Noun', 'Liquid', 'Verb', 'Number', 'Noun (plural)', 'Verb2', 'Adjective', 'Noun2', 'Noun (plural)2', 'Illness', 'Occupation', 'Body Part (plural)', 'Body Part'],
        'text': """In order to wash your face {Adverb}, you must wet your {Noun} in warm {Liquid}. 
        Then, {Verb} it across your face {Number} times. This will wash off any remaining {Noun (plural)}. 
        When you are done you should {Verb2} the cloth in {Adjective} water to clean it. 
        You should also wash your face with a {Noun2} to keep it smooth and shiny. 
        This will keep also keep away {Noun (plural)2}. Don`t worry. It is normal to experience {Illness} the first time you try this. 
        Consult your {Occupation} if you break out in {Body Part (plural)}. This works well on your {Body Part} too!""",

    },
    'pizza-parlor': {
        'name': 'Pizza Parlor',
        'prompts': ['Male Name', 'Adjective', 'Noun', 'Adjective2', 'Food (plural)', 'Noun (plural)', 'Verb ending in "-ed"', 'Liquid', 'Noun2'],
        'text': """Come on over to {Male Name}`s Pizza Parlor where you can enjoy your favorite {Adjective}-dish pizzas. 
        You can try our famous {Noun}-Lover's pizza, or select from our list of {Adjective2} toppings, including sauteed {Food (plural)}, {Noun (plural)}, and many more. 
        Our crusts are hand-{Verb ending in "-ed"} and basted in {Liquid} to make them seem more {Noun2}-made.""",
    },
}


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/form')
def madlib_form():
    madlib = request.args.get('madlib')

    if madlib:
        global story
        story = Story(stories[madlib]['prompts'], stories[madlib]['text'])
        return render_template('madlib_form.html', prompts=story.prompts)

    else:
        flash("Please choose a Madlib!")
        return redirect('/')


@app.route('/story')
def generate_story():
    response = request.args

    full_story = story.generate(response)

    return render_template('story.html', story=full_story)
