#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

FAV_COURSE = input('What is your favorite course? ')
DOG = input('Do you like dogs? ')
EMOTION = input('How do you feel rignt now? ' )

os.environ["FAV_COURSE"] = FAV_COURSE
os.environ["DOG"] = DOG
os.environ["EMOTION"] = EMOTION

print(os.getenv("FAV_COURSE"))
print(os.getenv("DOG"))
print(os.getenv("EMOTION"))
