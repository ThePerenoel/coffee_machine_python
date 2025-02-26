
# Kata Coffee Machine

This is an iteration of kata coffee machine (https://simcap.github.io/coffeemachine/) in plain **Python**. This app was coded according to hexagonal architecture principle. It has a CLI in order to execute the code and allow you to play with it.



## Run Locally

Clone the project

```bash
  git clone https://github.com/ThePerenoel/coffee_machine_python.git
```

Go to the project directory

```bash
  cd coffee_machine_python
```

Create virtural environment

```bash
  python -m venv .venv
```

Activate your virtural environment

```bash
  source .venv/bin/activate
```

Start the app

```bash
  python -m src.main
```


## Running Tests

To run tests, run the following command in the project root directory

```bash
  python -m unittest discover tests/
```

## How to use it

If you want to use the application (usescases + domain) in order to implement your own coffee machine, simply extend the usecases and implement the repositories and providers.  
