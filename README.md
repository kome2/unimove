# unimove  
unimove is a script that can create composite image of movement objects' trajectory extracted from movie.  
  
It requires the following environments.  
* Python 3.5 or more
* OpenCV 3.4.3 or more (https://github.com/opencv/opencv)
* OpenCV_contrib (https://github.com/opencv/opencv_contrib)

unimoveは、定点撮影の動画から動体を抽出し、その移動軌跡の合成画像を生成するスクリプトである。  
  
動作確認環境は以下のとおりである。  
* Python 3.5 or more
* OpenCV 3.4.3 or more (https://github.com/opencv/opencv)
* OpenCV_contrib (https://github.com/opencv/opencv_contrib)

# How to use (使い方)
  
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
  
  
実行中にqをタイプすることでスクリプトは停止する。  
また生成中の画像を出力したいときは、実行中にwをタイプすることで、その瞬間の画像をスクリプトファイルを同じ階層に出力できる。


# Contact
kome@hongo.wide.ad.jp
