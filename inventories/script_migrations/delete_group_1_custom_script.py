#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import uuid

unique_name = str(uuid.uuid4())
host_1 = f"host_{unique_name}"
host_2 = f"host_2_{unique_name}"
print(
    json.dumps(
        {
            "_meta": {
                "hostvars": {
                    f"{host_1}": {"name": f"{host_1}"},
                    f"{host_2}": {"name": f"{host_2}"},
                    "all_have": {"name": "all_have"},
                    "all_have2": {"name": "all_have2"},
                    "all_have3": {"name": "all_have3"},
                }
            },
            "child_group2": {"hosts": [f"{host_1}", "all_have2"]},
            "parent_group": {
                "hosts": [f"{host_2}", "all_have3"],
                "children": ["child_group2"],
            },
        }
    )
)
