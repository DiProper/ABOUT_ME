# 3. Дописать классы Human, House, SmallHouse (как на последнем занятии).
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Стоимость с учетом скидки: {final_price} USD.")
        return final_price

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def display_info(self):
        self.small_house = 40
        print(f"Площадь маленького дома: {self.small_house} кв.м.")

class Human:

    default_name = "No name"
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, money):
        self.__money += money
        print(f"Получено: {money} USD. Текущий счет: {self.__money} USD.")

    def make_deal(self, price):
        self.__money -= price
        self.__house += 1

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(price)
        else:
            print("No money!")

small_house = SmallHouse(10000)
Dmitry = Human("Dmitry", 38)
Dmitry.info()
Dmitry.earn_money(5000)
Dmitry.info()
Dmitry.buy_house(small_house, 10)

Dmitry.earn_money(5000)
Dmitry.info()
Dmitry.buy_house(small_house, 10)
Dmitry.info()