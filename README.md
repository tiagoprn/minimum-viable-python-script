# minimum-viable-python-script

This project is a minimalistic template that can be used as a base to develop a simple python script that interacts with stdin to take part e.g. on shell pipes.


## Features

- A Makefile to wrap the most common operations and ease development with commands to run the script and develop using test, apply formatters, run linters and tests, etc...

- There is no third-party library dependency (except for development ones), so that you can run your script standalone if you wish.

- python 3.x

- poetry as the package manager

- pylint as the linter, black as the code formatter, isort to fix import order

- pytest tests, with some plugins to ease presentation.

- coverage report.


## How to use this cookiecutter

- Install cookiecutter on your distribution (e.g. Ubuntu):

`$ sudo apt install cookiecutter`

- If you want to clone this repository locally to run the cookiecutter also locally:

```
$ mkdir -p ~/cookiecutters
$ cd ~/cookiecutters
$ git clone  https://github.com/tiagoprn/minimum-viable-python-script
```

- Enter the folder where your want to create your script locally:

```
cd ~/projects/
```

- Run the cookiecutter from the local copy:

`$ cookiecutter ~/cookiecutters/minimum-viable-python-script`

... or directly from github (recommended):

`$ cookiecutter gh:tiagoprn/minimum-viable-python-script`

It will ask some questions with sane defaults, and then will generate a folder with the value you
indicated for `project_slug`. Congratulations, this is your new minimal flask project! :)

- Enter the project directory:

`$ cd ~/projects/your-project_slug`

- Create a local git repository to bootstrap version control:

```
$ git init
$ git add .
$ git commit -m 'Boostrapping project.'
```

- From then on, follow the instructions on `README.md` so that you can setup the development environment.

