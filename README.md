# Looping Practice 1: Spicy Peppers

## Problem Description
Ron is cooking chili using an assortment of peppers.

The spiciness of a pepper is measured in Scolville Heat Units (SHU). Ron’s chili is currently
not spicy at all, but each time Ron adds a pepper, the total spiciness of the chili increases
by the SHU value of that pepper.

The SHU values of the peppers available to Ron are shown in the following table:

Pepper Name | Scolville Heat Units
--|--
Poblano | 1500
Mirasol | 6000
Serrano | 15500
Cayenne | 40000
Thai | 75000
Habanero | 125000

Your job is to determine the total spiciness of Ron’s chili after he has finished adding peppers.

## Input Specification
The first line of input will contain a positive integer N, representing the number of peppers Ron adds to his chili. The next N lines will each contain the name of a pepper Ron has
added. Each pepper name will exactly match a name that appears in the table above. Note that more than one pepper of the same name can be added.

## Output Specification
The output will consist of a positive integer T, representing the total spiciness of Ron’s chili.

### Sample Input
```
4
Poblano
Cayenne
Thai
Poblano
```

### Output for Sample Input
```
118000
```

### Explanation of Output for Sample Input
A Poblano pepper has an SHU value of 1500. A Cayenne pepper has an SHU value of 40000. A Thai pepper has an SHU value of 75000. The total spiciness of Ron’s chili is therefore: $1500 + 40000 + 75000 + 1500 = 118000$.


<br><br>

# Looping Practice 2: Fergusonball Ratings

## Problem Description
Fergusonball players are given a star rating based on the number of points that they score
and the number of fouls that they commit. Specifically, they are awarded 5 stars for each
point scored, and 3 stars are taken away for each foul committed. For every player, the
number of points that they score is greater than the number of fouls that they commit.
Your job is to determine how many players on a team have a star rating greater than 40.
You also need to determine if the team is considered a gold team which means that all the
players have a star rating greater than 40.

## Input Specification
The first line of input consists of a positive integer N representing the total number of players
on the team. This is followed by a pair of consecutive lines for each player. The first line
in a pair is the number of points that the player scored. The second line in a pair is the
number of fouls that the player committed. Both the number of points and the number of
fouls, are non-negative integers.

## Output Specification
Output the number of players that have a star rating greater than 40, immediately followed
by a plus sign if the team is considered a gold team.

### Sample Input 1
```
3
12
4
10
3
9
1
```

### Output for Sample Input 1
```
3+
```

### Explanation of Output for Sample Input 1
The chart shows the star rating for each player:
Player | Points | Fouls | Stars
--|--|--|--
1 | 12 | 4 | 48
2 | 10 | 3 | 41
3 | 9 | 1 | 42

For example, the star rating for the first player is
12×5−4×3 = 48. All three players have a rating
greater than 40 so the team is considered a gold
team.

### Sample Input 2
```
2
8
0
12
1
```

### Output for Sample Input 2
```
1
```

### Explanation of Output for Sample Input 2
The chart shows the star rating for each player:
Player | Points | Fouls | Stars
--|--|--|--
1 | 8 | 0 | 40
2 | 12 | 1 | 57

Since only one of the two players has a rating
greater than 40, this team is not considered a gold
team.