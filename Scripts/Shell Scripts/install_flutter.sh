#	Description:
#		A script to install Flutter framework
#	Author:
# 		Mike Zamayias

#	mkdir ~/Repositories
# echo 'mkdir ~/Repositories'
# sleep 2
# mkdir ~/Repositories

#	cd to ~/Repositories
 echo 'cd ~/Repositories'
 sleep 2
 cd ~/Repositories

#	clone repository
# echo 'clone flutter repository'
# sleep 2
# git clone https://github.com/flutter/flutter.git -b stable --depth 1

#	Add Flutter to PATH
echo 'add flutter to PATH'
sleep 2
echo 'export PATH="$PATH:/home/mzamayias/Repositories/flutter/bin"' >> ~/.zshrc

#	Download development binaries
echo 'flutter precache'
sleep 2
flutter precache
