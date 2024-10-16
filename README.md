###
Ive created this as a fork because I cant find how to add a comment ! 
Ive finally got the python to work again . the new versions (2024)  of python only works with the new version of scipy which for 
some reason doesnt have the functions that the python wizard needs.
you can get both on the python and scipy websites

You need to download and install   python 3.7.6 (32 bit) 
then you download an old version of SCIPY  (from 2020) 1.2.2 seemed to work for me
then in cmd window you change directory or folder to downloads (cd downloads) and type 
pip install [the whole filename inclding the .whl eg  scipy-1.2.2-cp37-cp37m-win32.whl ] for the scipy download 
then hopefully the bloody thing will work again! 

May add this advice to the main readme in the main repository 












- Added "lpcplayer" package (based on talkie) to support Play feature in GUI. 

- Added dirty support for other LPC coding tables. TMS5100 is default now.
  ```
    -T {tms5220,tms5100}, --tablesVariant {tms5220,tms5100}
                          Tables variant
  ```                        

- Support for python formatted output
  ```
    -f {arduino,C,hex,python}, --outputFormat {arduino,C,hex,python}
                          Output file format
  ```
- Small fixes and enhancements in GUI



------
This project is a python port of the great macOS tool BlueWizard (https://github.com/patrick99e99/BlueWizard), which is written in objective C and I was not familiar enough with this C dialect to make an portable command line application out of it.

It is intended to convert (voice) audio streams into LPC bitstreams used in the TMS 5220 chip or e.g. in the Arduino library Talkie. Now you can generate your own LPC streams and make your chips say the things you want them to.

Compared to BlueWizard some minor features have been added:
1. Ability to downsample a wave file automatically
2. Automated output formatters for C, Arduino (C-Dialect) and plain hex

Prerequisites:
- Python 2.7
- SciPy >= 0.18.1

Usage: 
```
       python_wizard.py [-h] [-u UNVOICEDTHRESHOLD] [-w WINDOWWIDTH] [-U] [-V]
                        [-S] [-p] [-a PREEMPHASISALPHA] [-d] [-r PITCHRANGE]
                        [-F FRAMERATE] [-m SUBMULTIPLETHRESHOLD]
                        [-f {arduino,C,hex}]
                        filename

positional arguments:
  filename              File name of a .wav file to be processed

optional arguments:
  -h, --help            show this help message and exit
  -u UNVOICEDTHRESHOLD, --unvoicedThreshold UNVOICEDTHRESHOLD
                        Unvoiced frame threshold
  -w WINDOWWIDTH, --windowWidth WINDOWWIDTH
                        Window width in frames
  -U, --normalizeUnvoicedRMS
                        Normalize unvoiced frame RMS
  -V, --normalizeVoicedRMS
                        Normalize voiced frame RMS
  -S, --includeExplicitStopFrame
                        Create explicit stop frame (needed e.g. for Talkie)
  -p, --preEmphasis     Pre emphasize sound to improve quality of translation
  -a PREEMPHASISALPHA, --preEmphasisAlpha PREEMPHASISALPHA
                        Emphasis coefficient
  -d, --debug           Enable (lots) of debug output
  -r PITCHRANGE, --pitchRange PITCHRANGE
                        Comma separated range of available voice pitch in Hz.
                        Default: 50,500
  -F FRAMERATE, --frameRate FRAMERATE
  -m SUBMULTIPLETHRESHOLD, --subMultipleThreshold SUBMULTIPLETHRESHOLD
                        sub-multiple threshold
  -f {arduino,C,hex}, --outputFormat {arduino,C,hex}
                        Output file format
```

