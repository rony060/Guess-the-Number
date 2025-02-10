from browser import document, alert
import random

number_to_guess = random.randint(1, 100)
attempts = 0

def make_guess():
    global attempts
    attempts += 1
    guess = int(document["guess"].value)
    result = document["result"]

    if guess < number_to_guess:
        result.text = "Too low!"
    elif guess > number_to_guess:
        result.text = "Too high!"
    else:
        result.text = f"Congratulations! You guessed the number in {attempts} attempts."
        document["guess"].disabled = True
        document["submit"].disabled = True

