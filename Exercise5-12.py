# Exercise 5-12: Styling if Statements

alien_color = 'green'
player_score = 0

# Check the alien's color.
if alien_color == 'green':
    player_score += 5
    print("You earned 5 points!")

elif alien_color == 'yellow':
    player_score += 10
    print("You earned 10 points!")

else:
    player_score += 15
    print("You earned 15 points!")

# Display the player's score.
print(f"Your total score is {player_score}.")