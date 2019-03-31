import os.path
import sys
import copy
import csv
import argparse
import pprint

from algorithms.max import max_generic, max_by_key
from algorithms.min import min_generic, min_by_key
from algorithms.sort import bubble_generic, bubble_by_key
from algorithms.search import search_generic

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


def gender_equality_index_comparator(r1, r2):
    r1_field = r1['Gender Equality Index']
    r2_field = r2['Gender Equality Index']
    return compare_fields(r1_field, r2_field)


def work_comparator(r1, r2):
    r1_field = r1['WORK']
    r2_field = r2['WORK']
    return compare_fields(r1_field, r2_field)


def money_comparator(r1, r2):
    r1_field = r1['MONEY']
    r2_field = r2['MONEY']
    return compare_fields(r1_field, r2_field)


def order_records(year_data, comparator):
    copied_list = copy.deepcopy(year_data)
    return bubble_generic(copied_list, comparator)


def find_record_by_key(year_data, comparator):
    return search_generic(year_data, comparator)


def find_maximum(year_data, comparator):
    return max_generic(year_data, comparator)


def find_maximum_by_key(year_data, key):
    return max_by_key(year_data, key)


def find_minimum(year_data, comparator):
    return min_generic(year_data, comparator)


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
    print(args)


def minimums(args):
    year = args.year
    metrics = args.metrics
    print(args)


def find_country(args):
    year = args.year
    countries = args.countries
    print(args)


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
parser_country.add_argument(
    '-o', '--order', action='store', dest='order',
    default='Gender Equality Index', help='Rendezési metrika'
)


# Order



# args = parser.parse_args(sys.argv[1:])
# args.func(args)

y2005 = read_year_data('2005')
y2005 = convert_values_to_floats(y2005)
max_time = max_by_key(y2005, time)
min_time = min_by_key(y2005, time)
y2005_ordered = bubble_by_key(y2005, time)
print_year_data_table(y2005_ordered)
