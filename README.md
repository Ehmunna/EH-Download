## Termux use 
``` python
pkg update && pkg upgrade -y
pkg install python git wget curl ffmpeg -y
pip install yt-dlp requests colorama tqdm
termux-setup-storage
git clone https://github.com/Ehmunna/EH-Download.git
cd EH-Download
chmod +x install_eh_simple.sh
bash install_eh_simple.sh
python eh_permission_fixed.py
