# chrono-utils

## filter

Given timestamped records on stdin, prints on stdout the ones that will happen in the near future, taking the current timestamp as a reference.

[Here](https://github.com/tiagoprn/chrono-utils/blob/88f7df6cd61df7a2afd3f7932acde41c95e95001/Makefile#L49) is an example on how to use it. Check also [tests for more scenarios](https://github.com/tiagoprn/chrono-utils/blob/master/chrono_utils/tests/test_filter_time_records.py).

You can use the main script standalone on any python3 installation, since it does not require any third party dependency. To do that, you can simply download it with curl:

```
curl https://raw.githubusercontent.com/tiagoprn/chrono-utils/master/chrono_utils/filter_time_records.py -o filter_time_records.py
```

# Setting up the development environment

1. Make sure you have pyenv installed. If not, install it.

2. Install pipx on your python distribution using the system's installed python (generally python3). With pipx you can install python utilities on isolated environments, which fits perfectly to install poetry. To install it: `sudo pip3 instal pipx`

3. After installing pipx, run: `pipx install poetry`

4. Create and enter a folder with the project's name, where you will use pyenv to define the python version that will be used by poetry to automatically create the virtualenv: `pyenv local 3.9.1`

5. Clone this repository with git clone

6. Enter the cloned repository folder

7. Run the following commands to setup the development environment:

```
make shell
make requirements
```

# Notes

- To supress "Entering Directory" messages when running make commands, run the command with `make -s` ("-s" means "silent"). e.g.: `make -s run`

- To understand a little more about poetry, you can check [this note of mine](https://tiagopr.nl/posts/published/using-poetry-for-dependencies-on-python-projects/).

