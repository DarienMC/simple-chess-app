"""
The constant.py module acts as a global constants class for the simple-chess-app project.
It loads user-defined parameters from the project's config.toml file and maps them to Python constants.
It then defines any other constant required for this project.
Notes:
    It was determined that doing this was OK for the scope of this project to avoid "magic numbers".
    However, for larger project, consider managing constants smartly to avoid maintainability problems.
    *Large* global constants classes are considered to be an anti-pattern.
"""

import toml
from pathlib import Path

# Assume config.toml is in the project's root directory
# Assume constants.py is in the project's source directory
__root_dir = Path(__file__).absolute().parent.absolute().parent

# import user-defined constants within config.toml file
with open(__root_dir / 'config.toml') as file:
    __config = toml.load(file, _dict=dict)

# high-level user-defined information and toggled options
VERSION = __config['version']
