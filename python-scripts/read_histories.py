Scriptsdef extend_list(small_list: list) -> list:
    big_list = []
    for package_name in small_list:
        big_list.extend(package_name)
    return big_list


def remove_from_list(list_to_clean: list, words_to_remove_to_clean: list) -> list:
    new_list = []
    for word in list_to_clean:
        if word not in new_list and word not in words_to_remove_to_clean:
            new_list.append(word)
    return new_list


def clean_list(list_to_clean: list) -> list:
    new_list = []Scripts
    for item in list_to_clean:
        if item not in new_list:
            new_list.append(item)
    return new_list


# read history
with open('history.txt', 'r', encoding='utf-8') as history:
    lines_1 = history.readlines()

# format lines
lines_1 = [
    line[7:-1]
    for line in lines_1
]

# read history
with open('zsh_history.txt', 'r', encoding='utf-8') as history:
    lines_2 = history.readlines()

# format lines
lines_2 = [
    line[15:-1]
    for line in lines_2
]

lines = lines_1 + lines_2

# list of packages to install
packages_to_install = []

# list of packages to remove
packages_to_remove = []

# words_to_remove to remove
words_to_remove = [
    'sudo', 'apt', 'install', 'remove', '-y', '--fix-broken', 'albert',
    'solaar-gnome3', 'piper', 'python3-pyudev', 'cups-pdf', '-y\\', 'apt-get',
    'ghostscript', 'unoconv', 'libreoffice-java-common', 'sudo', 'libvulkan1',
    'mesa-vulkan-drivers', 'mesa-vulkan-drivers', 'libratbag', 'glxinfo',
    'mesa-utils', 'wv', '\x1b[200~sudo', 'vulkan-utils', '', 'build-essential',
    'kernel-package', 'fakeroot', 'libssl-dev', 'ccache', 'flex', 'bison',
    'libelf-dev', 'libncurses5-dev', 'wget', 'cmake', 'python3', 'python-minimal',
    'python-mako', 'python3-mako', 'pkg-config', 'libexpat1-dev', 'libxrandr-dev',
    'libdrm-dev', 'libxdamage-dev', 'libxcb-glx0-dev', 'libxcb-dri2-0-dev',
    'libxcb-dri3-dev', 'libxcb-present-dev', 'libxshmfence-dev', 'libxxf86vm-dev',
    'libx11-xcb-dev', 'ninja-build', 'inkscape', 'steam-installer-y', 'clang',
    'libgtk-3-dev', 'libblkid-dev', 'liblzma-dev', 'pm-utils', 'hibernate',
    'lutris', 'nvidia-driver-455', 'nvidia-driver-450', 'nvidia-driver-435',
    'nvidia-graphics-drivers-455', 'lv2-dev', 'meson', 'fftw-dev', 'lv2',
    '-ylv2-dev', "'^lv2*'", 'python3.8-dev', 'pop-desktop-y', 'pop-desktop',
    'openjdk-8', 'openjdk-8-jdk', 'ttf-mscorefonts-installer', 'fonts-firacode',
    'dart', '--purge', 'steam', 'autoremove', 'solaar', '-y;', 'autoclean', '--purge\\',
    'printer-driver-cups-pdf', '\'^libreoffice.*\'--purge', '--allow-remove-essential',
    'reboot', 'slack-desktop', '&&', 'upgrade', 'update', './codium_1.43.2-1585083818_amd64.deb',
    'spotify-client', 'slack', 'inkscape-y', 'gnome-shell-extension-ubuntu-dock',
    'libc6:i386', 'libncurses5:i386', 'libstdc++6:i386', 'lib32z1', 'libbz2-1.0:i386', 'lm-sensors',
    'debhelper', 'dbus', 'google-mock', 'libboost-dev', 'libboost-filesystem-dev', 'libboost-log-dev',
    'libboost-iostreams-dev', 'libboost-program-options-dev', 'libboost-system-dev libboost-test-dev',
    'libboost-thread-dev', 'libcap-dev libsystemd-dev', 'libegl1-mesa-dev', 'libgles2-mesa-dev',
    'libglm-dev', 'libgtest-dev', 'liblxc1', 'libproperties-cpp-dev', 'libprotobuf-dev', 'libsdl2-dev',
    'libsdl2-image-dev', 'lxc-dev', 'protobuf-compiler', 'anbox', 'lame', 'kid3', 'easytag', 'mainline',
    'cmake-data', '\\\\n', 'libboost-system-dev', 'libboost-test-dev', 'libcap-dev', 'libsystemd-dev',
    'python3-setuptools', 'python3-gi', 'python-gobject'

]

# populate lists
for line in lines:
    if 'sudo' in line and 'apt' in line:
        if 'install' in line:
            if line not in packages_to_install:
                packages_to_install.append(line)
        if 'remove' in line:
            if line not in packages_to_remove:
                packages_to_remove.append(line)

packages_to_install = [
    package_name.split(' ')
    for package_name in packages_to_install
]
packages_to_install = remove_from_list(clean_list(extend_list(packages_to_install)), words_to_remove)

packages_to_remove = [
    package_name.split(' ')
    for package_name in packages_to_remove
]
packages_to_remove = remove_from_list(clean_list(extend_list(packages_to_remove)), words_to_remove)
