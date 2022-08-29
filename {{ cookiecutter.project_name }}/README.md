# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setting up the development environment

1. Make sure you have pyenv installed. If not, install it.

2. Install pipx on your python distribution using the system's installed python (generally python3). With pipx you can install python utilities on isolated environments, which fits perfectly to install poetry. To install it: `sudo pip3 instal pipx`

3. After installing pipx, run: `pipx install poetry`

4. Create and enter a folder with the project's name, where you will use pyenv to define the python version that will be used by poetry to automatically create the virtualenv:
```bash
pyenv local 3.9.1
```

5. Clone this repository with git clone

6. Enter the cloned repository folder

7. Run the following commands to setup the development environment:

```bash
make shell
make requirements
```

8. To validate the development environment is working, run the commands below:

```bash
$ make style-check
$ make lint
$ make test
$ make run
```


# Notes

- To supress "Entering Directory" messages when running make commands, run the command with `make -s` ("-s" means "silent"). e.g.: `make -s run`

- To understand a little more about poetry, you can check [this note](https://tiagopr.nl/posts/published/using-poetry-for-dependencies-on-python-projects/).

