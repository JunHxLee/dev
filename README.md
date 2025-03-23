# dev
pkg install git zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
pkg install python
python -m venv myenv
source ~/myenv/bin/activate
ssh -p 8022 192.168.50.49
pkg install golang
pkg install openjdk-21
git config --global user.email "soulfactor@gmail.com"
git config --global user.name "soulfactor"
