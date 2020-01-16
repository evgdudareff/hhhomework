class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f'Автомобиль марки {self.brand}, модель {self.model}\n'


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def addCar(self, newCar):
        self.cars.append(newCar)

    def removeCar(self, carIndex):
        if carIndex >= len(self.cars):
            return
        self.cars.pop(carIndex)

    def __repr__(self):
        for car in self.cars:
            print(car)
        return ''

    def __getitem__(self, pos):
        return self.cars[pos]


# Пример использования класса Car
print('-----------создали одну машину-----------------')
bmwX3 = Car('BMW', 'X3')
print(bmwX3)  # Автомобиль марки BMW, модель X3

print('-----------создали гараж-----------------------')
# Пример использования класса Garage
garage = Garage([Car('BMW', 'X5'), Car('Audi', 'A3'), Car('VW', 'Golf')])
print(garage)  # выведет авто

print('-----------добавляем авто----------------------')
garage.addCar(Car('Tesla', 'Model X'))
print(garage)  # выведет авто

print('-----------удаляем авто------------------------')
garage.removeCar(3)
print(garage)  # выведет авто

print('-----------переопределили get item-------------')
print(garage[0])  # переопределили get item
for car in garage:
    print(car)
