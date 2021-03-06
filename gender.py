import os.path
import sys
import copy
import csv
import argparse
import pprint

from algorithms.max import max_generic, max_by_key
from algorithms.min import min_generic, min_by_key
from algorithms.sort import bubble_generic, bubble_by_key
from algorithms.search import search_generic, search_by_key

stats = os.path.join(os.path.dirname(__file__), 'statistics')

work = 'WORK'
money = 'MONEY'
time = 'TIME'
health = 'HEALTH'
know = 'KNOWLEDGE'
power = 'POWER'


def read_year_data(year):
    csv_path = os.path.join(stats, year + '.csv')

    if not os.path.exists(csv_path):
        return []

    year_data = []

    csv_file = open(csv_path)
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        year_data.append(row)

    csv_file.close()
    return year_data


def convert_values_to_floats(year_data):
    converted_year_data = []

    for record in year_data:
        for key in record.keys() - {'Country'}:
            val = float(record[key].replace(',', '.'))
            rnd = round(val, 3)
            record[key] = rnd

        converted_year_data.append(record)

    return converted_year_data


def compare_fields(r1_field, r2_field):
    if r1_field > r2_field:
        return 1
    elif r1_field < r2_field:
        return -1
    else:
        return 0


def print_year_data(year_data, key):
    print('Country\t', key)
    for yd in year_data:
        print(yd['Country'] + '\t', yd[key])


def print_year_data_table(year_data):
    columns = ('Country', work, money, time, health, know, power)

    header = "|"
    border = "+"
    for col in columns:
        line = (len(col) * "-").ljust(10, '-')
        border = border + line + "+"
        header = header + col.ljust(10) + "|"

    print(border)
    print(header)

    for record in year_data:
        row = "|"

        for column in columns:
            cs = str(record[column]).ljust(10)
            row = row + cs + "|"

        print(border)
        print(row)

    print(border)


def print_year_data_graph(year_data, key):
    columns = ('Country', key)

    header = "|"
    border = "+"
    for col in columns:
        line = (len(col) * "-").ljust(10, '-')
        border = border + line + "+"
        header = header + col.ljust(10) + "|"

    print(border)
    print(header)

    for record in year_data:
        country = record['Country'].ljust(10)
        value = round(record[key])
        print("|" + country + "|" + str(value) + " " + (value * "#"))


def print_year(args):
    year = args.year

    data = read_year_data(year)
    data = convert_values_to_floats(data)
    print_year_data_table(data)


def print_keys(year_data):
    for k in year_data[0]:
        print(k)


def maximums(args):
    year = args.year
    metrics = args.metrics
    
    year_data = read_year_data(year)
    year_data = convert_values_to_floats(year_data)
    for metric in metrics:
        print(metric)
        maximum = max_by_key(year_data, metric)
        print_year_data_table(maximum)


def minimums(args):
    year = args.year
    metrics = args.metrics
    
    year_data = read_year_data(year)
    year_data = convert_values_to_floats(year_data)
    for metric in metrics:
        print(metric)
        minimum = min_by_key(year_data, metric)
        print_year_data_table(minimum)


def find_country(args):
    year = args.year
    countries = args.countries
    
    year_data = read_year_data(year)
    year_data = convert_values_to_floats(year_data)
    for country in countries:
        key = 'Country'
        value = country
        adat = search_by_key(year_data, key, country)
        print_year_data_table([adat])


def order(args):
    year = args.year
    metric = args.metric
    table = args.table
    graph = args.graph
    print(args)


parser = argparse.ArgumentParser(description='Statistics Reader')
parser.add_argument('year', action='store', help='Válaszd ki az évet')
parser.add_argument('--print-metrics', '-pm', action='store_true',
                    dest='print_keys', help='Lista a metrikákról')
parser.set_defaults(func=print_year)

commands = parser.add_subparsers()

# Find Maximums command
parser_maximums = commands.add_parser(
    'maxi', help='Maximumok keresése az adott évben az adott metrikák szerint'
)
parser_maximums.add_argument(
    '-m', action='append', dest='metrics', default=[], help='Metrikák'
)
parser_maximums.set_defaults(func=maximums)


# Find Minimums command
parser_minimums = commands.add_parser(
    'mini', help='Minimumok keresése az adott évben adott metrikák szerint'
)
parser_minimums.add_argument(
    '-m', action='append', dest='metrics', default=[], help='Metrikák'
)
parser_minimums.set_defaults(func=minimums)


# Find Country
parser_country = commands.add_parser(
    'country', help='Ország keresése'
)
parser_country.add_argument(
    '-c', action='append', dest='countries', default=[], help='Országok'
)
parser_country.set_defaults(func=find_country)

# Order



# args = parser.parse_args(sys.argv[1:])
# args.func(args)

def rendez_work_szerint(year):
    return bubble_by_key(year, 'WORK')

year_data = read_year_data('2012')
year_data = convert_values_to_floats(year_data)
rendezve = rendez_work_szerint(year_data)
print_year_data_table(rendezve)
