# NoitaDecode

This project is meant to provide tools exploring the Noita's eye enigma

It as been written in Python 3.7
It consists actually of a main script which crop each symbol from an image message

To execute the script, install the requirements from requirements.txt then run main.py

After execution you'll find:
- the cropping map in the project root folder
![Cropping map](https://i.postimg.cc/fMPRLwTc/E1.png)
- A folder with your tokens in the Out folder. Each token is named as "line_column_pattern.png" to provide easy data manipulation for later use
![Tokens](https://i.postimg.cc/XJ7zfRcT/Capture.jpg)
- A PatternChecker folder in the Out folder to help identifying pattern recognition issues
- Patterns are identified as :
  - N for North
  - S for South
  - O for Ouest (Well, I've just realized my mistake here ^^)   
  - E for East
  - C for Center

I didn't took that much time to clean the code, so it's actually some kind of a mess. I apologies for that. It will be better in a few times.
I'm open to feedback and pool request ;).

## What's next ?

As discussed by the community, the next goal of this project is to provide methods to handle eyes figures as triangles and try and provide tooling for different computation and deciphering methodologies.
![Triangles](https://i.postimg.cc/QsZw3RsH/graphic-design-is-my-passion2.png?dl=1)

## Data processed :

- East 1:

E C N C N S E E S S C O C O N N S C E S E N N O S N S C S S C C O C E O C C C 
C S E C O N E E C C C N O E E E O E N E E E E C N N C C C S E C N S O N N N S 
S N C E E N C O O C C C E C C N C O C O C N O O N O E C S S C E E C S O E O N 
E S N S N S N S C C S N N S E N E C N O E E S N S S N O O N S O N O O N E N N 
C N O C C S E N E N N O N S C C O N N N C N C C E O N E O N C C O C S N C C N 
C O C S S N O S E S O N N E E N C N C N C C O C N E C O N E O O E O O E O C E 
N S S S N E E C S S C N C S N N S N N N E N N E N C S E E S N O 
N S N C O E O E E O N S C S C O N N C E C S N E S E C O S N S 

- East 2:

N E N C N S E E S S C O C O N N S C E S E N N O S N S C S S C C O C E O C C O 
N S E C O N E E C C C N O E E E O E N E E E E C N N C C C S E C N S O N N S E 
S C E C N S E S C C O O E N C N O S C C N E N O N O C S N N C E O N C O E E S 
N C E O O N N N S E E E E S N O C S S S C N S C E S N C N C S E E O O N O E E 
C N O N N S C S C N O O N C E C E C S N N N N O E O N C S O E S E N S E N N E 
N O N N E C N E C C O C N C S C E E N E E O C E C O C C C C N C S E E N C O C 
C C N N S E E N C C O E E S N C O S E O E C N S N C S C N C E C C S C C E E N 
C E C N O E E O C S N E C S N S S C E S N C C C N C S S N C O O N E C N O E E 
C S O E C N C O S N C N N C C E C C N E O 
N S N O C E C E E C E C N O N S E E S N N 

- East 3:

E E N C N O S C O C C C N C C S C E E E C E S N E E E E S E N O O N O O E N N 
S S E C O N C C E E E E O S N S O N C C S E O E C C C C N C E E C C O E O S N 
S N S E E S S N E N E C N S O C C O N O N S C E S N C C C N E S N C O S N S C 
C E C C E C N O C C C E C E N E N E S N N N C C C C S N N E E E C N N C C S E 
N O C E N O E E E C E S C O E C C N E N O E O N E N N E E S N C O C N C C S O 
C C S C E N C S N S C C E N E E N C S N C C C C S N E S S E C C S E O C O E E 
C C N E O C E O N C E C E S E C O S C O S C S N E E O N S N S N E S C N N O E 
E S E S N N N S C E N N C E N C E C E E E S O N O N E N N S E O C S E N E S C 
C C N C S C N E O E E N E E O C S S C C S E N N C E O E N S N S S E S N C C N 
O N C E N C N C S S C C O S E C S N O N E N N N O E E S S C O C S O C C C O N 
C O N E O C N E S C O 
C O E S C N C N C O 

- East 4:

N C N C N O S C O C C C N C C C C C C N C E N S E S S N E C N O E N S S C C S 
E S E C O N C C E E E E O S N E N E O S C O S C S C C N N C E C S O E N N S C 
N C N C C O E E S E N C C S O S C C N O O E N O E E O C E E E C C S C C C E E 
S C S O N N C E E S N S E C E O C S S C E C S C E E E O O N N O E C N C N O N 
N O S E S O S C C N E C E O E E S C N N C S C N S C E C C N C O C C S C N S C 
C N E S S E O C N S O N S O N S C E O O N S C N O N E O N E E E E S C S S E E 
E N E E E E N O S N S C S C E C N S N C E N N S N C E E S C C C S N C S E S E 
O S E S S N O N N C S E O C S E C C N E E N C S N N E O S N O O C N E C E S N 
N E E C E O E S C N C N S N N E S E E N S C S 
S O E N E N C E E C N C C S E S C S O C S O 

- East 5:

N N N C N O S C O C C C N C C C C C C N C E N S E S S N E C N O S C O O N S S 
S S E C O N C C E E E E O S N E N E O S C O S C S C C N N C E N N N N E O S C 
N C N E N O E E S S C E C E O C N O N O O E N E E E E E S C E N E E N S E S S 
S C S O N N C E E O C N E C E C O N S C E C C E E O E O E C E O C S O N E C E 
C N O N N C N N O N C S N N N C N C E O C N N C E C O C N C C N S N C C N S C 
E N N E N N N S C N N C O O N E N N N N E O C S O N C N E E C O C C O N E N S 
N C E C O N C O N E E N N S O N S C N S S C N S E O S C N N C O E C N C E E N 
C E C E C S C C E E O C C N C N E C O O E S N N C O E N N N N O E C S N N C E 
N S N E E O E E C E E E C O N 
E S E O O E N C N S S N O S N 

- West 1:

S N N C N S E E S S C O C O N N S C E S E N N O S N S C S S C C O C E O C C O 
C S E C O N E E C C C N O E E E O E N E E E E C N N C C C S E C N S O N N C N 
C E C E C N C O O C C C N C O C O O C O C N O O N O E C S S C E E C S O N S N 
N N N E N S N S C C C N N C E C E C N O E E S N S S N O O N S O N O O N O C N 
E N E E E S S C S E O O C C C E O S E S N N N C E E N E S N C S N C E E C O S 
O C S O S N O C N E E E N N N S O C E N C S C N O N S S O N E E N S S C N S E 
C E O N O E E N O E E E C S C E O E C C N E S E N E O C E S E S E C N O C S 
S N C N S E E N N E N S C E C S E E E E C C O E E S N C S N S E E O N N S 

- West 2:
- 
S C N C N O S C O E S N N N N N S C N C S E C C N N O E N N N O E C O E N O O 
N S E C O N C C E O O N E C C E E E N O N C N S E O C C E E E E C N E C O C E 
N N C N E C E N C C O O C N E C E E C N O N C C E C E N S C C N S E O S S N E 
O C N N S C N N E C N C S E E S N S O S N O E E S N S E N S C S N N C C C C S 
N O S N N C E E S C E O E E O E C N C E N E E S N O E E C C N C S N N N E E S 
E C S O C N E S C C O N E E E E N S N S E E E C E S C E O E N O C E N N O O C 
N E E E C N C C C C N E N O S N C N E S S S N E C N C E E O E C S E E N 
C N N C N C N C N S E N E S N N C S C S E C S C E O N S E C S E E C S C 

- West 3:
 
N N N C N O S C O C O O C E S N C N C S S E S E N E C N N S E O C C S E C E S 
O S E C O N C C E S O E N E C S C N O O N E N E E E E O C N O E C E N N N S C 
C S S C S N N S O E E O N O O N N N S C S C C S N O E E S O C O E N S N N N E 
O S N O N S E C C E N C N O N E C E N N E O S N E S C E C S N N N O S C C E N 
N C S N S S E N O E C C E S C C N N N O S C S O N O S C S S N N C N E E N E C 
N C N N S E E N N N E C O O E S N C N S N S E N E S N C E C S N N C E E E C C 
N E C N E C N E S N S C C N N C E O C N O N S S C E N C E S C C E E E C C O O 
E N C S N E E E C C C N O O C N E E C C S E S E N O E N O N S S E N S N E E C 
N E C E E O C E E E S O E C S C S S N E C E O O C O C E C C 
C C E N E N N C C N O N N C E E O E N C S O C E O N N O O E 

- West 4:
 
S C N C N O S C O C C C N C C C C C C N C E N S E S S N E C N O C C O C C C E 
E S E C O N C C E E E E O S N E N E O S C O S C S C C N N C E E E N N S N O E 
E N N S N C E N O C C N C S E N E E E O N N E O S C C N C C N S N E E S S N S 
C S C E E N E S C N S E S C N O S C O N S O E C S C C C S E S S E O E N N O C 
C O C E N C E O C N C S E C E E N C E O S C E N C N E N C S C N E C S S E S E 
O C E E N N N C S N S E O N E N C E N O E O O C S N N N E E C E N O S N N O N 
E C O E S S E O N E C S S C E C E S S C N C O N E C O E O N C N E E S E N C N 
S N N N O C S N N O E N E S E N E E O N C E O C N S E O O C C S C E E N O O C 
E E O S N O N N O C O E N E N N N O N O C N S C 
C E C E S N C C C C S N C C C N C E N O C C N N 

## External resources used :
* Images used as feed data : From the Noita discord, thanks to **vagner24** 
* Character image extraction : https://stackoverflow.com/questions/60482696/how-to-crop-each-character-on-an-image-using-python-opencv
* Opencv pattern recognition : https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
