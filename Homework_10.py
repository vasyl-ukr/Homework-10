# ДЗ 9. Домашня робота №12

# Реалізувати клас Герой що має мати наступні атрибути: ім‘я, здоров‘я, ранг, сила і метод вдарити.
# Метод вдарити повинен наносити шкоду противнику в розмірі сили героя.
# Герой має мати наступні обмеження: здоров‘я від 0 до 100, ранг 1,2,3.
# Сила не більше 10% теперішнього здоров‘я героя. Не можна бити героїв здоров‘я яких менше 5.

class Hero:
# Добавити атрибут захист герою defense та атаки attack:

    def __init__(self, name, health=100, rank=1, power=10, money=100, defense=0, attack=0):

        self.name = name
        self.health = health
        self.rank = rank
        self.power = power
        self.money = money

        self.defense = defense
        self.attack = attack
        self.sword = None
        self.shield = None




    def get_defense(self):
        return self.__defense

    def set_defense(self, value):
        self.__defense = value

    defense = property(get_defense, set_defense)


    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0

        self.__health = value

    health = property(get_health, set_health)

    def get_rank(self):
        return self.__rank

    def set_rank(self, value):
        if value > 3:
            value = 3
        elif value < 1:
            value = 1
        else:
            value = int(value)



        self.__rank = value

    rank = property(get_rank, set_rank)

    def get_power(self):
        return self.__power

    def set_power(self, value):
        if value > 0.1 * self.health:
            value = int(0.1 * self.health)

        self.__power = value

    power = property(get_power, set_power)

    def get_money(self):
        return self.__money

    def set_money(self, value):
        if value < 0:
            value = 0
        self.__money = value

    money = property(get_money, set_money)

    def alive(self):
        return self.health > 5

    def block(self, hit):
        damage = int(hit * (1 - self.defense / 10))
        if damage > 0:
            self.health -= damage
            print(f'{self.name} lost {damage} points of health')
            self.power = self.power


    def hit(self, otherHero):
        if not otherHero.alive():
            print('You cannot hit')
        else:
            hit = int(self.power * (1 + self.attack / 10))
            print(f'{self.name} strikes {hit} points')
            otherHero.block(hit)
# Створити можливість героям використовувати спорядження для збільшення захисту чи сили.

    def use_sword(self, sword):
        if not isinstance(self.sword, Sword):
            print('you don\'t have a sword to use')
        else:
            self.attack += sword.attack

    def use_shield(self, shield):

        if not isinstance(self.shield, Shield):
            print('you don\'t have a shield to use')
        else:
            self.defense += shield.defense


# Реалізувати клас маг, який може відновлювати здоров'я інших героїв, також він має ранг як герой і може наносити удари.
# За відновлення здоров'я він бере гроші. ( Вам потрібно реалізувати цей функціонал ).
# Герой заробляє гроші за перемогу у бою з іншим героєм, також при перемозі він забирає всі гроші суперника.
# Скільки герой отримує грошей за перемогу і скільки коштує відновити здоров'я, на ваш розсуд)


class Wizzard (Hero):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def cure(self, otherHero):
        CURE_FEE = 10
        if otherHero.money >= CURE_FEE:
            otherHero.money -= CURE_FEE
            self.money += CURE_FEE
            otherHero.health = 100
        else:
            print('Not enough money, come back latter')


# Клас Арена, на якій зустрічаються 2 героя і проводиться битва між ними - метод fight

class Arena:

    def __init__(self, name, hero_1, hero_2):
        self.name = name
        self.hero_1 = hero_1
        self.hero_2 = hero_2


    def fight(self):
        PRIZE = 50

        print(f'Welcome to the fight between {self.hero_1.name} and {self.hero_2.name} on {self.name} arena')
        while self.hero_1.alive() and self.hero_2.alive():                            # fight to the death
            if self.hero_1.rank >= self.hero_2.rank:                                       # first hit with higher rank
                self.hero_1.hit(self.hero_2)
                if self.hero_2.alive():
                    self.hero_2.hit(self.hero_1)
            else:
                self.hero_2.hit(self.hero_1)
                if self.hero_1.alive():
                    self.hero_1.hit(self.hero_2)

        if self.hero_1.alive():
            self.hero_1.money += PRIZE
            self.hero_1.money += self.hero_2.money
            print(f"{self.hero_1.name} won the fight and got {self.hero_2.money + PRIZE} coins")
            self.hero_2.money -= self.hero_2.money
        else:
            self.hero_2.money += PRIZE
            self.hero_2.money += self.hero_1.money
            print(f"{self.hero_2.name} won the fight and get {self.hero_1.money + PRIZE} coins")
            self.hero_1.money -= self.hero_1.money

# Захист: класи щит та меч - збільшують захист та атаку героя, мають ціну і можуть бути купленими на ринку

class Shield:

    def __init__(self, name, defense = 0, price = 0):
        self.name = name
        self.defense = defense
        self.price = price

class Sword:

    def __init__(self, name, attack=0, price=0):
        self.name = name
        self.attack = attack
        self.price = price

# Створити можливість героям використовувати спорядження для збільшення захисту чи сили.
# Зробити обмеження на кількість спорядження одним героєм ( один герою не може носити 100500 мечів і 200к щитів ).
# Герой може купити на маркеті меч чи щит у випадку відсутності у нього і застосувати його (збільшити атаку чи захист)

class Market:
    def __init__(self, item):
        self.item = item

    def sell(self, hero):
        if isinstance(self.item, Sword):
            if hero.sword is None:
                hero.sword = self.item
                hero.money -= self.item.price
                hero.use_sword(self.item)
            else:
                print('you cannot buy another sword')

        if isinstance(self.item, Shield):
            if hero.shield is None:
                hero.shield = self.item
                hero.money -= self.item.price
                hero.use_shield(self.item)
            else:
                print('you cannot buy another shield')



ukr = Hero('ukr')
rus = Hero('rus')

s = Sword('javeline', price=5, attack=3)
shield = Shield('ppo', price=15, defense=2)
s2 = Sword('mlrs', price=20, attack=5)
msword = Market(s)
msword.sell(ukr)

market_s2 = Market(s2)
market_s2.sell(ukr)
mshield = Market(shield)
mshield.sell(ukr)

print(ukr.sword.name, ukr.money, ukr.attack, ukr.defense)

print(ukr.shield.name, ukr.money, ukr.attack, ukr.defense)

a = Arena('Donbass', ukr, rus)
# a.fight()
print(ukr.health, ukr.defense, ukr.attack)

print(ukr.money, rus.money)
