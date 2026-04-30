import os
import sys
import time
import hashlib

# 🛡️ 1. NIDAAMKA AMNIGA (ANTI-TAMPER SYSTEM)
def check_integrity():
    # Koodkan wuxuu xirayaa bot-ka haddii hal xaraf la beddelo
    # Hash-kan waa inuu u gaar yahay koodkaaga rasmiga ah
    try:
        with open(__file__, "rb") as f:
            # MD5 Hash calculation
            current_hash = hashlib.md5(f.read()).hexdigest()
        
        # Fiiro gaar ah: Haddii aad rabto inaad koodka xirto (Lock), 
        # nuqul ka qaado hash-ka ugu dambeeya oo halkan geli.
        pass
    except:
        pass

# 🎨 KALARADA (VIP COLORS)
G = "\033[1;92m" # Green
Y = "\033[1;93m" # Yellow
R = "\033[1;91m" # Red
B = "\033[1;94m" # Blue
W = "\033[1;97m" # White
C = "\033[1;96m" # Cyan
S = "\033[0m"    # Reset

def sako_banner():
    os.system('clear')
    print(f"{C}="*55)
    print(f"{Y}   ██████  █████  ██   ██  ██████      █████  █████")
    print(f"{Y}   ██      ██   ██ ██  ██  ██  ██      ██ ██  ██ ██")
    print(f"{W}   ██████  ███████ █████   ██  ██      █████  █████")
    print(f"{W}       ██  ██   ██ ██  ██  ██  ██         ██     ██")
    print(f"{R}   ██████  ██   ██ ██   ██ ██████  {G}V5.0   ██     ██")
    print(f"{C}="*55)
    print(f"{W}      [ 🛡️  GHOST CLEANER - SAKO 99 BRAND 🛡️ ]")
    print(f"{C}="*55 + S)

def main_menu():
    sako_banner()
    
    # 📂 HUBINTA FOLDER-KA DATA (DATA FOLDER CHECK)
    if not os.path.exists("/sdcard/Android/data"):
        print(f"{R}❌ [DIGNIIN / WARNING]: Foldarka DATA ma furna! / DATA folder is closed!{S}")
        print(f"{Y}Somali: Zxp, fadlan ifur foldarka Data adigoo mahadsan si aan kuu ilaaliyo.{S}")
        print(f"{W}English: Please open the Data folder to allow the protection to work.{S}")
        print(f"{Y}Albaabka ii fura zxp, si aan 24 saac kuugu adeego! ❤️{S}")
        input(f"\n{G}>>> Riix Enter / Press Enter...{S}")
        main_menu()

    print(f"{G}--- ACTIVE GAME SUPPORT ---{S}")
    games = {
        "1": ["FREE FIRE (Normal)", "com.dts.freefireth"],
        "2": ["FREE FIRE MAX", "com.dts.freefiremax"],
        "3": ["PUBG MOBILE (Global)", "com.tencent.ig"],
        "4": ["PUBG MOBILE (KR)", "com.pubg.krmobile"],
        "5": ["COD MOBILE (CODM)", "com.activision.callofduty.shooter"],
        "6": ["MOBILE LEGENDS", "com.mobile.legends"],
        "7": ["ROBLOX", "com.roblox.client"],
        "8": ["LUDO KING", "com.ludo.king"]
    }

    for k, v in games.items():
        print(f"{B}[{k}] {W}{v[0]}")
    
    print(f"{C}="*55)
    print(f"{R}[0] KA BAX / EXIT{S}")
    
    choice = input(f"\n{G}SAKO-SELECT > {S}")
    
    if choice == "0":
        print(f"{R}Bye! Stay Safe zxp.{S}")
        sys.exit()

    if choice in games:
        game_name = games[choice][0]
        pkg_name = games[choice][1]
        full_path = f"/sdcard/Android/data/{pkg_name}"

        # 🔍 HUBINTA CIYAARTA (GAME DETECTION)
        if not os.path.exists(full_path):
            print(f"\n{R}⚠️ [ERROR]: {game_name} Not Found!{S}")
            print(f"{Y}Somali: Ciyaartan kawayay nidaamkaaga! Fadlan soo dagso zxp.{S}")
            print(f"{W}English: This game was not found on your device! Please install it.{S}")
            time.sleep(4)
            main_menu()
        else:
            print(f"\n{G}✅ {game_name} FOUND!{S}")
            print(f"{Y}Somali: Nadiifinta 24-saac ee GHOST waa bilaabatay...{S}")
            print(f"{W}English: GHOST 24-hour cleaning has started...{S}")
            try:
                while True:
                    # 🧹 EXECUTION (Tirtirista Logs-ka)
                    # Example of paths to clean
                    os.system(f"rm -rf {full_path}/cache/*")
                    os.system(f"rm -rf {full_path}/files/report_info.txt")
                    
                    print(f"[{time.strftime('%H:%M:%S')}] {G}SAKO-99 PROTECTING...{S}", end="\r")
                    time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{R}[!] Stopped. Amnigaaga ayaa muhiim ah! / Safety first!{S}")
    else:
        print(f"{R}Invalid Choice! / Dooro nambar sax ah!{S}")
        time.sleep(2)
        main_menu()

if __name__ == "__main__":
    check_integrity()
    main_menu()
