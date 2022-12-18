class People():
    def __init__(self, first_name, second_name, age, phone, email):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"First name: {self.first_name}\
            \nSecond name: {self.second_name} \nAge: {self.age}\
            \nPhone number: {self.phone} \nEmail: {self.email}"


class Card():
    def __init__(self, number, data, cvv, validity):
        self.number = number
        self.data = data
        self.cvv = cvv
        self.validity = validity

    def __str__(self):
        return (f"\nInfo about card: \nNumber: {self.number}\
            \nData of issue: {self.data}\
            \nCVV: {self.cvv} \nValidity: {self.validity} year's")


class Job():
    def __init__(self, company, specialty, position, income):
        self.company = company
        self.specialty = specialty
        self.position = position
        self.income = income
    
    def __str__(self):
        return (f"\nInfo about job: \nCompany: {self.company}\
            \nSpecialty: {self.specialty} \nPosition: {self.position}\
             \nIncome for the year: {self.income}$")


class Address():
    def __init__(self, country, city, street, house):
        self.country = country
        self.city = city
        self.street = street
        self.house = house
    
    def __str__(self):
        return (f"\nInfo about address: \nCountry: {self.country}\
            \nCity: {self.city} \nStreet: {self.street}\
            \nHouse: {self.house}$")