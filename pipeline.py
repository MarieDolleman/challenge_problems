# !/bin/bash
import csv
import json
from collections import OrderedDict
import click

@click.command()
@click.option('--filenames', '-f', multiple=True, help='Please enter a list of files for the data base')
def main(filenames):
    full_dict = []
    for name in filenames:
        with open(name, 'r') as emails:
            data = csv.DictReader(emails)
            for i in data:
                full_dict.append(OrderedDict(i))
    with open('new_data.json', 'w') as output:
        json.dump(full_dict, output)

if __name__ == '__main__':
    main()