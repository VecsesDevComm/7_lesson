import os.path
import copy
import csv

from algorithms.max import max_generic
from algorithms.min import min_generic
from algorithms.sort import bubble_generic
from algorithms.search import search_generic

stats = os.path.join(os.path.dirname(__file__), 'statistics')

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


def compare_fields(r1_field, r2_field):
    r1_float = float(r1_field.replace(',', '.'))
    r2_float = float(r2_field.replace(',', '.'))

    if r1_float > r2_float:
        return 1
    elif r1_float < r2_float:
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
    

def find_minimum(year_data, comparator):
    return min_generic(year_data, comparator)


def print_year_data(year_data, key):
    print('Country\t', key)
    for yd in year_data:
        print(yd['Country'] + '\t', yd[key])


def print_keys(year_data):
    for k in year_data[0].keys():
        print(k)
