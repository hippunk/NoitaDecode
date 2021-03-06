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
  - O for West
  - E for East
  - C for Center

### Glyphes results : https://github.com/hippunk/NoitaDecode/blob/main/glyphes.txt

As discussed by the community, characters could form trigrams.
![Triangles](https://i.postimg.cc/QsZw3RsH/graphic-design-is-my-passion2.png?dl=1)

I've built a transform_to_trigram fuction which help process eyes as trigram
They are built following this process:
![trigrams_build](https://i.postimg.cc/VLWGkVrd/trigrams-process.jpg)
(There's currently no way to change triangles processing order, but you can do so by changing indices in the function)

### Trigrams results : https://github.com/hippunk/NoitaDecode/blob/main/trigrams.txt

Trigrams are then converted to unique values with parse_trigrams_to_numeric
For my first hypotesis, I don't consider glyph position so [N,S,O] is equivalent to [O,N,S] etc.
I've associated each glyph with a value that ensure each combinaison is unique  
  - N = 1
  - S = 10
  - W = 100
  - E = 1000
  - C = 10000

### Values results : https://github.com/hippunk/NoitaDecode/blob/main/trigrams.txt
 
 Then I've computed the converted text frequency :
 {10011: 67, 1011: 63, 11010: 61, 11100: 58, 20001: 57, 10101: 56, 11001: 53, 1101: 50, 10002: 45, 20010: 40, 10110: 39, 2001: 35, 21000: 34, 12000: 34, 12: 31, 111: 29, 1002: 29, 2010: 29, 2100: 28, 10020: 27, 102: 25, 20100: 22, 201: 21, 3000: 19, 1110: 19, 21: 15, 1020: 14, 3: 11, 10200: 10, 1200: 9, 30000: 6}
 
 That's 31 unique values, which match the Finnish alphabet size.
 https://www.sttmedia.com/characterfrequency-finnish
 
So we can expect no blank or punctuation.
I've built a translation pattern from those sttmedia alphabet statistics :
most_frequent_finnish_letters = ['A', 'I', 'T', 'N', 'E', 'S', 'O', 'L', '??', 'K', 'U', 'M', 'H', 'V', 'R', 'J', 'P', 'Y', 'D', '??', 'G', 'C', 'B', 'F', 'W', 'Z', 'X', '??', 'Q', '??', '??']

And converted our values by matching frequency.

### Texts results : https://github.com/hippunk/NoitaDecode/blob/main/texts.txt

As we can observe. There's a lot of double letters which seems to be a caracteristic of the Finnish language.

## What's next ?

I'm planning on automating recurent pattern detection.
I've found 2 of them manually

Long recurent patterns :
- pattern 1 : IEJFTKSQMINIFPNRAK??HSTBE, matches 3 times
- pattern 2 : NSNLJJIUJTLUB, matches 2 times

H"**IEJFTKSQMINIFPNRAK??HSTBE**"AIAYRSU??AOT??"**NSNLJJIUJTLUB**"D??EQKZLYRBRVS????EECLO??PC??ULCORZADNYURKAJ????VRMATDZJ


P"**IEJFTKSQMINIFPNRAK??HSTBE**"WAVSJIANDMAB??KAPULAA??TDSBDY??B??TAHSQ??THVRMGNNSKCITIM??N??ORDMCUMTRU??DIEK????AENSTEDMAJNOCYEO??STVIG


YIEBKNHVSA??LVKYLVHTOLNS??LRATVTRNOHALHLJ??AHAKEPYOSAATSKOLVITKNMH??ISNEIPYXEUOCUDHIW??LAV??TMCTNY??GDLRRIN??PLTC??TEPUYEDWKZCIP??NDI??J??WE??GCLWEOAQ


OIEBKNHVSAHOSKL??XKPELTJIE??AACGVYIATNUKJNOUFDNLONKEOLSIXWUEISWLXHGS????UMCPNV??KZVLYYIBRATUTOK??F??????MWACU??TYIIDOLTVE??AIXTL??U


RIEBKNHVSAHOSKL??XKPELRSLJ??AALGVYUOVNEBJNOVFDWHMNIJYTOGP????U??AGGO??LOGKNS??VEUESIAEVNACOFSASRHJWARNW????SDEAMOIID??MEYIQR


A"**IEJFTKSQMINIFPNRAK??HSTBE**"SO??VRSU??E??NC"**NSNLJJIUJTLUB**"J??LTDZUADDE??WUY??REDRXGTPTTSXTSGYMGFIKHWFHOTDMJHZXFSG??


AIEBKNWGPEIV??JHAPQOMLVSVBNGEPKPOCSAFTISJSVTIIAEZLKATL??GEF??HBFDVROIFTLTVN??UP??DUOPH??EEAMLZ??ATXATOSYNTYVA


GIEBKNU??OTA??UJYMMVGA??HTPO??UZURICFSGBPOAICZLTYUSPJA??M??ARXMGOHWNA??GZ??LLZKTR??OFM??MEIOMTAESSODEUIXOLOJKYMANNOHMLOHIBOTTWPK??NQ??NN


TIEBKNHVSAHOSKL??XKPELVSAEDOAIOMUEI??OLT??RLN????ETZIDIRUQHM??LK??XNMPHLWNSAP??YEMUZILTGIUW??NITYOYU??NSOW??SETYMSSVNIJ??CCIOE??NGCA??


## External resources used :
* Images used as feed data : From the Noita discord, thanks to **vagner24** 
* Character image extraction : https://stackoverflow.com/questions/60482696/how-to-crop-each-character-on-an-image-using-python-opencv
* Opencv pattern recognition : https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
* Finnish alphabet :  https://www.sttmedia.com/characterfrequency-finnish
* Finnish dictionnary : https://github.com/hugovk/everyfinnishword
