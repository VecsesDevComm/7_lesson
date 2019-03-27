from algorithms.max import max_generic
from algorithms.min import min_generic
from algorithms.sort import bubble_generic

heroes = [
    {
        'name': 'Tony Stark',
        'alias': 'Iron Man',
        'skill': 'Gazdag and Okos',
        'level': 6,
        'kinezet': 5
    },
    {
        'name': 'Steve Rogers',
        'alias': 'Captain America',
        'skill': 'Szóó Páverful',
        'level': 5,
        'kinezet': 8
    },
    {
        'name': 'Scarlet Witch',
        'alias': 'Wanda Maximoff',
        'skill': 'Mindstone',
        'level': 9,
        'kinezet': 8
    },
    {
        'name': 'Black Widow',
        'alias': 'Natasha Alianovna Romanoff',
        'skill': 'Csinos és gyilkos',
        'level': 5,
        'kinezet': 10
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
    max_level_heroes = max_generic(heroes, szint_alapjan)
    return max_level_heroes


def get_sexiest_hero():
    sexiest_heroes = max_generic(heroes, kinezet_alapjan)
    return sexiest_heroes

def get_min_level_hero():
    weakest_heroes = min_generic(heroes, szint_alapjan)
    return weakest_heroes


def get_ugliest_hero():
    unattractive_heroes = min_generic(heroes, kinezet_alapjan)
    return unattractive_heroes


def fight(h1, h2):
    if szint_alapjan(h1, h2) == 1:
        return h1
    elif szint_alapjan(h1, h2) == -1:
        return h2
    else:
        return None

def print_heroes(hlist):
    for h in hlist:
        print(h['name'], 'szint:', h['level'], 'külső:', h['kinezet'])



print('Legerősebbek')
print_heroes(get_max_level_hero())
print('Legszexibbek')
print_heroes(get_sexiest_hero())
print('Legcsúnyábbak')
print_heroes(get_ugliest_hero())
print('Leggyengébbek')
print_heroes(get_min_level_hero())

weakest = get_min_level_hero()[0]
ugliest = get_ugliest_hero()[0]
winner = fight(weakest, ugliest)

print('harc', weakest['name'], 'és', ugliest['name'], 'között')
if winner is not None:
    print('Győztes', winner['name'])
else:
    print('Döntetlen')


print('=====================')
bubble_generic(heroes, szint_alapjan)
print_heroes(heroes)
