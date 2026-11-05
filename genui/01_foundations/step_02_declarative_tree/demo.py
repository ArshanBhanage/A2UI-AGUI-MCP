import json
from catalog import validate_tree
from stream import IncrementalJSON

SAMPLE={"type":"Stack","props":{"direction":"column"},"children":[{"type":"Metric","props":{"title":"Open issues","value":"12"}}]}
parser=IncrementalJSON()
for chunk in [json.dumps(SAMPLE)[:25],json.dumps(SAMPLE)[25:]]:
    partial=parser.feed(chunk); print("partial=", partial is not None)
validate_tree(partial); print("validated declarative tree:", json.dumps(partial))

