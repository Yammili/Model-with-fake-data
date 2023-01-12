import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mimesis import Generic
import argparse
import logging

logging.basicConfig(
    level=logging.ERROR,
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
    nationality = db.Column("nationality", db.String)
    age = db.Column("age", db.Integer)
    job = db.Column("job", db.String)
    phone = db.Column("phone", db.String)
    email = db.Column("email", db.String)

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)

    def bootstrap(count, locale: str):
        """A function that generates random values for the people model and 
        automatically comments them to the database.

        Args:
            count (_type_): The amount of data to generate
            locale (str): Local data to be used for generation
        """
        if 0 <= count <= 5000:
            generic = Generic(locale)
            
            for _ in range(count):
                people = People(
                    id = generic.numeric.increment(),
                    full_name = generic.person.full_name(),
                    nationality = generic.person.nationality(),
                    age = generic.person.age(minimum=16, maximum=100),
                    job = generic.person.occupation(),
                    phone = generic.person.telephone(),
                    email = generic.person.email()
                )
                session.add(people)
                session.commit()
        else: logging.error("The number of instances of model 'People' is not in the range: 0 : 5000") 


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
    owner = db.Column("owner", db.String)

    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

    def bootstrap(count, locale: str):
        """A function that generates random values for the card model and 
        automatically comments them to the database.

        Args:
            count (_type_): The amount of data to generate
            locale (str): Local data to be used for generation
        """
        if 0 <= count <= 5000:
            generic = Generic(locale)
            
            for _ in range(count):
                card = Card(
                    id = generic.numeric.increment(),
                    number = generic.payment.credit_card_number(),
                    data = generic.payment.credit_card_expiration_date(minimum=16, maximum=27),
                    cvv = generic.payment.cvv(),
                    validity = generic.random.randint(a=4, b=5),
                    owner = generic.person.full_name()
                ) 
                session.add(card)
                session.commit()
        else: logging.error("The number of instances of model 'Card' is not in the range: 0 : 5000")


class Address(Base):
    """
    A model that describes someone's address with the following variables:
    id, country, city, street, house, zip code, inhabitant.
    
    """
    __tablename__ = "address"
     
    id = db.Column("id", db.Integer, primary_key=True)
    country = db.Column("country", db.String)
    city = db.Column("city", db.String)
    street = db.Column("street", db.String)
    house = db.Column("house", db.Integer)
    zip_code = db.Column("zip_code", db.Integer)
    inhabitant = db.Column("inhabitant", db.String)
    
    def __init__(self, **kwargs):
        super(Address, self).__init__(**kwargs)

    def bootstrap(count, locale: str):
        """A function that generates random values for the address model and 
        automatically comments them to the database.

        Args:
            count (_type_): The amount of data to generate
            locale (str): Local data to be used for generation
        """
        if 0 <= count <= 5000:   
            generic = Generic(locale)
            
            for _ in range(count):
                address = Address(
                    id = generic.numeric.increment(),
                    country = generic.address.country(),
                    city = generic.address.city(),
                    street = generic.address.street_name(),
                    house = generic.address.street_number(maximum=400),
                    zip_code = generic.address.zip_code(),
                    inhabitant = generic.person.full_name()
                )
                session.add(address)
                session.commit()
        else: logging.error("The number of instances of model 'Address' is not in the range: 0 : 5000")

def pars():
    parser = argparse.ArgumentParser()

    parser.add_argument("it_people", type=int, help="Number of iterations for model 'People'")
    parser.add_argument("it_card", type=int, help="Number of iterations for model 'Card'")
    parser.add_argument("it_address", type=int, help="Number of iterations for model 'Address'")

    args = parser.parse_args()
    
    People.bootstrap(args.it_people,"en")
    Card.bootstrap(args.it_card,"en")
    Address.bootstrap(args.it_address,"en")


if __name__ == "__main__":
    engine = db.create_engine("sqlite:///base.db", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    pars()
