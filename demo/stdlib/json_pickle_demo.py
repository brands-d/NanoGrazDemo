import json, pickle

data = {"name": "NanoGraz", "version": 1.0}

json.loads(json.dumps(data))
pickle.loads(pickle.dumps(data))
