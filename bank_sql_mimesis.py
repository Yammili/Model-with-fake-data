import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mimesis import Generic
import argparse
import logging
from os import path
import random

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname} {message}",
    style='{'
)

Base = declarative_base()

class People(Base):
    """
    A model that describes a people with the following variables:
    id, full_name, nationality, age, job, phone, email.
    
    """
    __tablename__ = "people"

    id = db.Column("id", db.Integer, primary_key=True)
    full_name = db.Column("fullname", db.String)
    age = db.Column("age", db.Integer)
    job = db.Column("job", db.String)
    phone = db.Column("phone", db.String)
    email = db.Column("email", db.String)
    nationality = db.Column("nationality", db.String)
    country = db.Column("country", db.String)
    city = db.Column("city", db.String)
    street = db.Column("street", db.String)
    house = db.Column("house", db.Integer)
    zip_code = db.Column("zip_code", db.Integer)

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)

    def bootstrap(count, locale: str):
        """A function that generates random values for the people model and 
        automatically comments them to the database.

        Args:
            count (int): The amount of data to generate
            locale (str): Local data to be used for generation
        """
        
        maxGen = 5000 #limiting the maximum number of data generations
        
        if 0 <= count <= maxGen:
            generic = Generic(locale)
            
            for _ in range(count):
                people = People(
                    full_name = generic.person.full_name(),
                    nationality = generic.person.nationality(),
                    age = generic.person.age(minimum=16, maximum=100),
                    job = generic.person.occupation(),
                    phone = generic.person.telephone(),
                    email = generic.person.email(),
                    country = generic.address.country(),
                    city = generic.address.city(),
                    street = generic.address.street_name(),
                    house = generic.address.street_number(maximum=400),
                    zip_code = generic.address.zip_code()
                )
                session.add(people)
                session.commit()
        else: logging.error("The number of instances of model 'People' is not in the range: 0 : 5000") 
    
    def count_people():
        """A function that generates a random id of a person who is in the database

        Returns:
            int: Returns a random id
        """
        list = []
        for val in session.query(People.id).distinct():
            list.append(val[0])
        
        values = list[random.randint(0, len(list)-1)]
        return values


class Card(Base):
    """
    A model that describes someone's credit card with the following variables:
    id, number, data, cvv, validity, owner.

    """
    __tablename__ = "card"

    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.Integer)
    data =  db.Column("data", db.String)
    cvv =  db.Column("cvv", db.String)
    validity =  db.Column("valitidy", db.Integer)
    owner_id = db.Column("owner", db.Integer, db.ForeignKey("people.id"))

    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

    def bootstrap(count, locale: str):
        """A function that generates random values for the card model and 
        automatically comments them to the database.

        Args:
            count (int): The amount of data to generate
            locale (str): Local data to be used for generation
        """
        
        maxGen = 5000 #limiting the maximum number of data generations
        
        if 0 <= count <= maxGen:
            generic = Generic(locale)
            
            for _ in range(count):
                card = Card(
                    number = generic.payment.credit_card_number(),
                    data = generic.payment.credit_card_expiration_date(minimum=16, maximum=27),
                    cvv = generic.payment.cvv(),
                    validity = generic.random.randint(a=4, b=5),
                    owner_id = People.count_people()
                ) 
                session.add(card)
                session.commit()
        else: logging.error("The number of instances of model 'Card' is not in the range: 0 : 5000")

def delete(val):
    """The function that is used to delete a person and his card.

    Args:
        val (int): ID of the person and cardholder to delete
    """
    session.query(People).filter(People.id == val).delete()
    session.query(Card).filter(Card.owner_id == val).delete()
    session.commit()

def pars():
    """A script generation method that generates the amount of data that the 
    user enters through the console. Also checks if more addresses than people 
    have been created.

    """
    parser = argparse.ArgumentParser()

    parser.add_argument("it_people", type=int, help="Number of iterations for model 'People'")
    parser.add_argument("it_card", type=int, help="Number of iterations for model 'Card'")
    # parser.add_argument("it_delete", type=int, help="ID of the person and cardholder to delete")

    args = parser.parse_args()

    People.bootstrap(args.it_people,"en")
    Card.bootstrap(args.it_card,"en")

    # delete(args.it_delete)

if __name__ == "__main__":
    if not path.exists("sqlite:///base.db"):    
        engine = db.create_engine("sqlite:///base.db", echo=False)
        Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    logging.info("The database has been updated!")

    pars()
