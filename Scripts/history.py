from pprint import pprint


def remove_garbage(some_list, *args):
    for item in args:
        if item in some_list:
            some_list.remove(item)
    return some_list


history = {}

with open('history.txt', 'r') as file:
    lines = file.readlines()
    history_size = len(str(len(lines)).split()[0])
    for line in lines:
        line_contents = line.split()
        command_index = int(line_contents[0])
        command = ' '.join(line_contents[1:])
        history[f'{command_index:0{history_size}d}'] = command

packages_to_install = [
    history[f'{index+1:0{history_size}d}'].split(' ')
    for index in range(0, len(history))
    if 'apt install' in history[f'{index+1:0{history_size}d}'] and 'apt upgrade' not in history[f'{index+1:0{history_size}d}']
][:-2]

for package in packages_to_install:
    remove_garbage(
        package,
        'sudo', 'apt', 'install', '-y', '\\\\n'
    )

packages_to_install = [
    item for package in packages_to_install for item in package
]

remove_garbage(
    packages_to_install,
    'gnome-shell-extension-ubuntu-dock', 'mainline', 'lm-sensors', 'inkscape-y', 'slack-desktop', 'slack', 'lame',
    'kid3', 'easytag'
)

pprint(packages_to_install)
print(len(packages_to_install))
