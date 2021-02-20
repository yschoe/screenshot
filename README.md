# screenshot

Simple python script that runs in the background and takes screenshot and saves to a file automatically, with time stamp. 

You can specify the file prefix and destination path. 

In the script, change the path variable:

```
path = "C:/Users/username/Pictures/"
```

To specify the file prefix, provide the info in the command line argument

```
./screenshot.py prefix 

or

python screenshot.py prefix
```

While the script is running, press [PrtScr] and the file will be saved like below:

```
C:/Users/username/Pictures/prefix-2021-02-19-21-56-00.png
```
