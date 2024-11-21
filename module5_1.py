class House:
    def __init__(self, name, floors_count):
        self.name = name
        self.floors_count = floors_count

    def go_to(self, new_floor):
        if self.floors_count < new_floor:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)