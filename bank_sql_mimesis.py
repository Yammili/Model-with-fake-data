import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mimesis import Generic

Base = declarative_base()

class People(Base):
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

    def _bootstrap(count, locale: str):
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
            print(people)


class Card(Base):
    __tablename__ = "card"

    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.Integer)
    data =  db.Column("data", db.String)
    cvv =  db.Column("cvv", db.String)
    validity =  db.Column("valitidy", db.Integer)
    owner = db.Column("owner", db.String)

    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

    def _bootstrap(count, locale: str):
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
            print(card)


class Address(Base):
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

    def _bootstrap(count, locale: str):
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
            print(address)


engine = db.create_engine("sqlite:///base.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

iteration = 25                    #number of iterations

People._bootstrap(iteration,"en")
Card._bootstrap(iteration,"en")
Address._bootstrap(iteration,"en")