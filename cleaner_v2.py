import hashlib
import sys
import os
import time

# Midabada (SAKO 99 Style)
GREEN, YELLOW, RED, BLUE, RESET = "\033[1;92m", "\033[1;93m", "\033[1;91m", "\033[1;94m", "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def sako_header():
    print(f"{GREEN}="*45)
    print(f"      🛡️  SAKO-99 GHOST CLEANER V3  🛡️")
    print(f"      [ PRIVATE LOGS REMOVER ]")
    print(f"{GREEN}="*45 + RESET)

def start_shizuku_msg():
    clear_screen()
    sako_header()
    print(f"{YELLOW}[!] MUHIIM: Fadlan horta fur foldarka DATA ee mobile-kaaga.")
    print(f"[!] Shizuku shid si uu iigu furmo albaabka nidaamka (Rootless Access).{RESET}")
    print(f"{BLUE}---{RESET}")
    input(f"{GREEN}Riix Enter markaad Shizuku shidid si aad u sii wadid...{RESET}")

def cleaner_engine(paths):
    clear_screen()
    sako_header()
    print(f"{BLUE}STATUS: {YELLOW}AUTO-CLEANING ACTIVE...{RESET}\n")
    try:
        while True:
            cleaned_count = 0
            for path in paths:
                if os.path.exists(path):
                    os.system(f"rm -rf {path}")
                    cleaned_count += 1
            
            current_time = time.strftime("%H:%M:%S")
            if cleaned_count > 0:
                print(f"[{current_time}] {GREEN}SUCCESS:{RESET} Removed {cleaned_count} security logs.")
            else:
                print(f"[{current_time}] {YELLOW}SECURE:{RESET} System Clean. Scanning...", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] SAKO-99: Ghost Cleaner Stopped.{RESET}")

def main():
    start_shizuku_msg()
    clear_screen()
    sako_header()
    
    print(f"{BLUE}Dooro ciyaarta aad rabto inaan nadiifiyo:{RESET}")
    print(f"{GREEN}1.{RESET} Free Fire (Normal)")
    print(f"{GREEN}2.{RESET} Free Fire Max")
    print(f"{GREEN}3.{RESET} PUBG Mobile (Global/KR)")
    print(f"{GREEN}4.{RESET} Call of Duty (CODM)")
    print(f"{GREEN}5.{RESET} Mobile Legends (MLBB)")
    print(f"{GREEN}6.{RESET} Roblox")
    print(f"{GREEN}7.{RESET} {YELLOW}ALL GAMES (Nadiifi Dhammaan){RESET}")
    print(f"{RED}0. EXIT{RESET}")
    
    choice = input(f"\n{BLUE}SAKO-SELECT > {RESET}")

    # Map-ka Paths-ka
    game_paths = {
        "1": ["/sdcard/Android/data/com.dts.freefireth/files/report_info.txt", "/sdcard/Android/data/com.dts.freefireth/cache"],
        "2": ["/sdcard/Android/data/com.dts.freefiremax/files/report_info.txt", "/sdcard/Android/data/com.dts.freefiremax/cache"],
        "3": ["/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs", "/sdcard/Android/data/com.pubg.krmobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs"],
        "4": ["/sdcard/Android/data/com.activision.callofduty.shooter/cache", "/sdcard/Android/data/com.activision.callofduty.shooter/files/contents"],
        "5": ["/sdcard/Android/data/com.mobile.legends/cache", "/sdcard/Android/data/com.mobile.legends/files/dragon2017/assets/log"],
        "6": ["/sdcard/Android/data/com.roblox.client/cache", "/sdcard/Android/data/com.roblox.client/files/logs"],
    }

    if choice == "0":
        sys.exit()
    elif choice == "7":
        all_paths = []
        for p in game_paths.values(): all_paths.extend(p)
        cleaner_engine(all_paths)
    elif choice in game_paths:
        cleaner_engine(game_paths[choice])
    else:
        print(f"{RED}Dooro nambar sax ah zxp!{RESET}")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
