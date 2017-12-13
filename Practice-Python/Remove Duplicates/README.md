Task : Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Program Flow
1. Program has an inbuilt list coded into it with an additional variable, x, provided to store the final list.
2. There are 2 method which have been coded into the code

Method 1 : each item of the list is iterated over. If the item has not been added into x, it is added in. This is done using the <i>not in</i> function.
Method 2 : The list is converted to a set and converted back to a list. This removes all duplicates

3. X is printed.

Sample output
For list a = [1,2,3,2,1,5,6,5,5,5]
```
[1, 2, 3, 5, 6]
```
