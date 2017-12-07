Task : Take a list and write a program that prints out all the elements of the list that are less than a specific number

Program Flow

1. User is prompted for the max range of the final list, this is stored under the variable <i> Criteria </i>
2. User is prompted to key in the list of values he wants to evaluate
3. The list is then sorted using the filter function and the sorted list is then printed for the user

Sample Input/Output


Case 1: Some of the values fit the max range
```
>>Please input the criteria to sort the final list by(Leave this blank if you want to use the default setting
of 5):  6
>>Please input the chosen elements in the list :  1 2 3 4 5 6 7 8 9 10
The Final List of numbers is [ 1 , 2 , 3 , 4 , 5 ]
```

Case 2: None of the values fit the max range
```
>>Please input the criteria to sort the final list by(Leave this blank if you want to use the default setting
of 5):  5
>>Please input the chosen elements in the list:  6 7 8 9 10
The Final List of numbers is [  ]
```

Case 3: All of the values fit the max range
```
>>Please input the criteria to sort the final list by(Leave this blank if you want to use the default setting 
of 5):  10
>>Please input the chosen elements in the list:  1 2 3 4 5 6 7 8 9
The Final List of numbers is [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
```
