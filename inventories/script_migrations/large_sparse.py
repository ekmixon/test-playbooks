#!/usr/bin/env python
import json
import os


Ng = int(os.environ.get("NUM_GROUPS", 25))
Nh = int(os.environ.get("NUM_HOSTS", 25))


data = {"_meta": {"hostvars": {}}}

for i in range(Nh):
    data.setdefault("ungrouped", []).append(f"Host-{i}")

for i in range(Ng):
    data[f"Group-{i}"] = {"vars": {"foo": "bar"}}

print(json.dumps(data, indent=2))
