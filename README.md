day - 5
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

day -6:

 Playlist Analysis System
 Problem Statement:
This program takes a list of song durations (in seconds) and analyzes the playlist. It classifies the playlist as Balanced, Repetitive, Too Short, Too Long, or Irregular. After classification, it provides a suitable recommendation.
 Personalization Applied:
Applied Rule: A playlist is considered Balanced only if the difference between the longest and shortest song (`max - min`) is greater than or equal to 30 seconds.
If variation is less than 30 seconds, it is marked as Irregular
 Logic Used:
I used list input to store song durations.
First, I checked for invalid entries (duration ≤ 0).
Then I calculated total duration using `sum()` and number of songs using `len()`.
Using conditional statements, I categorized the playlist based on total duration and repetition (`count()` function).
Finally, I applied the personalization rule using `max()` and `min()` to determine if the playlist is balanced.
How to Run:
1. Enter song durations separated by space
2. Program analyzes the playlist
3. It displays total duration, number of songs, category, and recommendation
Example Input and Output:
Input:
Enter durations: 180 200 220 210
Output:
Total Duration: 810 seconds
Songs: 4
Category: Balanced Playlist
Recommendation: Good listening session



