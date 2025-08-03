from flask import Flask, render_template
import requests

response = requests.get(" https://api.npoint.io/674f5423f73deab1e9a7")
all_post = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in all_post:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)





if __name__ == "__main__":
    app.run(debug=True)