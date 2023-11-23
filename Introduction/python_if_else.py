'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.
'''

num = int(input())

if num%2 != 0:
    print("Weird")
else:
    if num>2 and num <5:
        print("Not Weird")
    elif num>6 and num <=20:
        print("Weird")
    else:
        print("Not Weird")