# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")


# The game starts here.

define a = Character("Angel", color="#fff")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    scene bg entrance_hall
    pause
    show angel casual
    pause
    scene bg park
    "There's a gentle breeze that blows the sweet scent of various aromas"
    a "Ahhh fresh air. I love the park this time of the day!"
    a "Oh Hey! I didn't get your name. What do they call you?"
    $ p = renpy.input("Oh, um I am. . .")
    if p == "":
        "Please enter a name."
    p "My name is [p], nice to meet you" 
    a "Hehe nice to meet you [p]!"
    a "Ah I've got a brainteaser for you"
    a "Do you like chocolate topped vanilla ice-cream?"
    menu:
        "Absolutely, it's the best!":
            "I LOVE THAT ONE! It's my favourite."
            jump yes
        "Uhh. No.":
            "Sorry no, I'm not a fan."
            jump no

label yes:
    show angel casual
    a "I know right! especially when its melted at the right temperature!"
label no:
    a "Aww. but it's a perfect blend."    
    return
