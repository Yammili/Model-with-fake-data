import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class People(Base):
    __tablename__ = "people"

    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("firstname", db.String)
    last_name = db.Column("lastname", db.String)
    gender = db.Column("gender", db.CHAR)
    age = db.Column("age", db.Integer)
    phone = db.Column("phone", db.String)
    email = db.Column("email", db.String)

    def __init__(self, id, first_name, last_name, gender, age, phone, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"({self.id}) {self.first_name} {self.last_name} {self.gender} {self.age} {self.phone} {self.email}"


class Card(Base):
    __tablename__ = "card"

    number = db.Column("number", db.Integer, primary_key=True)
    data =  db.Column("data", db.String)
    cvv =  db.Column("cvv", db.Integer)
    validity =  db.Column("valitidy", db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey("people.id"))

    def __init__(self, number, data, cvv, valitidy, owner):
        self.number = number 
        self.data = data
        self.cvv = cvv
        self.validity = valitidy
        self.owner = owner

    def __repr__(self):
        return f"({self.number}) {self.data} {self.cvv} {self.validity} owned by {self.owner}."


class Address(Base):
    __tablename__ = "address"
     
    id = db.Column("id", db.Integer, primary_key=True)
    country = db.Column("country", db.String)
    city = db.Column("city", db.String)
    street = db.Column("street", db.String)
    house = db.Column("house", db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey("people.id"))
    
    def __init__(self, id, country, city, street, house, owner):
        self.id = id
        self.country = country
        self.city = city
        self.street = street
        self.house = house 
        self. owner = owner 

    def __repr__(self):
        return f"({self.id}) {self.country} {self.city} {self.street} {self.house}  {self.owner}."

engine = db.create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = People(12312, "Mike", "Pop", "m", 28, "066565656", "123@gmail.com")
card = Card(20483434234234, "09/23", 123, 5, person.id)
address = Address(14333,"USA", "Miami", "Bread", 56, person.id)
session.add(person)
session.add(card)
session.add(address)
session.commit()

print(session.query(People, Card, Address).all())
