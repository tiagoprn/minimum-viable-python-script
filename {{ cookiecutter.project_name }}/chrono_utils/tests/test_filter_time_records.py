from datetime import datetime

import pytest
import time_machine

from chrono_utils.filter_time_records import (
    _filter_records,
    _get_datetime_instance_from_12_hours_format,
)


@pytest.mark.parametrize(
    'fake_current_datetime,hour,expected_datetime',
    [
        ['2021-01-01T08:00', '9:00am', '2021-01-01T09:00'],
        ['2021-01-01T08:00', '1:00pm', '2021-01-01T13:00'],
        ['2021-01-01T08:00', '12:00am', '2021-01-01T00:00'],
        ['2021-01-01T08:00', '12:00pm', '2021-01-01T12:00'],
    ],
)
def test_get_datetime_instance_from_12_hours_format(
    fake_current_datetime, hour, expected_datetime
):
    with time_machine.travel(fake_current_datetime, tick=False):
        datetime_instance = _get_datetime_instance_from_12_hours_format(hour)
        expected_datetime_instance = datetime.fromisoformat(expected_datetime)
        assert datetime_instance == expected_datetime_instance


@pytest.mark.parametrize(
    'fake_current_datetime,expected_filtered_records,number_of_records',
    [
        [
            '2021-01-01T00:00',
            ['5:00am 01', '7:59am 02', '8:00am 03', '8:01am 04', '1:00pm 05'],
            5,
        ],
        ['2021-01-01T05:00', ['5:00am 01'], 1],
        ['2021-01-01T05:00', ['5:00am 01', '7:59am 02', '8:00am 03'], 3],
        [
            '2021-01-01T05:00',
            ['5:00am 01', '7:59am 02', '8:00am 03', '8:01am 04', '1:00pm 05'],
            5,
        ],
        [
            '2021-01-01T08:00',
            ['7:59am 02', '8:00am 03', '8:01am 04', '1:00pm 05'],
            3,
        ],
        ['2021-01-01T13:59', ['1:00pm 05', '2:00pm 06'], 1],
        ['2021-01-01T13:59', ['1:00pm 05', '2:00pm 06'], 3],
        ['2021-01-01T13:59', ['1:00pm 05', '2:00pm 06'], 5],
        ['2021-01-01T14:00', ['1:00pm 05', '2:00pm 06'], 1],
        ['2021-01-01T14:00', ['1:00pm 05', '2:00pm 06'], 3],
        ['2021-01-01T14:00', ['1:00pm 05', '2:00pm 06'], 5],
        ['2021-01-01T14:01', [], 3],
    ],
)
def test_filter_records(
    fake_current_datetime, expected_filtered_records, number_of_records
):
    with time_machine.travel(fake_current_datetime, tick=False):
        records = [
            '5:00am 01',
            '7:59am 02',
            '8:00am 03',
            '8:01am 04',
            '1:00pm 05',
            '2:00pm 06',
        ]

        filtered_records = _filter_records(records, number_of_records)
        assert filtered_records == expected_filtered_records
