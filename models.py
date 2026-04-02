class Dog:
    def _init_(self, dog_id, name, age, breed, adopted=False):
        self.id = dog_id
        self.name = name
        self.age = age
        self.breed = breed
        self.adopted = adopted

class Adopter:
    def _init_(self, adopter_id, name, lastName, address, id_card=None):
        self.adopter_id = adopter_id # Referecia a Person.id
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id_card = id_card