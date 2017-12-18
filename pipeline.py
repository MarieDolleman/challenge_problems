# !/bin/bash
import csv
import json
from collections import OrderedDict
import click
import logging

logger = logging.getLogger(__name__)

@click.command()
@click.option('--filenames', '-f', multiple=True, help='Please enter a list of files for the data base')
def main(filenames):
    full_dict = []
    for name in filenames:
        try:
            with open(name, 'r') as emails:
                data = csv.DictReader(emails)
                for i in data:
                    full_dict.append(OrderedDict(i))
        except FileNotFoundError as f:
            logger.error('Unable to open file: %s \nPlease make sure path to file is correct' %name)
        except UnicodeDecodeError:
            logger.error('File: %s has an invalid file type. \nPlease convert to csv.' %name)
    with open('new_data.json', 'w') as output:
        json.dump(full_dict, output)

if __name__ == '__main__':
    main()