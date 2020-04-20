#!/usr/bin/env python3
"""
Author      : Vicky
Description : Python Adventure Game
"""
# import os, time and random module
import os
import time
import random


def play_the_game():
    """Main Menu.
    First main screen from the game.
    """
    clear_screen()
    print("=================================\n"
          "\nWelcome to Vicky's Adventure Game\n "
          "\n=================================\n")
    time.sleep(2)
    item = []
    option = random.choice(["demon", "centaur", "cerberus",
                            "kaiju", "ogre", "minotaur"])
    intro_game(item, option)
    main_field(item, option)


def clear_screen():
    """Clearing the screen.
    Clear the screen from all of text.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def typing_game(msg_to_print):
    """Pause between typing.
    Adding timer sleep for 1 second.
    """
    print(msg_to_print)
    time.sleep(1)


def intro_game(item, option):
    """Introduction in Game.
    First intro at the Game.
    """
    typing_game("You find yourself wake up in an open field, filled "
                "with wildtree and purple wildflowers.")
    typing_game("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    typing_game("In front of you is an old house.\n")
    typing_game("To your left is a super creepy cave.\n")
    typing_game("In your hand you hold your rusty (but not very "
                "effective) dagger.\n")


def option_cave(item, option):
    """Option to the Cave.
    Player selected the Cave.
    """
    if "cursed_sword" in item:
        typing_game("\nYou peek cautiously into the cave.")
        typing_game("\nYou've been here before, and gotten all "
                    " the good stuff. It's just an empty cave "
                    " now.")
        typing_game("\nYou walk back to the field.\n")
    else:
        typing_game("\nYou peek cautiously into the cave.")
        typing_game("\nIt turns out to be only a very small cave.")
        typing_game("\nYour eye catches a glint of shiny behind a "
                    "rock.")
        typing_game("\nYou have found the magical Sword of Titan!")
        typing_game("\nYou discard your silly rusty dagger and take "
                    "the sword with you.")
        typing_game("\nYou walk back out to the field.\n")
        item.append("cursed_sword")
    main_field(item, option)


def option_house(item, option):
    """Option to the House.
    Player selected the House.
    """
    typing_game("\nYou approach the door of the old house.")
    typing_game("\nYou are about to knock when the door "
                "opens and out steps a " + option + ".")
    typing_game("\nWaitttt! This is the " + option + "'s house!")
    typing_game("\nThe " + option + " attacks you!\n")

    if "cursed_sword" not in item:
        typing_game("You feel a bit under-prepared for this, "
                    "what with only having a rusty dagger.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "cursed_sword" in item:
                typing_game("\nAs the " + option + " moves to attack, "
                            "you unleash your shiny sword.")
                typing_game("\nThe Sword of Titan shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                typing_game("\nBut the " + option + "takes one look at "
                            "your shiny new weapon and runs away!")
                typing_game("\nYou have rid the town of the " + option +
                            ". You are Victorious!\n")
            else:
                typing_game("\nYou do your best...")
                typing_game("but your rusty dagger is no match for the "
                            + option + ".")
                typing_game("\nYou have been Defeated!\n")
                typing_game("\nGAME OVER!\n")
            play_again()
            break

        if choice2 == "2":
            typing_game("\nYou run back into the open field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            main_field(item, option)
            break


def main_field(item, option):
    """Main Field.
    Field before player have to choose.
    """
    typing_game("Enter 1 to knock on the door of the old house.")
    typing_game("Enter 2 to peer into the dark cave.")
    typing_game("What would you like to do?")

    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            option_house(item, option)
            break
        elif choice1 == "2":
            option_cave(item, option)
            break


def play_again():
    """Re-Start Game.
    Question if want to play again or not.
    """
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        typing_game("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_the_game()
    elif again == "n":
        typing_game("\n\n\nThank you for playing this game!"
                    "\nI hope you enjoy!\n"
                    "See you next time.\n\n\n")
        clear_screen()
    else:
        play_again()


# Let's Play this Game
play_the_game()
