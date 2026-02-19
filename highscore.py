

def beat_high_score(score): 
    with open ("current_score.txt") as f:
        score = int(f.read())
    with open("high_score.txt") as f: 
        previous_high_score = int(f.read())
    score_string = f"Your score is {score}"
    if score > previous_high_score: 
        with open("high_score.txt","w") as f: 
            f.write(f"{score}")
        congratulatory_string = f"Congratulations! You beat the preivous high score of {previous_high_score}"
    else:
        congratulatory_string = f"Sorry, you could not beat the previous high score of {previous_high_score}"
        
    return score_string, congratulatory_string


    
