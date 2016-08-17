import random
import heroes

def get_hero():
    role = input('What role are you going to play? [Any, Offlane, Mid, Carry, Support]\n')

    if role.lower() == 'any':
        print(random.choice(heroes.heroes))
    elif role.lower() == 'offlane':
        print(random.choice(heroes.offlane))
    elif role.lower() == 'mid':
        print(random.choice(heroes.mid))
    elif role.lower() == 'carry':
        print(random.choice(heroes.carry))
    elif role.lower() == 'support':
        print(random.choice(heroes.support))
    else:
        print('That isn\'t a role!')

if __name__ == '__main__':
    get_hero()
