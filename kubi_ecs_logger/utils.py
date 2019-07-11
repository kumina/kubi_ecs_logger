import json
import sys


def pprint(data: dict, output_destination=sys.stdout):
    print(json.dumps(data, indent=2, sort_keys=True), file=output_destination)
