"""
Description
	A script to download and install Dart automatically.
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
    "sudo apt update",
    "sudo apt install -y apt-transport-https",
    "sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'",
    "sudo sh - c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'",
    "sudo apt update",
    "sudo apt install -y dart",
    "echo 'export PATH=\"$PATH:/usr/lib/dart/bin\"' >> ~/.zshrc"
)

for command in commands:
    execute(command)
