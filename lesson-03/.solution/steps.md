Start the container

```
$ docker run -v $(pwd)/html:/usr/share/nginx/html:ro -d -p 8000:80 nginx:alpine
10e0b735d72f31ad4fdfbf41f31860f0f2fb8274a7a5b3999ac77559e66124a2
```

List running containers

```
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                    NAMES
10e0b735d72f   nginx:alpine         "/docker-entrypoint.…"   58 seconds ago   Up 56 seconds   0.0.0.0:8000->80/tcp     tender_bassi
```

Pause container

```
$ docker pause 10e0b735d72f
10e0b735d72f
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED              STATUS                       PORTS                    NAMES
10e0b735d72f   nginx:alpine         "/docker-entrypoint.…"   About a minute ago   Up About a minute (Paused)   0.0.0.0:8000->80/tcp     tender_bassi
```

Resume container

```
$ docker unpause 10e0b735d72f
10e0b735d72f
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                    NAMES
10e0b735d72f   nginx:alpine         "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8000->80/tcp     tender_bassi
```

Stop the container

```
$ docker stop 10e0b735d72f
10e0b735d72f
$ docker ps -a
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS                        PORTS                    NAMES
10e0b735d72f   nginx:alpine         "/docker-entrypoint.…"   2 minutes ago    Exited (0) 5 seconds ago                               tender_bassi
```

Delete the container

```
$ docker rm 10e0b735d72f
10e0b735d72f
```

Run a named container that automatically gets deleted when stopped:

````
$ docker run -v $(pwd)/html:/usr/share/nginx/html:ro -d -p 8000:80 --name web-server --rm nginx:alpine
3ef370c5c8ba8bc890f014b9205840952edee232a2dc20354dd2da271d6578d6
```

List it:

```
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS        PORTS                    NAMES
1d3a3b6808fb   nginx:alpine         "/docker-entrypoint.…"   3 seconds ago   Up 1 second   0.0.0.0:8000->80/tcp     web-server
```

Confirm it is deleted, when stopped:

```
$ docker stop web-server
web-server

$ docker ps -a | grep web-app
```