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

## What's next ?

As discussed by the community, the next goal of this project is to provide methods to handle eyes figures as triangles and try and provide tooling for different computation and deciphering methodologies.
![Triangles](https://i.postimg.cc/QsZw3RsH/graphic-design-is-my-passion2.png?dl=1)



## External resources used :
* Images used as feed data : From the Noita discord, thanks to **vagner24** 
* Character image extraction : https://stackoverflow.com/questions/60482696/how-to-crop-each-character-on-an-image-using-python-opencv
* Opencv pattern recognition : https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
