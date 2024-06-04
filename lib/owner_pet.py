class Pet:
    PET_TYPES= ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name,pet_type,owner=None):
    
        if pet_type not in self.PET_TYPES:
            raise ValueError("pet type must be in the list ofPET_TYPES")
        else:
            self.name=name
            self._pet_type=pet_type
            self.owner=owner
            self.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in self.PET_TYPES:
            raise ValueError("pet type must be in the list ofPET_TYPES")
        self._pet_type=value
        
    pass

class Owner:
    def __init__(self,name):
        self.name=name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner==self]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
         raise ValueError("pet must be an instance of Pet")
        
        pet.owner=self
        
    def get_sorted_pets(self):
        sortedpets=sorted(Pet.all, key=lambda pet:pet.name)
        return sortedpets
        

    pass