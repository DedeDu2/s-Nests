class Bird:
    def __init__(self, species):
        self.species = species
        self.nest = None

    def build_nest(self, materials):
        self.nest = materials

# Create Bird objects
bird1 = Bird("sparrow")
bird2 = Bird("parrot")

# Build nests
bird1.build_nest("twigs")
bird2.build_nest("leaves")

# Print nests
print("Nest of sparrow:", bird1.nest)
print("Nest of parrot:", bird2.nest)
