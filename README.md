# unimove  
unimove is a script that can create composite image of movement objects' trajectory extracted from movie.  
  
It requires the following environments.  
* Python 3.5 or more
* OpenCV 3.4.3 or more (https://github.com/opencv/opencv)
* OpenCV_contrib (https://github.com/opencv/opencv_contrib)

# How to use
  
```
usage: unimove.py [-h] [-f FRAME] [-s START] input  

positional arguments:  
input                   Absolute/relative path to input file  

optional arguments:  
-h, --help  
                        show this help message and exit  
-f FRAME, --frame FRAME  
                        Number of interval frame  
-s START, --start START  
                        Time of union start  
```

When you execute this script, it creates a composite image of movement objects' trajectory.  
  
During the script execution, you can stop the script when you press 'q'.   
Moreover, you can output the composite image of that moment into the same directory of this script when you press 'w'.  
  
# Sample  
Input movie  
![Input](https://github.com/kome2/unimove/raw/master/img/sample.gif)  
  
Output Image  
![Output](https://github.com/kome2/unimove/raw/master/img/sample.jpg)  

# Refrence 
日本語記事はこちら   
https://www.komee.org/entry/2018/10/27/120000  

# Contact
kome@hongo.wide.ad.jp
