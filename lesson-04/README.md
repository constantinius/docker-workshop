# Lesson 4 - Multi stage builds

In this lesson we will compile a simple C file, for which we will need some building tools. We don't want those tools to be in the final image though.

- Create a multi-stage Dockerfile
  - Start from a purposefully small base image (e.g: `debian:stable-slim`) as the first stage called `build-stage`
  - Add the `hello.c` and install build tools to compile C programs
    - To install on Debian: `apt-get update ; apt-get -y install gcc`
  - Compile the C file
    - Using `gcc`: `gcc hello.c`
    - By default this produces the `a.out` executable
  - Add a second stage using the same base image but called `run-stage`
  - Copy the compiled program from the `build-stage`
  - Set this program as the default command

- Build the image from the Dockerfile and tag it as `multi-hello`
- Run the image to see if it worked
