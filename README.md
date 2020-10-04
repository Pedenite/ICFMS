# ICFMS

Use: `python3 icfms.py file1.jpg file2.png file3.ppm ...`

Program gets image files as arguments and converts it to .ppm format using image-magik from linux (works only on linux, unless the file is already on .ppm format). The images are then, processed to cut out white spaces off the right side and bottom of them.

###### Does not work if there are relatively big white spaces to the left or top (yet)
