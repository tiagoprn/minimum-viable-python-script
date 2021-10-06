#!/usr/bin/env python3

"""
Given lines with time records, filters the records showing the ones
that occur at the current time and the next ones, by the number specified
as parameter.

This is script is designed with the purposed to be used as a pipe to
a previous command to generate/list the records. Each record must be
separated by a newline.

e.g.

$ cat ../sample_input.txt | ./filter_time_records.py 3

This will show the next 3 records that will happen in the near future
(taking the current timestamp as the time reference).
"""

import argparse
import logging
import os
from datetime import datetime
from sys import stdin, stdout
from typing import List

CURRENT_SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
LOG_FORMAT = (
    '[%(asctime)s PID %(process)s '
    '%(filename)s:%(lineno)s - %(funcName)s()] '
    '%(levelname)s -> \n'
    '%(message)s\n'
)
logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(f'{CURRENT_SCRIPT_NAME}.log'),
        # logging.StreamHandler(stdout)
    ],
)


def _get_current_timestamp_in_12_hours_format() -> str:
    current_timestamp = datetime.now().strftime('%I:%M%p').lower()

    return (
        current_timestamp[1:]
        if current_timestamp.startswith('0')
        else current_timestamp
    )


def _get_datetime_instance_from_12_hours_format(
    timestamp_in_12_hours_format: str,
) -> datetime:
    day_str = datetime.now().strftime('%Y-%m-%d')
    full_datetime = f'{day_str} {timestamp_in_12_hours_format.upper()}'
    return datetime.strptime(full_datetime, '%Y-%m-%d %I:%M%p')


def _filter_records(data: List[str], number_of_records: int) -> List[str]:
    filtered_records = []

    current_timestamp = _get_current_timestamp_in_12_hours_format()

    logging.info('Filtering all records >= ' f'{current_timestamp}...\n')

    for position, line in enumerate(data):
        if not line.strip():
            continue

        timestamp_string = line.split()[0]
        timestamp_as_datetime = _get_datetime_instance_from_12_hours_format(
            timestamp_string
        )

        if timestamp_as_datetime >= datetime.now():
            if not filtered_records and (position > 0):
                filtered_records.append(data[position - 1])
                number_of_records += 1
            filtered_records.append(line)
        else:
            continue

        if len(filtered_records) == number_of_records:
            return filtered_records

    return filtered_records


def filter_input(parsed_args: argparse.Namespace):
    logging.info('Will filter for the next {args.number_of_records} records.')
    data = stdin.readlines()

    filtered_records = _filter_records(data, parsed_args.number_of_records)
    for record in filtered_records:
        stdout.write(record)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "number_of_records", type=int, help="show the next x records"
    )
    filter_input(parser.parse_args())
