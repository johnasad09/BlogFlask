from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
RECIPIENT_EMAIL = os.environ["RECIPIENT_EMAIL"]
SMTP = os.environ["SMTP"]



response = requests.get(" https://api.npoint.io/674f5423f73deab1e9a7")
all_post = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in all_post:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message: {message}"
    with smtplib.SMTP(SMTP, 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, RECIPIENT_EMAIL, email_message)



if __name__ == "__main__":
    app.run(debug=True)
