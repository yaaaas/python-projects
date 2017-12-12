Task : Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. The number of guesses is also printed out for the user. He is then given the option to quit the program or continue playing

Program Flow
1. Random Number is generated using random.randint
2. Using a while loop, the user is continually prompted for a guess
3. This while loop only breaks if the user guesses the number correctly and chooses to exit the program

Sample Input

Case 1 : User chooses to exit and takes 4 guesses
```
>>Guess the number! Input your guess here:  3
Too High!
>>Guess the number! Input your guess here:  4
Too High!
>>Guess the number! Input your guess here:  1
Too low!
>>Guess the number! Input your guess here:  2
You've guessed correctly! The number is 2. You took 4 guesses!
>>Would you like to exit? (Type Exit) :  Exit
```

Case 2: User does not choose to exit on the first round and plays two rounds of the guessing game.

```
Guess the number! Input your guess here:  3
Too High!
Guess the number! Input your guess here:  1
You've guessed correctly! The number is 1. You took 2 guesses!
Would you like to exit? (Type Exit) :  
Guess the number! Input your guess here:  6
Too low!
Guess the number! Input your guess here:  8
Too low!
Guess the number! Input your guess here:  9
You've guessed correctly! The number is 9. You took 3 guesses!
Would you like to exit? (Type Exit) :  Exit
```
