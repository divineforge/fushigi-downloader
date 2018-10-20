# Synopsis

Download scan from the web site http://doraemon.mangawiki.org/

# Usage
```
usage: fushigi.py [-h] --manga MANGA --chapter CHAPTER [--start START] --end END

Fushigi Downloader

optional arguments:
  -h, --help            show this help message and exit
  --manga MANGA, -m MANGA
                        Manga to download
  --chapter CHAPTER, -c CHAPTER
                        Chapter to download
  --start START, -s START
                        Page to start download
  --end END, -e END     Page to end download
```

The manga, chapter and page argument can be found in the site url with the arguments of the same name

# Example

Download the second chapter of raw doraemon scans

the URL is:

 http://doraemon.mangawiki.org/read-manga/index.php?manga=Doraemon-Manga-Raw&chapter=Doraemon_Vol_02_RAW&page=1

The command line is:
```sh
python fushigi.py -m Doraemon-Manga-Raw -c Doraemon_Vol_02_RAW -s 1 -e 192
```

# Tips

straighten images

The scans on mangawiki are good, but a little skew.

As a post process after download I recommend to use image magic deskew function

 for i in *.jpg; do echo $i; convert -deskew 40% -set option:deskew:auto-crop 10 $i deskew_$i;done


___


## Python3 Virtualenv Setup

Added Guide from here
https://gist.githubusercontent.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3/raw/3013691801f5707624e7ec84bfdd6cfc06037c25/Python3%2520Virtualenv%2520Setup.md

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:
```bash
$ virtualenv -p python3 <desired-path>
```

Activate the virtualenv:
```bash
$ source <desired-path>/bin/activate
```

Deactivate the virtualenv:
```bash
$ deactivate
```


[About Virtualenv](https://virtualenv.pypa.io/en/stable/)