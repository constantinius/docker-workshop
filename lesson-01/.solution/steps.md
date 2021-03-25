Build the image

```
$ docker build . -t hello-world
Sending build context to Docker daemon  6.144kB
Step 1/3 : FROM ubuntu:20.04
 ---> f643c72bc252
Step 2/3 : ADD hello.sh .
 ---> 455afd8d24b4
Step 3/3 : CMD ./hello.sh
 ---> Running in ebb362e8b362
Removing intermediate container ebb362e8b362
 ---> 4f58b60d9fce
Successfully built 4f58b60d9fce
Successfully tagged hello-world:latest
```

Run the image in a container

```
$ docker run hello-world
Hello World
```
