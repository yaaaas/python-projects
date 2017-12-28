Task : Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

A working copy of this program can be found at https://repl.it/@ivanleo97/Binary-Search 

Program Flow
1. A number is taken as an input to be evaluated.
2. The middle of the entire array is first taken as a starting point. The program quits here if the middle of the array is equal to the number input at step 1. If the number is smaller than the middle element, the lower end of the array is evaluated, otherwise, the upper end of the array is evaluated. 
3. This starts a loop that creates an increasingly smaller range of values to be evaluated. The loop continually runs until the elemenent is found or the length of the range being evaluated is one.
4. A final output is then printed depending on the result of the loop.

Sample output
Case 1: Number does not exist in the list
```
Please input the number to be searched for:  660
5605 , 889, Range : 0 889
3298 , 444, Range : 0 444
2171 , 222, Range : 0 222
611 , 111, Range : 0 111
1942 , 56, Range : 55 111
1804 , 28, Range : 55 83
1767 , 14, Range : 55 69
632 , 7, Range : 55 62
651 , 4, Range : 58 62
664 , 2, Range : 60 62
660 does not exist in the list
```

Case 2: Number exists in the list
```
Please input the number to be searched for:  8012
5605 , 889, Index Range : 0 889
7704 , 445, Index Range : 444 889
8842 , 223, Index Range : 666 889
8280 , 111, Index Range : 666 777
7921 , 55, Index Range : 666 721
8099 , 28, Index Range : 693 721
7986 , 14, Index Range : 693 707
8041 , 7, Index Range : 700 707
8012 is in the list
```
