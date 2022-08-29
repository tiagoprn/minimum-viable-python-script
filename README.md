# minimum-viable-python-script

This project is a minimalistic template that can be used as a base to develop a simple pure python script to run on the CLI.


## Features

- A Makefile to wrap the most common operations and ease development with commands to run the script and its' tests, apply formatters, run linters, tests, etc...

- There is no third-party library dependency (except for development ones), so that you can run your script standalone if you wish.

- python 3.10

- poetry as the package manager

- pylint as the linter, black as the code formatter, isort to fix import order

- pytest tests, with some plugins to ease presentation.

- coverage report.


## How to use this cookiecutter

- Install cookiecutter on your distribution (e.g. Ubuntu):

`$ sudo apt install cookiecutter`


- Enter the folder where your want to create your script locally:

`$ cd ~/projects/`

- Run the cookiecutter from github (recommended):

`$ cookiecutter gh:tiagoprn/minimum-viable-python-script`

It will ask some questions (which have default values, case you are on a hurry) and generate a folder with the value you indicated for `project_slug`. Congratulations, this is your new minimal python project! :)

- Enter the project directory:

`$ cd ~/projects/your_project_slug`

- Create a local git repository to bootstrap version control:

```
$ git init
$ git add .
$ git commit -m 'Boostrapping project.'
```

- From then on, follow the instructions on `README.md` so that you can setup the development environment.

