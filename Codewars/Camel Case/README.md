Task : You are given an argument, s, which is a string to be converted to camel case and another argument, n, which is a number(1,2 or 3). 

There are three kinds of camelCase:

```
 camelCase 1: The first letter of each word should be capitalized. 
               Except for the first word.

 Example: "Hello world"  -->  "helloWorld"

 camelCase 2: The last letter of each word should be capitalized. 
               Except for the last word. 

 Example: "Hello world"  -->  "hellOworld"

 camelCase 3: The first and last letters of each word should be capitalized. 
               Except for the first and lasts letter of sentence. 

 Example: "Hello world"  -->  "hellOWorld"
```
You can assume that all of the input data is valid. That is: s always be a string; It contains at least two words; Each word contains only letters(a-zA-Z); Each word contains ar least three letters; n always be 1,2 or 3.


Program Flow
1. The string is first split into its constituent words using the .split() function. These words are then assigned to an array, final.
2. Function is called and the desired type of conversation is selected using n
3. The program runs a loop for each element, creating the desired word by taking splices of individual portions and converting them to upper or lower case.
4. Final is then returned
