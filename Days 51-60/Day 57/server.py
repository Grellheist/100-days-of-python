from flask import Flask, render_template
from datetime import datetime
import requests

AGIFY_URL = "https://api.agify.io?name="
GENDERIZE_URL = "https://api.genderize.io?name="
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    agify_response = requests.get(f"{AGIFY_URL}{name}")
    genderize_response = requests.get(f"{GENDERIZE_URL}{name}")
    person_name = agify_response.json()["name"].title()
    person_age = agify_response.json()["age"]
    person_gender = genderize_response.json()["gender"]
    return render_template("guess.html",
                           name=person_name,
                           age=person_age,
                           gender=person_gender)


@app.route("/blog")
def get_blog():
    response = requests.get(BLOG_URL)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    response = requests.get(BLOG_URL)
    post = response.json()[blog_id-1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
