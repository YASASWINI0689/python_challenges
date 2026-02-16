Smart Transport Load Balancing System
Problem Statement:
This program takes a list of package weights and classifies them into Very Light, Normal, Heavy, Overload, and Invalid categories. After classification, a personalized rule is applied based on the length of my name.
Personalization Applied:
Length of my full name (excluding spaces) = 17
PLI = 17 % 3 = 2
Applied Rule: Rule C (Kept only Normal and Heavy loads)
Logic Used
I used a for loop and conditional statements to categorize each weight. Then I counted valid weights and applied the rule based on PLI value. Finally, I displayed the updated lists.
How to Run:
1.	Enter your full name
2.	Enter weights separated by space
3.	The program shows categorized results
Example Input and output:
Enter your full name: yasaswini attaluri 
L value: 17
PLI value: 2
Enter weights: 56 8 21 45 
Applied Rule C
Total Valid: 4
Affected Items: 0
Very Light: []
Normal Load: [8, 21]
Heavy Load: [56, 45]
Overload: []
Invalid Entries: []
