# detect_stream

PREREQUISITES:</br>
This has been developed on MacOS and has not been properly tested on Windows or Linux. There have been reports of this working Windows 11, but I am not aware of the details involved.</br>

Use pip to install the following the libraries:</br>
`pip install cv2-python pafy youtube-dl`</br>

An error will pop up pointing to <something>/site-packages/pafy/backend_youtube_dl.py and dislikes. </br>

Edit the file it points you to, look for the line that starts with dislikes... and comment it out (change to #dislikes...). Save the file and everything should load proper.</br>

RUNNING:</br>
```
$ python3 ./MoDe.py -s http://youtube.com/XYZABCUVW -q 1 -o /Users/UserName/Pictures/

usage: MoDe.py [-h] [-c CODEC] [-q QUAD] [-s SOURCE] [-t THREADING]
               [-v VERBOSE] [-C CONTOURAREA] [-D DELTA] [-g GAUSSIANBLUR]
               [-o OUTDIR]

To Enable QUADrants, THREADING, VERBOSE set VALUE to 1

optional arguments:
  -h, --help            show this help message and exit
  -c CODEC, --codec CODEC
                        x264 mpv4 divx
  -q QUAD, --quad QUAD  Enable Quadrant Splitting
  -s SOURCE, --source SOURCE
                        http YouTube URL or File Path
  -t THREADING, --threading THREADING
                        Enable Threading
  -v VERBOSE, --verbose VERBOSE
                        Enable Verbose
  -C CONTOURAREA, --contourarea CONTOURAREA
                        Define contourArea
  -D DELTA, --delta DELTA
                        Define Sensitivity Delta
  -g GAUSSIANBLUR, --gaussianblur GAUSSIANBLUR
                        Define gaussianBlur value
  -o OUTDIR, --outdir OUTDIR
                        Directory to save clips/captures
```
</br>
Changing detection variables:</br>
Gaussian Blur: g will decrease blur, G will increase blur</br>
Delta    : d will decrease delta, D will increase delta</br>
contourArea  : c will decrease contourArea, C will increase contourArea</br>
             : < will decrease contourArea by 200, > will increase contourArea by 200 (Tutorials started it at 10000 but low numbers helped box small objects)</br>
Hide Display : h will hide and unhide the detection variables</br>

PLAYBACK CONTROLS:</br>
Pause (p)</br>
unpause (anykey)</br>
save image (s)</br>
save video clip (S) Recording begins -30s from when you push S</br>
exit recording (x)</br>
