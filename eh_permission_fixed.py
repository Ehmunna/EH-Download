#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import requests
from datetime import datetime
from colorama import init, Fore, Back, Style
from tqdm import tqdm

# Colorama initialize
init(autoreset=True)

# ===========================================
# 🎨 CUSTOM COLORS
# ===========================================
class Colors:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW + Style.BRIGHT
    BLUE = Fore.BLUE + Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    MAGENTA = Fore.MAGENTA + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

# ===========================================
# 📁 STORAGE SETUP
# ===========================================
SD_CARD = "/storage/emulated/0"
DOWNLOAD_BASE = os.path.join(SD_CARD, "EH_Downloads")

# সাব ফোল্ডার
FOLDERS = {
    "youtube": "YouTube",
    "facebook": "Facebook", 
    "instagram": "Instagram",
    "tiktok": "TikTok",
    "google": "Google",
    "audio": "Audio",
    "images": "Images"
}

# ===========================================
# 🎭 CLEAN UI EFFECTS
# ===========================================
def clear_screen():
    """স্ক্রিন ক্লিয়ার"""
    os.system('clear')

def print_slow(text, color=Colors.GREEN, delay=0.03):
    """স্লো প্রিন্ট এফেক্ট"""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(text, duration=1.5):
    """লোডিং এনিমেশন"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        print(f"\r{Colors.CYAN}{chars[i % len(chars)]} {text}{Colors.RESET}", end="")
        time.sleep(0.1)
        i += 1
    print()

def progress_bar(total, desc="Processing"):
    """প্রোগ্রেস বার"""
    for _ in tqdm(range(total), 
                  desc=f"{Colors.YELLOW}{desc}{Colors.RESET}", 
                  bar_format="{l_bar}%s{bar}%s{r_bar}" % (Colors.BLUE, Colors.RESET),
                  ncols=60):
        time.sleep(0.01)

def print_boxed(text, color=Colors.CYAN):
    """বক্সে টেক্সট প্রিন্ট"""
    border = "═" * (len(text) + 4)
    print(f"{color}╔{border}╗")
    print(f"║  {text}  ║")
    print(f"╚{border}╝{Colors.RESET}")

def print_separator(char="─", length=60, color=Colors.CYAN):
    """সেপারেটর লাইন"""
    print(f"{color}{char * length}{Colors.RESET}")

# ===========================================
# 🔓 STORAGE PERMISSION FIX
# ===========================================
def check_and_setup_storage():
    """স্টোরেজ পারমিশন চেক এবং সেটআপ"""
    print(f"\n{Colors.YELLOW}[+] Checking storage permissions...{Colors.RESET}")
    
    # প্রথমে ডিরেক্টরি তৈরি করার চেষ্টা করুন
    try:
        os.makedirs(DOWNLOAD_BASE, exist_ok=True)
        print(f"{Colors.GREEN}[✓] Can create directories{Colors.RESET}")
        
        # টেস্ট ফাইল তৈরি
        test_file = os.path.join(DOWNLOAD_BASE, "test_permission.txt")
        with open(test_file, 'w') as f:
            f.write("EH Downloader Test - Storage is accessible\n")
        
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"{Colors.GREEN}[✓] Can write and delete files{Colors.RESET}")
            return True
        else:
            print(f"{Colors.YELLOW}[!] Need storage permission{Colors.RESET}")
            return False
            
    except PermissionError:
        print(f"{Colors.YELLOW}[!] Storage permission needed{Colors.RESET}")
        return False
    except Exception as e:
        print(f"{Colors.YELLOW}[!] Storage issue: {str(e)}{Colors.RESET}")
        return False

def setup_storage_manual():
    """ম্যানুয়াল স্টোরেজ সেটআপ"""
    print(f"\n{Colors.CYAN}{'═'*60}")
    print_boxed("STORAGE SETUP INSTRUCTIONS", Colors.YELLOW)
    print(f"{Colors.CYAN}{'═'*60}{Colors.RESET}")
    
    print(f"\n{Colors.WHITE}Please follow these steps:{Colors.RESET}")
    print(f"{Colors.GREEN}1.{Colors.RESET} Open Termux app")
    print(f"{Colors.GREEN}2.{Colors.RESET} Run this command:")
    print(f"   {Colors.CYAN}termux-setup-storage{Colors.RESET}")
    print(f"{Colors.GREEN}3.{Colors.RESET} A popup will appear")
    print(f"{Colors.GREEN}4.{Colors.RESET} Click {Colors.YELLOW}'ALLOW'{Colors.RESET} or {Colors.YELLOW}'হ্যাঁ'{Colors.RESET}")
    print(f"{Colors.GREEN}5.{Colors.RESET} Come back here and press Enter")
    
    input(f"\n{Colors.YELLOW}[↵] Press Enter after granting permission...{Colors.RESET}")
    
    # আবার চেক
    return check_and_setup_storage()

def create_folders_manual():
    """ম্যানুয়ালি ফোল্ডার তৈরি"""
    print(f"\n{Colors.YELLOW}[+] Creating directories...{Colors.RESET}")
    
    try:
        # মেইন ডাউনলোড ফোল্ডার
        os.makedirs(DOWNLOAD_BASE, exist_ok=True)
        
        # সব সাবফোল্ডার
        for folder in FOLDERS.values():
            folder_path = os.path.join(DOWNLOAD_BASE, folder)
            os.makedirs(folder_path, exist_ok=True)
            print(f"{Colors.GREEN}  ✓ {folder}{Colors.RESET}")
        
        print(f"{Colors.GREEN}[✓] All directories created!{Colors.RESET}")
        return True
        
    except Exception as e:
        print(f"{Colors.RED}[✗] Error creating directories: {str(e)}{Colors.RESET}")
        return False

# ===========================================
# 🏆 EH BANNER
# ===========================================
def show_banner():
    """EH ব্যানার"""
    clear_screen()
    
    # EH ASCII Art
    print(f"{Colors.RED}")
    print("███████╗██╗  ██╗")
    print("██╔════╝██║  ██║")
    print("█████╗  ███████║")
    print("██╔══╝  ██╔══██║")
    print("███████╗██║  ██║")
    print("╚══════╝╚═╝  ╚═╝")
    print(f"{Colors.RESET}")
    
    print_separator("━", 30, Colors.RED)
    
    # Developer Info
    print(f"\n{Colors.GREEN}╭──────────────────────────────╮")
    print(f"│     {Colors.YELLOW}DEVELOPER INFO{Colors.GREEN}        │")
    print(f"├──────────────────────────────┤")
    print(f"│ {Colors.CYAN}Facebook{Colors.RESET}: EH Munna       {Colors.GREEN}│")
    print(f"│ {Colors.BLUE}Telegram{Colors.RESET}: @ehmunna999    {Colors.GREEN}│")
    print(f"╰──────────────────────────────╯{Colors.RESET}")
    
    # Current Time
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    print(f"\n{Colors.YELLOW}⏰ Time: {current_time}")
    print(f"📅 Date: {current_date}")
    print(f"📁 Storage: {DOWNLOAD_BASE}")
    
    # Storage status
    if os.path.exists(DOWNLOAD_BASE):
        print(f"🔓 Status: {Colors.GREEN}ACCESSIBLE{Colors.RESET}")
    else:
        print(f"🔒 Status: {Colors.RED}RESTRICTED{Colors.RESET}")
    
    print_separator("━", 60, Colors.CYAN)

# ===========================================
# 🎬 DOWNLOADER FUNCTIONS
# ===========================================
def download_with_progress(url, cmd, platform, quality):
    """প্রোগ্রেস সহ ডাউনলোড"""
    print(f"\n{Colors.CYAN}{'━'*60}")
    print_boxed(f"DOWNLOADING {platform.upper()}", Colors.YELLOW)
    print(f"{Colors.CYAN}{'━'*60}{Colors.RESET}")
    
    print(f"\n{Colors.WHITE}Platform: {Colors.GREEN}{platform}")
    print(f"{Colors.WHITE}Quality:  {Colors.BLUE}{quality}")
    if url:
        print(f"{Colors.WHITE}URL:      {Colors.CYAN}{url[:40]}...{Colors.RESET}")
    
    # Connection animation
    print(f"\n{Colors.BLUE}[•] Connecting...{Colors.RESET}")
    progress_bar(50, "Establishing connection")
    
    # Download animation
    print(f"\n{Colors.GREEN}[↓] Downloading...{Colors.RESET}")
    
    try:
        # Run command
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if process.returncode == 0:
            print(f"\n{Colors.GREEN}{'━'*60}")
            print_boxed("DOWNLOAD COMPLETED", Colors.GREEN)
            print(f"{Colors.GREEN}{'━'*60}{Colors.RESET}")
            return True
        else:
            print(f"\n{Colors.RED}{'━'*60}")
            print_boxed("DOWNLOAD FAILED", Colors.RED)
            print(f"{Colors.RED}Error: {process.stderr[:100]}{Colors.RESET}")
            print(f"{Colors.RED}{'━'*60}{Colors.RESET}")
            return False
            
    except Exception as e:
        print(f"\n{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")
        return False

# ===========================================
# 📥 YOUTUBE DOWNLOADER (FIXED FORMATS)
# ===========================================
def youtube_downloader():
    """ইউটিউব ডাউনলোডার - MP4 ফরম্যাট নিশ্চিত"""
    show_banner()
    print_boxed("YOUTUBE DOWNLOADER", Colors.RED)
    
    url = input(f"\n{Colors.YELLOW}[?] YouTube URL: {Colors.RESET}").strip()
    if not url:
        print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}[1] 4K Ultra HD (MP4)")
    print(f"{Colors.CYAN}[2] 1080p Full HD (MP4)")
    print(f"{Colors.CYAN}[3] 720p HD (MP4)")
    print(f"{Colors.CYAN}[4] 480p SD (MP4)")
    print(f"{Colors.CYAN}[5] MP3 320kbps (Audio)")
    print(f"{Colors.CYAN}[6] MP3 128kbps (Audio){Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select option (1-6): {Colors.RESET}").strip()
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["youtube"])
    
    try:
        if choice == "1":
            cmd = f'yt-dlp -f "bestvideo[height<=2160][ext=mp4]+bestaudio[ext=m4a]/best[height<=2160][ext=mp4]" --merge-output-format mp4 -o "{download_path}/%(title)s_4K.mp4" "{url}"'
            quality = "4K MP4"
        elif choice == "2":
            cmd = f'yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]" --merge-output-format mp4 -o "{download_path}/%(title)s_1080p.mp4" "{url}"'
            quality = "1080p MP4"
        elif choice == "3":
            cmd = f'yt-dlp -f "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]" --merge-output-format mp4 -o "{download_path}/%(title)s_720p.mp4" "{url}"'
            quality = "720p MP4"
        elif choice == "4":
            cmd = f'yt-dlp -f "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]" --merge-output-format mp4 -o "{download_path}/%(title)s_480p.mp4" "{url}"'
            quality = "480p MP4"
        elif choice == "5":
            cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 320k -o "{download_path}/%(title)s_320kbps.mp3" "{url}"'
            quality = "MP3 320kbps"
        elif choice == "6":
            cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 128k -o "{download_path}/%(title)s_128kbps.mp3" "{url}"'
            quality = "MP3 128kbps"
        else:
            cmd = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --merge-output-format mp4 -o "{download_path}/%(title)s.mp4" "{url}"'
            quality = "Best Quality MP4"
        
        print(f"\n{Colors.BLUE}[+] Format: {quality}{Colors.RESET}")
        
        if download_with_progress(url, cmd, "YouTube", quality):
            print(f"\n{Colors.GREEN}📁 Saved to: {download_path}{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 📘 FACEBOOK DOWNLOADER
# ===========================================
def facebook_downloader():
    """ফেসবুক ডাউনলোডার"""
    show_banner()
    print_boxed("FACEBOOK DOWNLOADER", Colors.BLUE)
    
    url = input(f"\n{Colors.YELLOW}[?] Facebook URL: {Colors.RESET}").strip()
    if not url:
        print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}[1] HD Quality (MP4)")
    print(f"{Colors.CYAN}[2] SD Quality (MP4)")
    print(f"{Colors.CYAN}[3] Audio Only (MP3){Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select quality (1-3): {Colors.RESET}").strip()
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["facebook"])
    
    try:
        if choice == "1":
            cmd = f'yt-dlp -f "hd" --merge-output-format mp4 -o "{download_path}/%(title)s_HD.mp4" "{url}"'
            quality = "HD MP4"
        elif choice == "2":
            cmd = f'yt-dlp -f "sd" --merge-output-format mp4 -o "{download_path}/%(title)s_SD.mp4" "{url}"'
            quality = "SD MP4"
        elif choice == "3":
            cmd = f'yt-dlp -x --audio-format mp3 -o "{download_path}/%(title)s_Audio.mp3" "{url}"'
            quality = "MP3 Audio"
        else:
            cmd = f'yt-dlp -f "best" --merge-output-format mp4 -o "{download_path}/%(title)s.mp4" "{url}"'
            quality = "Best Quality MP4"
        
        print(f"\n{Colors.BLUE}[+] Format: {quality}{Colors.RESET}")
        
        if download_with_progress(url, cmd, "Facebook", quality):
            print(f"\n{Colors.GREEN}📁 Saved to: {download_path}{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 📷 INSTAGRAM DOWNLOADER
# ===========================================
def instagram_downloader():
    """ইনস্টাগ্রাম ডাউনলোডার"""
    show_banner()
    print_boxed("INSTAGRAM DOWNLOADER", Colors.MAGENTA)
    
    print(f"\n{Colors.CYAN}[1] Post/Video (MP4)")
    print(f"{Colors.CYAN}[2] Reels (MP4)")
    print(f"{Colors.CYAN}[3] Photo (JPG){Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select type (1-3): {Colors.RESET}").strip()
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["instagram"])
    
    try:
        if choice in ["1", "2"]:
            url = input(f"\n{Colors.YELLOW}[?] Instagram URL: {Colors.RESET}").strip()
            if not url:
                print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
                return
            
            cmd = f'yt-dlp -f "best" --merge-output-format mp4 -o "{download_path}/%(title)s.mp4" "{url}"'
            platform = "Instagram"
            quality = "MP4"
        
        elif choice == "3":
            url = input(f"\n{Colors.YELLOW}[?] Instagram Photo URL: {Colors.RESET}").strip()
            if not url:
                print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
                return
            
            # Direct image download
            filename = f"instagram_{int(time.time())}.jpg"
            filepath = os.path.join(download_path, filename)
            
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, stream=True)
            
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"{Colors.GREEN}[✓] Photo downloaded: {filename}{Colors.RESET}")
                return
            else:
                print(f"{Colors.RED}[✗] Failed to download photo{Colors.RESET}")
                return
        
        else:
            print(f"{Colors.RED}[!] Invalid choice{Colors.RESET}")
            return
        
        print(f"\n{Colors.BLUE}[+] Format: {quality}{Colors.RESET}")
        
        if download_with_progress("", cmd, platform, quality):
            print(f"\n{Colors.GREEN}📁 Saved to: {download_path}{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 🎵 TIKTOK DOWNLOADER (SIMPLE VERSION)
# ===========================================
def tiktok_downloader():
    """টিকটক ডাউনলোডার - শুধু মেইন ডাউনলোড"""
    show_banner()
    print_boxed("TIKTOK DOWNLOADER", Colors.CYAN)
    
    url = input(f"\n{Colors.YELLOW}[?] TikTok URL: {Colors.RESET}").strip()
    if not url:
        print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}[1] Video (MP4)")
    print(f"{Colors.CYAN}[2] Audio Only (MP3){Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select option (1-2): {Colors.RESET}").strip()
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["tiktok"])
    
    try:
        if choice == "1":
            cmd = f'yt-dlp -f "best" --merge-output-format mp4 -o "{download_path}/%(title)s.mp4" "{url}"'
            quality = "MP4 Video"
        elif choice == "2":
            cmd = f'yt-dlp -x --audio-format mp3 -o "{download_path}/%(title)s_Audio.mp3" "{url}"'
            quality = "MP3 Audio"
        else:
            cmd = f'yt-dlp -f "best" --merge-output-format mp4 -o "{download_path}/%(title)s.mp4" "{url}"'
            quality = "MP4 Video"
        
        print(f"\n{Colors.BLUE}[+] Format: {quality}{Colors.RESET}")
        
        if download_with_progress(url, cmd, "TikTok", quality):
            print(f"\n{Colors.GREEN}📁 Saved to: {download_path}{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 🔍 GOOGLE DOWNLOADER
# ===========================================
def google_downloader():
    """গুগল/সাধারণ ডাউনলোডার"""
    show_banner()
    print_boxed("GOOGLE DOWNLOADER", Colors.YELLOW)
    
    url = input(f"\n{Colors.YELLOW}[?] Enter direct download URL: {Colors.RESET}").strip()
    if not url:
        print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
        return
    
    # ফাইলের নাম বের করুন
    filename = os.path.basename(url).split('?')[0]
    if not filename or '.' not in filename:
        filename = f"download_{int(time.time())}.mp4"
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["google"])
    
    print(f"\n{Colors.CYAN}[1] Fast Download (wget)")
    print(f"{Colors.CYAN}[2] Resume Support (curl){Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select method (1-2): {Colors.RESET}").strip()
    
    try:
        if choice == "1":
            cmd = f'wget -c --show-progress -O "{download_path}/{filename}" "{url}"'
            method = "wget"
        elif choice == "2":
            cmd = f'curl -L -# -o "{download_path}/{filename}" "{url}"'
            method = "curl"
        else:
            cmd = f'wget -c -O "{download_path}/{filename}" "{url}"'
            method = "wget"
        
        print(f"\n{Colors.BLUE}[+] Method: {method}{Colors.RESET}")
        print(f"{Colors.BLUE}[+] File: {filename}{Colors.RESET}")
        
        if download_with_progress(url, cmd, "Google", "Direct Download"):
            filepath = os.path.join(download_path, filename)
            if os.path.exists(filepath):
                size = os.path.getsize(filepath) / (1024 * 1024)
                print(f"\n{Colors.GREEN}📁 Saved to: {filepath}")
                print(f"📦 Size: {size:.2f} MB{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 🎵 AUDIO DOWNLOADER
# ===========================================
def audio_downloader():
    """অডিও ডাউনলোডার"""
    show_banner()
    print_boxed("AUDIO DOWNLOADER", Colors.GREEN)
    
    url = input(f"\n{Colors.YELLOW}[?] Video URL: {Colors.RESET}").strip()
    if not url:
        print(f"{Colors.RED}[!] No URL provided{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}[1] MP3 320kbps (Best)")
    print(f"{Colors.CYAN}[2] MP3 192kbps (High)")
    print(f"{Colors.CYAN}[3] MP3 128kbps (Medium)")
    print(f"{Colors.CYAN}[4] M4A Format{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select quality (1-4): {Colors.RESET}").strip()
    
    download_path = os.path.join(DOWNLOAD_BASE, FOLDERS["audio"])
    
    try:
        if choice == "1":
            cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 320k -o "{download_path}/%(title)s_320kbps.mp3" "{url}"'
            quality = "MP3 320kbps"
        elif choice == "2":
            cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 192k -o "{download_path}/%(title)s_192kbps.mp3" "{url}"'
            quality = "MP3 192kbps"
        elif choice == "3":
            cmd = f'yt-dlp -x --audio-format mp3 --audio-quality 128k -o "{download_path}/%(title)s_128kbps.mp3" "{url}"'
            quality = "MP3 128kbps"
        elif choice == "4":
            cmd = f'yt-dlp -x --audio-format m4a -o "{download_path}/%(title)s.m4a" "{url}"'
            quality = "M4A Format"
        else:
            cmd = f'yt-dlp -x --audio-format mp3 -o "{download_path}/%(title)s.mp3" "{url}"'
            quality = "MP3 Default"
        
        print(f"\n{Colors.BLUE}[+] Format: {quality}{Colors.RESET}")
        
        if download_with_progress(url, cmd, "Audio", quality):
            print(f"\n{Colors.GREEN}🎵 Saved to: {download_path}{Colors.RESET}")
    
    except Exception as e:
        print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")

# ===========================================
# 📂 UTILITY FUNCTIONS
# ===========================================
def open_folder():
    """ফোল্ডার ওপেন"""
    show_banner()
    print_boxed("OPEN DOWNLOADS", Colors.GREEN)
    
    if os.path.exists(DOWNLOAD_BASE):
        print(f"\n{Colors.YELLOW}[+] Opening folder...{Colors.RESET}")
        loading_animation("Accessing storage", 1)
        
        try:
            subprocess.run(f"termux-open {DOWNLOAD_BASE}", shell=True, capture_output=True)
            print(f"{Colors.GREEN}[✓] Folder opened!{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}[!] Could not open file manager{Colors.RESET}")
            print(f"{Colors.CYAN}Manual path: {DOWNLOAD_BASE}{Colors.RESET}")
    else:
        print(f"{Colors.RED}[✗] Folder not found!{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Run storage setup first{Colors.RESET}")

def show_stats():
    """স্ট্যাটস দেখান"""
    show_banner()
    print_boxed("SYSTEM STATISTICS", Colors.CYAN)
    
    if not os.path.exists(DOWNLOAD_BASE):
        print(f"\n{Colors.RED}[✗] Download folder not found!{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Please setup storage first{Colors.RESET}")
        return
    
    total_size = 0
    print(f"\n{Colors.YELLOW}📊 Storage Usage:{Colors.RESET}")
    
    for folder in FOLDERS.values():
        folder_path = os.path.join(DOWNLOAD_BASE, folder)
        if os.path.exists(folder_path):
            size = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.exists(fp):
                        size += os.path.getsize(fp)
            total_size += size
            size_mb = size / (1024 * 1024)
            if size_mb > 0:
                print(f"{Colors.GREEN}  {folder}: {size_mb:.1f} MB{Colors.RESET}")
    
    total_mb = total_size / (1024 * 1024)
    print(f"\n{Colors.BLUE}📦 Total: {total_mb:.1f} MB{Colors.RESET}")
    print(f"{Colors.BLUE}📁 Location: {DOWNLOAD_BASE}{Colors.RESET}")

# ===========================================
# ⚙️ STORAGE SETUP MENU
# ===========================================
def storage_setup_menu():
    """স্টোরেজ সেটআপ মেনু"""
    show_banner()
    print_boxed("STORAGE SETUP", Colors.YELLOW)
    
    print(f"\n{Colors.WHITE}Storage access is required for downloads.{Colors.RESET}")
    print(f"{Colors.CYAN}Choose an option:{Colors.RESET}")
    print(f"\n{Colors.GREEN}[1] Setup storage automatically")
    print(f"{Colors.GREEN}[2] Setup storage manually")
    print(f"{Colors.GREEN}[3] Check current status")
    print(f"{Colors.GREEN}[4] Back to main menu{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select option (1-4): {Colors.RESET}").strip()
    
    if choice == "1":
        print(f"\n{Colors.YELLOW}[+] Setting up storage automatically...{Colors.RESET}")
        
        try:
            # Try to run termux-setup-storage
            result = subprocess.run("termux-setup-storage", shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"{Colors.GREEN}[✓] Storage setup initiated{Colors.RESET}")
                print(f"{Colors.YELLOW}[!] Please check your phone for permission popup{Colors.RESET}")
                print(f"{Colors.YELLOW}[!] Click 'ALLOW' or 'হ্যাঁ' when prompted{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}[!] Could not setup automatically{Colors.RESET}")
                print(f"{Colors.CYAN}Trying manual method...{Colors.RESET}")
                setup_storage_manual()
            
            time.sleep(3)
            
            # Check if successful
            if check_and_setup_storage():
                create_folders_manual()
                input(f"\n{Colors.YELLOW}[↵] Press Enter to continue...{Colors.RESET}")
                return True
            else:
                print(f"{Colors.RED}[✗] Storage setup failed{Colors.RESET}")
                input(f"\n{Colors.YELLOW}[↵] Press Enter to continue...{Colors.RESET}")
                return False
                
        except Exception as e:
            print(f"{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")
            return False
    
    elif choice == "2":
        if setup_storage_manual():
            create_folders_manual()
            return True
        else:
            return False
    
    elif choice == "3":
        if check_and_setup_storage():
            print(f"\n{Colors.GREEN}[✓] Storage is accessible{Colors.RESET}")
            print(f"{Colors.GREEN}[✓] Download folder: {DOWNLOAD_BASE}{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}[✗] Storage is not accessible{Colors.RESET}")
            print(f"{Colors.YELLOW}[!] Please setup storage first{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}[↵] Press Enter to continue...{Colors.RESET}")
    
    elif choice == "4":
        return False
    
    return False

# ===========================================
# 📱 MAIN MENU
# ===========================================
def main_menu():
    """মেইন মেনু"""
    # প্রথমে স্টোরেজ চেক
    if not os.path.exists(DOWNLOAD_BASE):
        print(f"\n{Colors.YELLOW}[!] Storage not setup{Colors.RESET}")
        storage_setup_menu()
    
    while True:
        show_banner()
        
        print(f"\n{Colors.CYAN}┌─────────────── MENU ───────────────┐")
        print(f"│  {Colors.RED}1.{Colors.RESET} 🎬 YouTube Downloader       │")
        print(f"│  {Colors.BLUE}2.{Colors.RESET} 📘 Facebook Downloader      │")
        print(f"│  {Colors.MAGENTA}3.{Colors.RESET} 📷 Instagram Downloader     │")
        print(f"│  {Colors.CYAN}4.{Colors.RESET} 🎵 TikTok Downloader        │")
        print(f"│  {Colors.YELLOW}5.{Colors.RESET} 🔍 Google Downloader        │")
        print(f"│  {Colors.GREEN}6.{Colors.RESET} 🎵 Audio Downloader         │")
        print(f"│  {Colors.BLUE}7.{Colors.RESET} 📂 Open Downloads Folder    │")
        print(f"│  {Colors.CYAN}8.{Colors.RESET} 📊 System Statistics         │")
        print(f"│  {Colors.YELLOW}9.{Colors.RESET} ⚙️ Storage Setup            │")
        print(f"│  {Colors.RED}0.{Colors.RESET} 🚪 Exit Program              │")
        print(f"└──────────────────────────────────────┘{Colors.RESET}")
        
        print_separator("─", 40, Colors.CYAN)
        
        choice = input(f"\n{Colors.YELLOW}[?] Select option (0-9): {Colors.RESET}").strip()
        
        if choice == "1":
            youtube_downloader()
        elif choice == "2":
            facebook_downloader()
        elif choice == "3":
            instagram_downloader()
        elif choice == "4":
            tiktok_downloader()
        elif choice == "5":
            google_downloader()
        elif choice == "6":
            audio_downloader()
        elif choice == "7":
            open_folder()
        elif choice == "8":
            show_stats()
        elif choice == "9":
            storage_setup_menu()
        elif choice == "0":
            print(f"\n{Colors.RED}{'━'*40}")
            print(f"{Colors.YELLOW}👋 Thank you for using EH Downloader!")
            print(f"{Colors.GREEN}📁 Files saved in: {DOWNLOAD_BASE}")
            print(f"{Colors.BLUE}📞 Contact: @ehmunna999")
            print(f"{Colors.RED}{'━'*40}{Colors.RESET}")
            time.sleep(2)
            sys.exit(0)
        else:
            print(f"{Colors.RED}[!] Invalid option{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}[↵] Press Enter to continue...{Colors.RESET}")

# ===========================================
# 🚀 PROGRAM START
# ===========================================
if __name__ == "__main__":
    try:
        # Initial setup
        clear_screen()
        print_slow(f"{Colors.RED}Initializing EH Downloader...{Colors.RESET}", Colors.RED, 0.05)
        time.sleep(1)
        
        # Check Python and packages
        print(f"\n{Colors.YELLOW}[+] Checking requirements...{Colors.RESET}")
        
        try:
            import yt_dlp
            print(f"{Colors.GREEN}[✓] yt-dlp installed{Colors.RESET}")
        except:
            print(f"{Colors.RED}[✗] yt-dlp not installed{Colors.RESET}")
            print(f"{Colors.YELLOW}[!] Installing yt-dlp...{Colors.RESET}")
            subprocess.run("pip install yt-dlp", shell=True, capture_output=True)
        
        # Start main program
        loading_animation("Loading EH Downloader", 2)
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program interrupted{Colors.RESET}")
        print(f"{Colors.GREEN}[✓] Files saved in: {DOWNLOAD_BASE}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[✗] Error: {str(e)}{Colors.RESET}")
