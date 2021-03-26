# Lesson 5 - Entrypoint vs Command

In this lesson we explore the usage of an entrypoint.

## A: Entrypoint to use for set-up or tear-down tasks

- For sake of simplicity we use Python for our entrypoint and use `python:3.8` as our base image
- Create an `entrypoint.py` file, that prints something before and after the actual command, while running the command in between
  - Hint: the command is passed in `sys.argv`, but the first `argv` is the `entrypoint.py` itself
- Add this file to the image and set the entrypoint to `python3 entrypoint.py`
- Build and run this image to see if it worked

## B: Entrypoint to use as a default command

- Start from any base image of your choice (e.g: `ubuntu:20.04`)
- Set the built-in command `ls` as your entrypoint
- Set the default command to the `-a` option to list all files/directories
- Build the image and tag it as `entrypoint-b`
- Run the image with default options
- Run the image using specific options (e.g: `-lisah`, which prints much more information)

