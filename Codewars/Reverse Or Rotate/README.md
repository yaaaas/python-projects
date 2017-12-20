The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If
  - sz is <= 0 or if str is empty return ""
  - sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
  
Program Flow:
1. Function is called and arguments passed in are checked to ensure they meet the requirements. If they do not, '' is returned
2. The string is then sliced into chunks of size sz using a for loop that has a step of sz
3. Before the for loop runs, it checks to see if i(the current starting index of the slice)+sz(the step) is greater than the overall length of the string provided. If it is, the for loops stops.
4. If it is not, the sum of each number in the string chunk of size sz is then compiled and evaluated. If it is divisible by 2, the chunk is reversed by using a splice. Otherwise, it is rotated to the left by one position ( Eg. 12345 becomes 23451 )
5. The final result is added to a final string called final which is then returned.

Sample Output
```
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"
```
