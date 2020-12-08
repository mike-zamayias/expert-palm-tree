# import modules
from read_history import *

packages_to_install.extend(
    ['vlc', 'google-chrome-stable', 'chrome-gnome-shell', 'code',
     'papirus-icon-theme', 'breeze-cursor-theme', 'materia-gtk-theme',
     'slack-desktop']
)
packages_to_install = clean_list(packages_to_install)

packages_to_install = ' '.join(packages_to_install)
command_to_install_packages = f'sudo apt install -y {packages_to_install}'

packages_to_remove.extend(
    ['firefox', 'geary', 'gnome-calendar', 'gnome-contacts']
)
packages_to_remove = clean_list(packages_to_remove)

packages_to_remove = [
    f"'^{package_name}.*'"
    if not package_name.startswith("'^")
    else package_name
    for package_name in packages_to_remove
]
packages_to_remove = clean_list(packages_to_remove)

packages_to_remove = ' '.join(packages_to_remove)
command_to_remove_packages = f'sudo apt remove -y {packages_to_remove}'

print(command_to_install_packages)
print(command_to_remove_packages)
