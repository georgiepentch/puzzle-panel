# Puzzle Panel Solver

## Getting started

To run the solver, clone the repository and run `new_gui.py`.

Open the solver window next to your game display as shown below:

<img width="1298" alt="Screen Shot 2023-05-07 at 1 33 02 PM" src="https://user-images.githubusercontent.com/85321099/236693612-0dfa9b8b-8ded-4758-9bc1-1a01ca36317d.png">

The solver may take a few seconds, but it should automatically update and highlight the squares that need to be pressed.

## Troubleshooting

**IMPORTANT:** Make sure that there's nothing on your screen blocking the game display, otherwise the solver will not work properly.

If the solver still isn't working, open up `shroom.png` and `feather.png`, and ensure that the pictures match with the sprites in your game. By defeault, the solver is configured to work with OpenEmu using the Linear shader. Other emulators, such as DeSmuME, tend to display the same with more saturated colours, which interferes with the sprite detection. If you are using another emulator and the sprites don't match the images in the repo, the best course of action is likely to replace `shroom.png` and `feather.png` with your own screenshots of the sprites from the game display.

## Next steps

I'm probably done with this project for now. I wanted to make a bot that would be able to play the game directly (`wip_bot.py`), but unfortuantely that doesn't seem to be possible. I can't get my script to actually interact with the emulator (I can simulate the mouse moving just fine, and have even coded it to move the mouse to the correct locations, but I can't make it click). I think it's because of something I read on the python `macmouse` documentation:

> Other applications, such as some games, may register hooks that swallow all key events. In this case mouse will be unable to report events.

This would explain why functions like `pyautogui.click()` seem to have no effect on emulators, despite working just fine on other applications.
