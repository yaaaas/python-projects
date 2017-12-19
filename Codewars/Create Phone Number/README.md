Task: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parenthesis!

Program Flow
1. User inputs a string that contains the numbers which will be converted
2. String is converted to a list and is split into it's constituent numbers
3. Splices of the strings are then compiled with their respective formatting and combined together to give the final result.
