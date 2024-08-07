# RegEx Module in Python

* Search in text using Staring And ending word
* re.search(patten, txt)
* this function is stop when it's get a first match

## Character Class 
* [] = Character class Ex. [A-z] means is A to Z char
* . = any character except newline Example :- "mas mds" r'm.s' you got a string
* \w \d \s = \w\d\s	word, digit, whitespace
* \W \D \S = \W\D\S	not word, digit, whitespace
* [abc] = [abc]	any of a, b, or c
* [^abc] = [^abc]	not a, b, or c
* [a-g] = [a-g] character between a & g
* a|b = means ex. "mitesh amin" so r'mit|ami' so ans is ['mit','ami']
* 
## Anchor
* .* = means anything in between
* \b \B = word, not-word boundary