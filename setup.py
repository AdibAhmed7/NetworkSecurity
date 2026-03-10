# Import find_packages and setup functions from setuptools
# setuptools is used to package and distribute Python projects
from setuptools import find_packages, setup

# Import List type for type hinting
# This helps indicate that the function returns a list of strings
from typing import List


# Function to read requirements from requirements.txt
def get_requirements() -> List[str]:
    """
    This function reads the requirements.txt file
    and returns a list of required libraries.
    """

    # Create an empty list to store all the dependencies
    requirement_lst: List[str] = []

    try:
        # Open the requirements.txt file in read mode
        with open('requirements.txt', 'r') as file:

            # Read all lines from the file
            # Each line represents a dependency
            lines = file.readlines()

            # Process each line in the requirements file
            for line in lines:

                # Remove extra spaces and newline characters
                requirement = line.strip()

                # Ignore empty lines and "-e ." entry
                # "-e ." is used for editable installation in development
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    # If requirements.txt does not exist, print an error message
    except FileNotFoundError:
        print("requirements.txt file not found")

    # Return the final list of dependencies
    return requirement_lst


# Print the list of requirements (mainly for testing/debugging)
print(get_requirements())


# setup() function defines metadata and configuration for your project
setup(
    # Name of the Python package/project
    name="NetworkSecurity",

    # Version of the package
    version="0.0.1",

    # Author name
    author="Adib Ahmed",

    # Author email address
    author_email="adibahmed0425@gmail.com",

    # Automatically find all packages (folders containing __init__.py)
    packages=find_packages(),

    # Install required dependencies automatically from requirements.txt
    install_requires=get_requirements()
)