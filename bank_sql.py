from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    second_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f"First name: {self.first_name}\
            \nSecond name: {self.second_name} \nAge: {self.age}\
            \nPhone number: {self.phone} \nEmail: {self.email}"


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, primary_key=True)
    data =  db.Column(db.Integer, nullable=False)
    cvv =  db.Column(db.Integer, nullable=False)
    validity =  db.Column(db.Integer, nullable=False)

    def __str__(self):
        return (f"\nInfo about card: \nNumber: {self.number}\
            \nData of issue: {self.data}\
            \nCVV: {self.cvv} \nValidity: {self.validity} year's")


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(20), nullable=False)
    specialty = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    income = db.Column(db.Integer, nullable=False)
    
    def __str__(self):
        return (f"\nInfo about job: \nCompany: {self.company}\
            \nSpecialty: {self.specialty} \nPosition: {self.position}\
             \nIncome for the year: {self.income}$")


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    house = db.Column(db.Integer, nullable=False)
    
    def __str__(self):
        return (f"\nInfo about address: \nCountry: {self.country}\
            \nCity: {self.city} \nStreet: {self.street}\
            \nHouse: {self.house}$")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)