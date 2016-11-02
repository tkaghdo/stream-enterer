__author__ = 'Tamby Kaghdo'

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(f1,f2,name):
    winner = ""
    f1_health = f1.health
    f1_attack = f1.damage_per_attack
    f2_health = f2.health
    f2_attack = f2.damage_per_attack
    turn = name
    while f1_health > 0 and f2_health > 0:
        if turn == f1.name:
            f2_health -= f1_attack
            turn = f2.name
        elif turn == f2.name:
            f1_health -= f2_attack
            turn = f1.name

    if f1_health > f2_health:
        winner = f1.name
    else:
        winner = f2.name
    return winner

def main():
    print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 50, 4),"Harry"))

if __name__ == '__main__':
    main()
