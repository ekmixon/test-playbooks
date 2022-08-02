#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from datetime import datetime

# This is a useful script to determine what happens on an inventory import
# when the contents change. By using a timestamp, we should force the values
# herein to change every time the sync is done.
#
# There are 2 examples
#  - demonstrate new / old hosts by changing the hostname returned each time
#         which is relevant to `overwrite`
#  - demonstrate `overwrite_vars` by including 2 sub-examples
#      - variable changes its name on every import
#      - variable changes its value on every import


time_val = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S.%f')

moover = f"moover-{time_val}"

print(
    json.dumps(
        {
            "_meta": {
                "hostvars": {
                    "change_of_vars": {
                        "static_key": f"host_dynamic_{time_val}",
                        f"dynamic_{time_val}": "host_static_value",
                    },
                    moover: {"static_var": "static_value"},
                }
            },
            "all": {
                "vars": {
                    "static_inventory_key": f"inventory_dynamic_{time_val}",
                    f"dynamic_{time_val}": "inventory_static_value",
                }
            },
            "group_with_moover": {"hosts": ["change_of_vars", moover]},
            "group_with_vars": {
                "hosts": ["change_of_vars"],
                "vars": {
                    "static_group_key": f"group_dynamic_{time_val}",
                    f"dynamic_group_{time_val}": "group_static_value",
                },
            },
            "ungrouped": {"hosts": [moover, "change_of_vars"]},
        }
    )
)