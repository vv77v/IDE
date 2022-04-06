"""Guess the number game
The computer makes its own guess and guesses the number itself
"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number
    
    Args:
        number (int, optional): The hidden number. Defolds to 1.
        
    Returns:
        int: Number of attempts
    """
    count = 0
    gap = 50
    predict_number = 50
    
    while True:
        count+=1
     
        if predict_number > number: # the number must be less than
            gap//=2
            if gap == 0: gap = 1
            predict_number = predict_number - gap
                
        elif predict_number < number: # the number must be greater than
            gap//=2
            if gap == 0: gap = 1
            predict_number = predict_number + gap
        else: break   
    return(count)


def score_game(random_predict) -> int:
    """For how many attempts on average for 1000 approaches does our algorithm guess

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1) # we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # Made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'my algorithm guesses the number in an average of: {score} attempts')
    return(score)


if __name__=='__main__':
    # RUN
    score_game(random_predict)
    