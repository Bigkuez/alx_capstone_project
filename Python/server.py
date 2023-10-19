from flask import Flask, render_template, request
from models import Contact  # Import your Contact model
from connection import session, database

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to my portfolio"

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a Contact instance and add it to the database
        contact = Contact(name=name, email=email, message=message)
        session.add(contact)
        session.commit()

        print("Data saved to the database.")

    return render_template("contactus.html")

if __name__ == "__main__":
    app.run(debug=True)
