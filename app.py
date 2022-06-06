from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def madlib_form():
    return render_template('homepage.html', prompts=story.prompts)


@app.route('/story')
def generate_story():
    response = request.args

    full_story = story.generate(response)

    return render_template('story.html', story=full_story)
