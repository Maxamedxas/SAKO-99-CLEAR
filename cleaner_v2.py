import os
import time
import sys

# Midabada SAKO 99 Style
GREEN, YELLOW, RED, BLUE, RESET = "\033[1;92m", "\033[1;93m", "\033[1;91m", "\033[1;94m", "\033[0m"

def sako_header():
    os.system('clear')
    print(f"{GREEN}="*45)
    print(f"      🛡️  SAKO-99 GHOST CLEANER (CLEAR) 🛡️")
    print(f"      [ STATUS: ACTIVE | MODE: PRIVATE ]")
    print(f"{GREEN}="*45 + RESET)

def main():
    sako_header()
    # Farriinta Shizuku
    print(f"{YELLOW}[!] MUHIIM: Fadlan fur foldarka DATA ee mobile-kaaga.")
    print(f"[!] Shizuku shido si aan foldarkaas u galo (Albaabka ii fur).{RESET}")
    print(f"{BLUE}---{RESET}")
    input(f"{GREEN}Riix Enter markaad foldarka furto...{RESET}")
    
    sako_header()
    print(f"{BLUE}Dooro ciyaarta aad rabto inaan nadiifiyo:{RESET}")
    print(f"1. Free Fire (Normal)")
    print(f"2. Free Fire Max")
    print(f"3. PUBG Mobile")
    print(f"4. Dhammaan (All Games)")
    
    choice = input(f"\n{BLUE}SAKO-SELECT > {RESET}")
    
    # Dariiqyada (Paths)
    paths = {
        "1": ["/sdcard/Android/data/com.dts.freefireth/files/report_info.txt", "/sdcard/Android/data/com.dts.freefireth/cache"],
        "2": ["/sdcard/Android/data/com.dts.freefiremax/files/report_info.txt", "/sdcard/Android/data/com.dts.freefiremax/cache"],
        "3": ["/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs"],
    }

    target = []
    if choice == "4":
        for p in paths.values(): target.extend(p)
    elif choice in paths:
        target = paths[choice]
    else:
        print(f"{RED}Dooro nambar sax ah!{RESET}")
        return

    print(f"\n{YELLOW}[*] Nadiifintu waa bilaabatay...{RESET}")
    while True:
        try:
            for p in target:
                if os.path.exists(p):
                    os.system(f"rm -rf {p}")
            print(f"[{time.strftime('%H:%M:%S')}] {GREEN}System is Clean!{RESET}", end="\r")
            time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n{RED}[!] SAKO-99: Joojiyay.{RESET}")
            break

if __name__ == "__main__":
    main()
