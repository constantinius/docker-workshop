# Lesson 3 - Volumes and Container interaction

In this lesson we will learn how to use volumes to mount data into a container. We will also start the container in detached mode in order to later interact with it.

## Volumes

- Start the `nginx:alpine` image with the following parameters
  - Mount the `html` directory to the internal directory nginx serves its files from (`/usr/share/nginx/html`)
  - Map the exposed port (`80`) to another port that does not require privileges (e.g: `8000`)

- Bonus points
  - You can never be too safe: mount the `html` directory in read-only mode

## Basic container interactions

- Access the running container via a browser
- List the running container and note its container ID
- Pause that container
  - Show the container details to see that it is indeed paused
  - Test using the browser
- Resume that container
  - Show the container details to see that it is again running
  - Test using the browser
- Stop that container
  - Show the container details to see that it is stopped
- Delete the container
  - Show the container details to see that it is indeed removed

## Named containers

- Start the `nginx:alpine` image again with the same parameters, but this time give it the name `web-server`
- Again list the images
- Stop and cleanup the container

- Bonus points
  - Cleaning up every single container when it is stopped is a chore. We would like to have them deleted when they are stopped.
