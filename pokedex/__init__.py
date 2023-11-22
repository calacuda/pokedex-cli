import os
from pathlib import Path

# resource_path = os.path.join(os.path.split(__file__)[0], "resources")
resource_path = os.path.join(os.path.expanduser("~/.cache/pokedex"), "resources")
Path(resource_path).mkdir(parents=True, exist_ok=True)
