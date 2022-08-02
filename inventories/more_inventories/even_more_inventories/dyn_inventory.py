#!/usr/bin/env python
from argparse import ArgumentParser
import json

inventory = {
    'group_seven': {
        'hosts': (
            (
                [f'group_seven_host_0{i}' for i in range(1, 6)]
                + [f'group_seven_and_eight_host_0{i}' for i in range(1, 6)]
            )
            + [f'group_seven_eight_and_nine_host_0{i}' for i in range(1, 6)]
        ),
        'vars': {'is_in_group_seven': True},
    },
    'group_eight': {
        'hosts': (
            (
                (
                    [f'group_eight_host_0{i}' for i in range(1, 6)]
                    + [f'group_seven_and_eight_host_0{i}' for i in range(1, 6)]
                )
                + [f'group_eight_and_nine_host_0{i}' for i in range(1, 6)]
            )
            + [f'group_seven_eight_and_nine_host_0{i}' for i in range(1, 6)]
        ),
        'vars': {'is_in_group_eight': True},
    },
    'group_nine': {
        'hosts': (
            (
                [f'group_nine_host_0{i}' for i in range(1, 6)]
                + [f'group_eight_and_nine_host_0{i}' for i in range(1, 6)]
            )
            + [f'group_seven_eight_and_nine_host_0{i}' for i in range(1, 6)]
        ),
        'vars': {'is_in_group_nine': True},
    },
    'all': {'vars': {'ansible_connection': 'local', 'inventories_var': True}},
    'ungrouped': {'hosts': [f'ungrouped_host_{i}' for i in range(11, 16)]},
    '_meta': {
        'hostvars': {
            'group_seven_host_01': {'group_seven_host_01_has_this_var': True},
            'group_eight_host_01': {'group_eight_host_01_has_this_var': True},
            'group_nine_host_01': {'group_nine_host_01_has_this_var': True},
        }
    },
}

def dumps(dct):
    return json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()


def load_inventory():
    args = parse_args()
    if args.list_instances:
        print(dumps(inventory))


if __name__ == '__main__':
    load_inventory()
