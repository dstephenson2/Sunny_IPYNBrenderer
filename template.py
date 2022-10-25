import os
from pathlib import Path # path to make our os independent; basis the os paths it will be configured; say like if it is bash it wil use forward slash whle in command prompt it is backward slash
import logging # helps us to log each activity and also in debugging

logging.basicConfig(
    level=logging.INFO, # prints all the data that we need
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"source/{project_name}/__init__.py", # __init__.py is required to import the directory as a package, and should be empty.
    # example.py is an example of a module within the package that could contain the logic (functions, classes, constants, etc.) of your package
    f"tests/__init__.py", 
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py", 
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini", # python packages also need to be tested 
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created a file: {filepath} at path: {filepath}")
    else:
        logging.info(f"file is already present at : {filepath}")
