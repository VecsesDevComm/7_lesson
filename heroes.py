from algorithms.max import max_generic
from algorithms.min import min_generic


heroes = [
    {
        'name': 'Tony Stark',
        'alias': 'Iron Man',
        'skill': 'Gazdag and Okos',
        'level': 7,
        'kinezet': 5
    },
    {
        'name': 'Steve Rogers',
        'alias': 'Captain America',
        'skill': 'Szóó Páverful',
        'level': 6,
        'kinezet': 8
    },
    {
        'name': 'Scarlet Witch',
        'alias': 'Wanda Maximoff',
        'skill': 'Mindstone',
        'level': 8,
        'kinezet': 8
    },
    {
        'name': 'Black Widow',
        'alias': 'Natasha Alianovna Romanoff',
        'skill': 'Csinos és gyilkos',
        'level': 5,
        'kinezet': 9
    },
    {
        'name': 'Thor',
        'alias': 'Thor',
        'skill': 'God',
        'level': 9,
        'kinezet': 10
    }
]

# 0 -> Ha h1 és h2 egyenlőek
# 1 -> Ha h1 nagyobb
# -1 -> Ha h2 nagyobb
def szint_alapjan(h1, h2):
    if h1['level'] > h2['level']:
        return 1
    elif h1['level'] < h2['level']:
        return -1
    else:
        return 0


# 0 -> Ha h1 és h2 egyenlőek
# 1 -> Ha h1 nagyobb
# -1 -> Ha h2 nagyobb
def kinezet_alapjan(h1, h2):
    if h1['kinezet'] < h2['kinezet']:
        return -1
    elif h1['kinezet'] > h2['kinezet']:
        return 1
    else:
        return 0


def get_max_level_hero():
    hero = max_generic(heroes, szint_alapjan)
    return hero


def get_sexiest_hero():
    hero = max_generic(heroes, kinezet_alapjan)
    return hero

def get_min_level_hero():
    hero = min_generic(heroes, szint_alapjan)
    return hero


def get_ugliest_hero():
    hero = min_generic(heroes, kinezet_alapjan)
    return hero


def fight(h1, h2):
    if szint_alapjan(h1, h2) == 1:
        return h1
    elif szint_alapjan(h1, h2) == -1:
        return h2
    else:
        return None


print('Legerősebb', get_max_level_hero()['name'])
print('Legszexibb', get_sexiest_hero()['name'])
print('Legcsúnyább', get_ugliest_hero()['name'])
print('Leggyengébb', get_min_level_hero()['name'])

weakest = get_min_level_hero()
ugliest = get_ugliest_hero()
winner = fight(weakest, ugliest)

print('harc', weakest['name'], 'és', ugliest['name'], 'között')
if winner is not None:
    print('Győztes', winner['name'])
else:
    print('Döntetlen')
