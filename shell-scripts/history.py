"""
A python script to setup packages in a fresh Pop_OS! installation from a previous one.
"""
from pprint import pprint
from os import system as run


def remove_garbage(some_list, *args):
    """
    Function to remove garbage from a list of strings,
    some_list is the list of strings and
    *args is the garbage to be removed.
    """
    for item in args:
        if item in some_list:
            some_list.remove(item)
    return some_list


def read_history():
    """
    Function to read and parse a .txt file which includes a sessions history, returns a dictionary
    with the indexes of those commands as its keys and the commands as its values.
    """
    #   create a new dictioanry
    history = {}
    #   read from file
    with open('history.txt', 'r') as file:
        lines = file.readlines()
    #   parse file
    history_size = len(str(len(lines)).split()[0])
    for line in lines:
        line_contents = line.split()
        command_index = int(line_contents[0])
        command = ' '.join(line_contents[1:])
        history[f'{command_index:0{history_size}d}'] = command
    #   return dictionary
    return history, history_size


def install_packages():
    """
    Function to install packages from the history.txt file
    """
    #   call read_history function
    history, history_size = read_history()
    #   make a packages installation commands list
    packages_to_install = [
        history[f'{index+1:0{history_size}d}'].split(' ')
        for index in range(0, len(history))
        if 'apt install' in history[f'{index+1:0{history_size}d}'] and 'apt upgrade' not in history[f'{index+1:0{history_size}d}']
    ][:-2]
    #   remove command garbage
    for package in packages_to_install:
        remove_garbage(
            package,
            'sudo', 'apt', 'install', '-y', '\\\\n'
        )
    #   merge those string lists to a list of strings
    packages_to_install = [
        item for package in packages_to_install for item in package
    ]
    #   remove package garbage
    remove_garbage(
        packages_to_install,
        'gnome-shell-extension-ubuntu-dock', 'mainline', 'lm-sensors', 'inkscape-y', 'slack-desktop', 'slack', 'lame',
        'kid3', 'easytag', './codium_1.43.2-1585083818_amd64.deb'
    )
    command = f"sudo apt install {' '.join(packages_to_install)} -y"
    print(command)


def initial_setup():
    setup_spotify_installation = [
        'curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - ',
        'echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list'
    ]
    setup_codium_installation = [
        'wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | sudo apt-key add - ',
        "echo 'deb https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/repos/debs/ vscodium main' | sudo tee --append /etc/apt/sources.list.d/vscodium.list"
    ]
    other_options = [
        'sudo apt update && sudo apt upgrade -y',
        'sudo gpasswd -a $USER input',
        'reboot'
    ]
    for command in setup_spotify_installation + setup_codium_installation + other_options:
        print(command)


pprint(read_history()[0])
install_packages()
initial_setup()
