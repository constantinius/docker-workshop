Building the image

```
docker build . -t entrypoint-b
```

Run with default parameters

```
$ docker run -it --rm entrypoint-b
.  ..  .dockerenv  bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

Running with non-default parameters

```
$ docker run -it --rm entrypoint-b -lisah
total 56K
 538003 4.0K drwxr-xr-x   1 root root 4.0K Mar 26 13:03 .
 538003 4.0K drwxr-xr-x   1 root root 4.0K Mar 26 13:03 ..
 538001    0 -rwxr-xr-x   1 root root    0 Mar 26 13:03 .dockerenv
2373514    0 lrwxrwxrwx   1 root root    7 Nov  6 01:21 bin -> usr/bin
2373515 4.0K drwxr-xr-x   2 root root 4.0K Apr 15  2020 boot
5038000    0 drwxr-xr-x   5 root root  360 Mar 26 13:03 dev
 537994 4.0K drwxr-xr-x   1 root root 4.0K Mar 26 13:03 etc
2373920 4.0K drwxr-xr-x   2 root root 4.0K Apr 15  2020 home
2373921    0 lrwxrwxrwx   1 root root    7 Nov  6 01:21 lib -> usr/lib
2373922    0 lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib32 -> usr/lib32
2373923    0 lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib64 -> usr/lib64
2373924    0 lrwxrwxrwx   1 root root   10 Nov  6 01:21 libx32 -> usr/libx32
2373925 4.0K drwxr-xr-x   2 root root 4.0K Nov  6 01:21 media
2373926 4.0K drwxr-xr-x   2 root root 4.0K Nov  6 01:21 mnt
2373927 4.0K drwxr-xr-x   2 root root 4.0K Nov  6 01:21 opt
      1    0 dr-xr-xr-x 144 root root    0 Mar 26 13:03 proc
2373929 4.0K drwx------   2 root root 4.0K Nov  6 01:25 root
2493636 4.0K drwxr-xr-x   1 root root 4.0K Nov 25 22:25 run
2373936    0 lrwxrwxrwx   1 root root    8 Nov  6 01:21 sbin -> usr/sbin
2373937 4.0K drwxr-xr-x   2 root root 4.0K Nov  6 01:21 srv
      1    0 dr-xr-xr-x  13 root root    0 Mar 25 16:56 sys
2373939 4.0K drwxrwxrwt   2 root root 4.0K Nov  6 01:25 tmp
2493621 4.0K drwxr-xr-x   1 root root 4.0K Nov  6 01:21 usr
2493625 4.0K drwxr-xr-x   1 root root 4.0K Nov  6 01:25 var
```
