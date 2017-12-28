 Task: Write a program which will guess a number within a given range that you choose. The user will then say whether each guess the computer makes is too high or too low.
 
A live preview of this code can be found at https://repl.it/@ivanleo97/I-will-guess-your-number 

Program Flow
1. User is prompted for a range upper limit, which will then be set as the variable end.
2. A for loop is set up to guess the user's number. The user will be prompted to input ( l : The guess was too low, h : The guess was too high or y: The guess was correct). A variable called guesses is initialised to keep track of the number of guesses.
3. The middle value of the range currently being evaluated is then used as the guess. 
4. If the user indicates that the value is too high, the upper range of the evaluated limit is used next (  middle value to end). Otherwise, the lower range of the evaluated limit is used next ( start to middle value )
5. The final number of guesses is printed out along with the user's number.

Sample output

```
What is the highest range that you want to play at:  1000
start: 0
End: 1000
The new guess is 500
Did I guess it correctly? ( h, l ,y ) : h
start: 
start: 0
End: 500
The new guess is 250
Did I guess it correctly? ( h, l ,y ) : l
start: 250
End: 500
The new guess is 375
Did I guess it correctly? ( h, l ,y ) : l
start: 375
End: 500
The new guess is 437
Did I guess it correctly? ( h, l ,y ) : y
Got you! I knew the answer was 437
I took 4 guesses to guess your number! Eat that! 

```
