import os

from art import *

palavra = input("Digite uma palavra: ")

asciiArt = text2art(palavra, font="standard")
print(asciiArt)

os.system("pause")
