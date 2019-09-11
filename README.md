# CS50 - Similarities
My work for CS50's Similarities assignment.

A program that parses text files and highlights similarities across files. Program can find whole line similarities, whole sentence similarities, or similarities in substrings of a specified length.

The following files were provided by CS50 - I did not write any of the code in the below files:
* compare
* application.py
* templates/compare.html
* templates/layout.html
* templates/error.html
* static/styles.css
* requirements.txt

https://docs.cs50.net/2018/x/psets/6/similarities/less/similarities.html


Look of index layout where you choose, the two text files you wish to compare and to what level you wish to compare them:
![Index Layout](https://i.imgur.com/goO1WeN.png)


Look of whole line similarities highlighted:
![Whole Line Similarities](https://i.imgur.com/aMjlnnC.png)


Look of sentence similarities highlighted:
![Sentence Similarities](https://i.imgur.com/voVwDlC.png)


Look of substrings similarities highlighted:
![Substring Similarities](https://i.imgur.com/LtWBgNG.png)


# Getting Started

Install Flask and activate environment. 
Install requirements.txt by executing the below into the console within the project folder:

```
pip install -r requirements.txt
```

Then execute the following to run:
```
export FLASK_APP=application.py
```
```
flask run
```

Go to the local host URL provided.
