#	Description:
#		A script to install Dart programming language
#	Author:
# 		Mike Zamayias

#	Update packages
echo 'update packages'
sleep 2
sudo apt update

#	Update apt-transport-https
echo 'install apt-transport-https'
sleep 2
sudo apt install apt-transport-https -y

#	Download keys
echo 'download dart stuff'
sleep 2
sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
sudo sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'

#	Update packages
echo 'update packages'
sleep 2
sudo apt update

#	Install Dart
echo 'install dart'
sleep 2
sudo apt install dart -y

#	Add Dart to PATH
echo 'add dart to PATH'
sleep 2
echo 'export PATH="$PATH:/usr/lib/dart/bin"' >> ~/.zshrc
