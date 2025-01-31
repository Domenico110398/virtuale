class Client:
    def __init__(self, name, surname, age, email, card_code):
        self.name = name    
        self.surname = surname
        self.age = age
        self.email = email
        self.card_code = card_code

    def show_info(self):
        """method to show info"""
        print(f"Name: {self.name}\nSurname: {self.type}\nAge: {self.age}\nEmail {self.email}\nCard {self.card_code}")

    