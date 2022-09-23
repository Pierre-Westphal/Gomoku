from os import system

system("pip install pyinstaller")
system("pyinstaller main.py algo.py --name pbrain-gomoku-ai.exe --onefile")
system('copy .\\dist\\pbrain-gomoku-ai.exe .')