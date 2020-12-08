"""
Description
	A script to download and install Flutter SDK automatically.
Author
	Mike Zamayias
"""

from os import system as run
from time import sleep


def execute(command):
    print(command)
    sleep(2)
    run(command)


commands = (
    "cd ~",
    "mkdir Development",
    "cd Development",
    "git clone https://github.com/flutter/flutter.git -b dev --depth 1",
    "echo 'export PATH=\"$PATH:/home/mzamayias/Development/flutter/bin\"' >> ~/.zshrc",
    "source ~/.zshrc",
    "cd",
    "echo 'export PATH=\"$PATH:/usr/lib/dart/bin\"' >> ~/.zshrc"
    "flutter precache"
)

for command in commands:
    execute(command)
