# String And String Method

## String Slicing Type:-
* Basic String Slicing
* Omitting Indices
* Negative Indices
* Step (Stride) in Slicing
* Reversing a String

## Basic String Slicing:-
- You can extract a portion of a string by specifying the start and end indices. The syntax is string[start:end].
- The start index is inclusive (i.e., the character at that position is included), and the end index is exclusive (i.e., the character at that position is not included).
- my_string = "Hello, World!"
- substring = my_string[7:12]  # Extracts "World"

## Omitting Indices:- 
- If you omit the start index, it defaults to the beginning of the string.
- If you omit the end index, it defaults to the end of the string.
- my_string = "Hello, World!"
- first_part = my_string[:5]  # Extracts "Hello"
- last_part = my_string[7:]  # Extracts "World!"

## Negative Indices:- 
- You can use negative indices to count from the end of the string.
- my_string = "Hello, World!"
- last_character = my_string[-1]  # Extracts "!"

## Step (Stride) in Slicing:- 
- You can specify a step value to skip characters during slicing.
- my_string = "0123456789"
- even_digits = my_string[::2]  # Extracts "02468"

## Reversing a String:- 
- To reverse a string, use a step value of -1.
- my_string = "Hello, World!"
- reversed_string = my_string[::-1]  # Extracts "!dlroW ,olleH"

## String Method's:
- capitalize()
- lower()
- upper()
- strip()
- startswith()
- endswith()
- replace()
- split()
- join()



