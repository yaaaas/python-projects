Task : Create a program that will play the “cows and bulls” game with the user. 

The game works like this:Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Program Flow
1. A random number is generated
2. User is prompted for his guess
3. User's guess is then compared to that of the generated number by splitting each number into lists. individual elements are then compared with their respective counterparts to give the number of "cows" and "bulls" that the user has obtained.
4. If the user guesses correctly, the program then prints out the correct number and the number of guesses the user has taken to arrive at the value. Otherwise, after 8 guesses, the program quits.

A working version of this file can be found at : https://repl.it/@ivanleo97/SadDescriptiveStickinsect . Click this <a href="https://repl.it/@ivanleo97/SadDescriptiveStickinsect"> Link </a>to see it!

Sample Output:

Case 1: User does not guess it.
```
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
The correct answer was 9515. You took 8 guesses
```

Case 2: User guesses the value
```
Please input your guess! 1234
Your guess was 1234
Cows: 0, Bulls: 4
Please input your guess! 5587
Your guess was 5587
Cows: 3, Bulls: 1
Please input your guess! 5586
Your guess was 5586
Cows: 4, Bulls: 0
The correct answer was 5586. You took 3 guesses
```
