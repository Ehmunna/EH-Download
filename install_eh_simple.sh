#!/data/data/com.termux/files/usr/bin/bash

echo -e "\e[91m"
echo "███████╗██╗  ██╗"
echo "██╔════╝██║  ██║"
echo "█████╗  ███████║"
echo "██╔══╝  ██╔══██║"
echo "███████╗██║  ██║"
echo "╚══════╝╚═╝  ╚═╝"
echo -e "\e[0m"
echo "=============================="
echo -e "\e[92mEH DOWNLOADER - SIMPLE SETUP\e[0m"
echo "=============================="
echo ""

echo -e "\e[93m[1] Installing packages...\e[0m"
pkg install python wget curl -y

echo -e "\e[93m[2] Installing yt-dlp...\e[0m"
pip install yt-dlp colorama tqdm requests

echo -e "\e[93m[3] Making script executable...\e[0m"
chmod +x eh_permission_fixed.py

echo ""
echo -e "\e[92m[✓] Installation complete!\e[0m"
echo ""
echo -e "\e[96m──────────────────────────────"
echo "IMPORTANT: Manual permission setup"
echo "──────────────────────────────"
echo "1. Run: python eh_permission_fixed.py"
echo "2. Select option 9 (Storage Setup)"
echo "3. Follow the instructions"
echo "──────────────────────────────"
echo "Developer: EH Munna"
echo "Telegram: @ehmunna999"
echo -e "──────────────────────────────\e[0m"
