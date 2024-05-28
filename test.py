from pygr.runner import Runner
from pygr.definition import Definition
import json

with open("package_template.json") as f:
    definition = f.read()

definition = json.loads(definition)
Runner(Definition(definition)).run_definition()
