Task

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
```
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
```

Program Flow
1. A variable called Final is initialised to store the final input
2. We run a loop for every variable in the array that is passed into the program. This loop counts the number of occurences of the current element in the final variable. If it is less than the limit, the element is appended into the final array
3. The final array is then returned as the final input
