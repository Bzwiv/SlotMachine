class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def ring(self):
        print (f"ring ring, ring ring. Hello, {self.name}")

person1 = Person("Bzwiv", "test@test.com", 1234567890)

person1.ring()