from setuptools import setup, find_packages

setup(
    name="coffee_machine_core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "parameterized",
    ],
    author="Loic NOEL",
    description="Iteration of coffee machine made in plain Python code. No framework.",
    url="https://github.com/ThePerenoel/coffee_machine_python.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
