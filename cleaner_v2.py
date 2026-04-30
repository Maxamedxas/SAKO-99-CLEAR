import hashlib
import sys
import os
import time

# 1. Nidaamka Amniga (Anti-Tamper)
# Nidaamkan wuxuu hubiyaa inaan code-ka xaraf laga beddelin
def check_integrity():
    # Hash-kan hoose waa aqoonsiga code-kaaga SAKO 99
    # Haddii aad xaraf beddesho, waa inaad hash-ka cusub halkan gelisaa
    ORIGINAL_HASH = "8c946e5973b7a5a8f4c28e9376a911043329976378e910243b23c21c32adc62a" 
    
    try:
        with open(__file__, "rb") as f:
            current_hash = hashlib.sha256(f.read()).hexdigest()
        
        # Haddii hash-ka uu isbeddelo, code-ku wuxuu dareemayaa in la taabtay
        if current_hash != ORIGINAL_HASH:
            print("\n\033[1;91m[!] SECURITY BREACH DETECTED!")
            print("[!] SAKO-99 PROTECTOR: Code modification detected. Stopping...\033[0m")
            sys.exit()
    except Exception:
        sys.exit()

# Midabada Hacker-ka (SAKO 99 Style)
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
RED = "\033[1;91m"
BLUE = "\033[1;94m"
RESET = "\033[0m"

# 2. Liiska meelaha Logs-ka ee 5-ta Ciyaarood ee ugu waaweyn
LOG_PATHS = [
    "/sdcard/Android/data/com.dts.freefireth/files/report_info.txt",
    "/sdcard/Android/data/com.dts.freefireth/cache",
    "/sdcard/Android/data/com.dts.freefiremax/files/report_info.txt",
    "/sdcard/Android/data/com.dts.freefiremax/cache",
    "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs",
    "/sdcard/Android/data/com.pubg.krmobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs",
    "/sdcard/Android/data/com.activision.callofduty.shooter/cache",
    "/sdcard/Android/data/com.activision.callofduty.shooter/files/contents",
    "/sdcard/Android/data/com.mobile.legends/cache",
    "/sdcard/Android/data/com.mobile.legends/files/dragon2017/assets/log",
    "/sdcard/Android/data/com.roblox.client/cache",
    "/sdcard/Android/data/com.roblox.client/files/logs"
]

def sako_cleaner_v2():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{GREEN}="*45)
    print(f"      🛡️  SAKO-99 GHOST CLEANER V2  🛡️")
    print(f"      [ MULTI-GAME LOGS REMOVER ]")
    print(f"      STATUS: {YELLOW}ENCRYPTED & PROTECTED")
    print(f"{GREEN}="*45 + RESET)
    print(f"{BLUE}Target Games: FF, FF Max, PUBG, CODM, MLBB, Roblox{RESET}\n")

    while True:
        cleaned_count = 0
        for path in LOG_PATHS:
            if os.path.exists(path):
                os.system(f"rm -rf {path}")
                cleaned_count += 1
        
        current_time = time.strftime("%H:%M:%S")
        if cleaned_count > 0:
            print(f"[{current_time}] {GREEN}SUCCESS:{RESET} Removed {cleaned_count} security logs.")
        else:
            print(f"[{current_time}] {YELLOW}SECURE:{RESET} System is clean. Scanning...", end="\r")
            
        time.sleep(1)

if __name__ == "__main__":
    # check_integrity() # Ka saar '#' si aad u kiciso nidaamka amniga
    try:
        sako_cleaner_v2()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] SAKO-99: Ghost Cleaner Stopped.{RESET}")
