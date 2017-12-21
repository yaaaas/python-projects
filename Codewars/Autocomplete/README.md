Task : Create a program that matches a user's input to a defined dictionary of words and suggest words to complete the input. If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.

Example:
```
autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
```

Program Flow:
1. The Program first initialises a new list called matches to store the values that match the user's input
2. The program then compares the user's input to a splice of each individual value in dictionary. If the input matches, the item is added to the list "Matches"
3. Matches is then returned.
