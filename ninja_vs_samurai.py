import random
import time

class Character:

    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def speak(self):
        return f'{self.name}   звук атаки'

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def hp_statistics(self):
        bar_length = 20
        filled = int((self.hp / 100) * bar_length)
        bar = '█' * filled + '░' * (bar_length - filled)
        return f'{self.name}:  [{bar}]  {self.hp}/100 HP'
    
class Ninja(Character):
   
    def __init__(self):
        super().__init__('Ниндзя тень', 100)

    def speak(self):
        return random.choice([
            "атаки  тени",
            'удар в спину',
            'кунай летит в цель',
            'тихая смерть'
        ])
   
    def attack(self, attack_type):
        if attack_type == '1' or attack_type == 'быстрая атака':
            damage = random.randint(10, 20)
            print(f'быстрая атака сюрикеном! ({damage} урона)')
            return damage
        elif attack_type == '2' or attack_type == 'сильный':
            damage = random.randint(25, 40)
            print(f'Сильная атака катаной! ({damage} урона)')
            return damage
        elif attack_type == '3' or attack_type == 'точный удар':
            if random.random() < 0.3:
                damage = random.randint(35, 50)
                print(f'ТОЧНЫЙ УДАР КАТАНОЙ! КРИТ! ({damage} урона)')
            else:
                damage = random.randint(15, 25)
                print(f'точный удар! ({damage})')
            return damage
        else:
            print('непонятная атака??? повтори еще раз')
            return 0 

class Samurai(Character):

    def __init__(self):
        super().__init__('Самурай Акио', 120)

    def speak(self):
        return random.choice([
            'Клинок рассёк воздух — и твою защиту вместе с ним',
            'Тень самурая мелькнула — удар уже нанесён',
            'Холодная сталь нашла свою цель',
            'Последний взмах катаны — и ты на грани поражения'
        ])
    
    def attack(self):
        attack_type = random.choice(['легкая', 'средняя', 'тяжелая'])

        if attack_type == 'легкая':
            damage = random.randint(8, 10)
            print(f"легкая атака! ({damage} урона)")
        elif attack_type == 'средняя':
            damage = random.randint(15, 20)
            print(f'удар двумя катанами! ({damage} урона)')
        else:
            damage = random.randint(20, 23)
            print(f'грандиозная атака! ({damage} урона)')

        return damage
    
def battle():    
    print('=' * 50)
    print('НИНДЗЯ ПРОТИВ САМУРАЯ БИТВА ТЕНЕЙ!')
    print('=' * 50)

    player = Ninja()
    enemy = Samurai()

    print('\n История: самурай захватил деревню')
    print('ты ниндзя  последния надежда на тебе')
    print('ты можешь победить его только ты\n')

    time.sleep(1)
    print(f'{player.speak()}')
    print(f'{enemy.speak()}')
    print('игра начинается')

    round_num = 1

    while player.is_alive() and enemy.is_alive():
        print(f'\n РАУНД {round_num}')
        print(player.hp_statistics())
        print(enemy.hp_statistics())
        print()

        print('Твой ход выбери тип атаку:')
        print('1 - быстрый (сюрикен)')
        print('2 - сильный (катана)')
        print('3 - точный (крит)')
        choice = input('твой ход (1/2/3):').strip().lower()

        player_damage = player.attack(choice)
        enemy.take_damage(player_damage)

        if not enemy.is_alive():  # ✅ теперь внутри while
            print(f'\n 💀 {enemy.name} повержен! ты нанес последний удар!')
            break

        print('\n ход самурая')
        time.sleep(1)

        enemy_damage = enemy.attack()
        player.take_damage(enemy_damage)

        if not player.is_alive():  # ✅ теперь внутри while
            print(f'\n {player.name} пал в бою самурай победил')
            break

        round_num += 1

    print('\n' + "=" * 50)
    print('битва окончена')
    print('=' * 50)

    if player.is_alive() and not enemy.is_alive():
        print('\n победа!')
    elif not player.is_alive() and enemy.is_alive():
        print('ПОРАЖЕНИЕ')
    else:
        print('ничья')

if __name__ == "__main__":
    battle()