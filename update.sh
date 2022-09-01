echo "███████╗██╗  ██╗███╗   ██╗███████╗██╗   ██╗    ";
echo "╚══███╔╝██║  ██║████╗  ██║╚══███╔╝██║   ██║    ";
echo "  ███╔╝ ███████║██╔██╗ ██║  ███╔╝ ██║   ██║    ";
echo " ███╔╝  ╚════██║██║╚██╗██║ ███╔╝  ██║   ██║    ";
echo "███████╗     ██║██║ ╚████║███████╗╚██████╔╝    ";
echo "╚══════╝     ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     ";
echo "                                               ";

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/jedicode/

clear

cd /etc/

clear

sudo rm -rf /etc/jedicode

clear

mkdir jedicode

clear

cd jedicode

clear

git clone https://github.com/Z4nzu/jedicode.git

clear

cd jedicode

clear

sudo chmod +x install.sh

clear

./install.sh

clear
