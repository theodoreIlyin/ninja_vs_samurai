import random
import time


BAR_LENGTH = 20
TURN_DELAY = 1


class Character:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def speak(self) -> str:
        raise NotImplementedError("Метод speak() має бути перевизначений у дочірньому класі")

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)

    def hp_statistics(self) -> str:
        filled = int((self.hp / self.max_hp) * BAR_LENGTH)
        bar = "█" * filled + "░" * (BAR_LENGTH - filled)
        return f"{self.name}: [{bar}] {self.hp}/{self.max_hp} HP"


class Ninja(Character):
    def __init__(self):
        super().__init__("Ніндзя Тінь", 100)

    def speak(self) -> str:
        return random.choice([
            "Тіні вже поруч...",
            "Я завдам удару непомітно.",
            "Мій кунай знайде ціль.",
            "Тиха смерть наближається."
        ])

    def attack(self, attack_type: str) -> tuple[int, str]:
        if attack_type == "1":
            damage = random.randint(10, 20)
            return damage, f"Швидка атака сюрікеном! ({damage} шкоди)"
        elif attack_type == "2":
            damage = random.randint(25, 40)
            return damage, f"Сильна атака катаною! ({damage} шкоди)"
        elif attack_type == "3":
            if random.random() < 0.3:
                damage = random.randint(35, 50)
                return damage, f"ТОЧНИЙ УДАР! КРИТ! ({damage} шкоди)"
            else:
                damage = random.randint(15, 25)
                return damage, f"Точний удар! ({damage} шкоди)"
        else:
            return 0, "Невідома атака."


class Samurai(Character):
    def __init__(self):
        super().__init__("Самурай Акіо", 120)

    def speak(self) -> str:
        return random.choice([
            "Моя катана не знає пощади.",
            "Один удар може вирішити все.",
            "Твій шлях закінчується тут.",
            "Сила честі сильніша за страх."
        ])

    def attack(self) -> tuple[int, str]:
        attack_type = random.choice(["легка", "середня", "важка"])

        if attack_type == "легка":
            damage = random.randint(8, 12)
            return damage, f"Легка атака! ({damage} шкоди)"
        elif attack_type == "середня":
            damage = random.randint(15, 20)
            return damage, f"Удар двома катанами! ({damage} шкоди)"
        else:
            damage = random.randint(20, 25)
            return damage, f"Потужна атака! ({damage} шкоди)"


def show_intro(player: Ninja, enemy: Samurai) -> None:
    print("=" * 50)
    print("НІНДЗЯ ПРОТИ САМУРАЯ: БИТВА ТІНЕЙ")
    print("=" * 50)
    print("\nІсторія: самурай захопив село.")
    print("Ти — ніндзя, остання надія.")
    print("Лише ти можеш його зупинити.\n")

    time.sleep(TURN_DELAY)
    print(player.speak())
    print(enemy.speak())
    print("\nГра починається!")


def get_player_choice() -> str:
    print("\nТвій хід. Обери тип атаки:")
    print("1 - швидка (сюрікен)")
    print("2 - сильна (катана)")
    print("3 - точна (критична)")

    choice = input("Введи 1, 2 або 3: ").strip()
    while choice not in {"1", "2", "3"}:
        choice = input("Помилка. Введи тільки 1, 2 або 3: ").strip()

    return choice


def show_status(player: Ninja, enemy: Samurai, round_num: int) -> None:
    print(f"\nРАУНД {round_num}")
    print(player.hp_statistics())
    print(enemy.hp_statistics())


def player_turn(player: Ninja, enemy: Samurai) -> bool:
    choice = get_player_choice()
    damage, message = player.attack(choice)
    print(message)
    enemy.take_damage(damage)

    if not enemy.is_alive():
        print(f"\n💀 {enemy.name} повержений! Ти завдав останнього удару!")
        return True

    return False


def enemy_turn(player: Ninja, enemy: Samurai) -> bool:
    print("\nХід самурая...")
    time.sleep(TURN_DELAY)

    damage, message = enemy.attack()
    print(message)
    player.take_damage(damage)

    if not player.is_alive():
        print(f"\n{player.name} загинув у бою. Самурай переміг.")
        return True

    return False


def show_result(player: Ninja, enemy: Samurai) -> None:
    print("\n" + "=" * 50)
    print("БИТВА ЗАКІНЧЕНА")
    print("=" * 50)

    if player.is_alive() and not enemy.is_alive():
        print("\nПЕРЕМОГА!")
    elif not player.is_alive() and enemy.is_alive():
        print("\nПОРАЗКА!")
    else:
        print("\nНІЧИЯ!")


def battle() -> None:
    player = Ninja()
    enemy = Samurai()

    show_intro(player, enemy)

    round_num = 1

    while player.is_alive() and enemy.is_alive():
        show_status(player, enemy, round_num)

        if player_turn(player, enemy):
            break

        if enemy_turn(player, enemy):
            break

        round_num += 1

    show_result(player, enemy)


if __name__ == "__main__":
    battle()
