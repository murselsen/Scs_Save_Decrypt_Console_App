import ctypes.wintypes
import logging
import os
import shutil
import sys
import time

logging.basicConfig(filename="info.log", level=logging.INFO)
logging.basicConfig(filename="crash.log", level=logging.ERROR)

CSIDL_PERSONAL = 5  # My Documents
SHGFP_TYPE_CURRENT = 0  # Get current, not default value

global result, appMainPath, buf, myDocuments, gameList, SII_exe, active_profile, active_save, profileTable, saveTable

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(
    None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf
)
myDocumentsPath = buf.value
print("*****************************************************************")
print("*                                                               *")
print("*      【Product Name : Scs Games - Save SII Decrypt】          *")
print("*      【Author: MQuel】                                        *")
print("*      【Github: github@murselsen】                             *")
print("*      【Discord: 35mursel】                                    *")
print("*      【Version: v1】                        b                 *")
print("*      【License: 2025 - 2030】                                 *")
print("*                                                               *")
print("*****************************************************************")
print("*                                                               *")
print("*      --gameName: (required)                                   *")
print("*                                                               *")
print("*      ets : Euro Truck Simulator 2                             *")
print("*      ats : American Truck Simulator                           *")
print("*                                                               *")
print("*      --profileDisplayName: (required)                         *")
print("*                                                               *")
print("*      --saveDisplayName: (required)                            *")
print("*                                                               *")
print("*****************************************************************")


profileTable = {"ID": [], "Profile": [], "Path": []}
gameList = {"ets": "Euro Truck Simulator 2", "ats": "American Truck Simulator"}
gameSII_exe = os.path.join(os.getcwd(), "gameDecrypt.exe")
infoSII_exe = os.path.join(os.getcwd(), "infoDecrypt.exe")


def exit(status):
    if status:
        input("🚪 | Press any key to exit :")
    else:
        return True


def existsGameDecryptExe(savePath):
    gameSiiExePath = os.path.join(savePath, "gameDecrypt.exe")
    if os.path.exists(gameSiiExePath):
        logging.error(" | Error: gameDecrypt.exe file exists.")
        return True
    else:
        logging.error(" | Error: gameDecrypt.exe file does not exist.")
        return False


def existsInfoDecryptExe(savePath):
    infoSiiExePath = os.path.join(savePath, "infoDecrypt.exe")
    if os.path.exists(infoSiiExePath):
        logging.error(" | Error: infoDecrypt.exe file exists.")
        return True
    else:
        logging.error(" | Error: infoDecrypt.exe file does not exist.")
        return False


def decryptGame():
    print("📂 | Game - Current Directory:", os.getcwd())
    print("🔔 | Status: copying gameDecrypt.exe. Please Wait!")
    time.sleep(1.0)
    shutil.copyfile(gameSII_exe, os.getcwd() + "/gameDecrypt.exe")
    existsGameDecryptExe(os.getcwd()) if print(
        "🔔 | Status: gameDecrypt.exe has been copied.") else False
    time.sleep(1.0)
    cmdGaneDecrypt = "gameDecrypt.exe game.sii"
    os.system(cmdGaneDecrypt)
    time.sleep(2.0)
    os.remove("gameDecrypt.exe")
    print("\n🔔 | Status: gameDecrypt.exe has been removed. Please Wait!")
    time.sleep(1.0)
    


def decryptInfo():
    print("📂 | Info - Current Directory:", os.getcwd()) 
    print("🔔 | Status: copying infoDecrypt.exe. Please Wait!")
    time.sleep(1.0)
    shutil.copyfile(infoSII_exe, os.getcwd() + "/infoDecrypt.exe")
    existsGameDecryptExe(os.getcwd()) if print(
        "🔔 | Status: infoDecrypt.exe has been copied.") else False
    time.sleep(1.0)
    cmdGaneDecrypt = "infoDecrypt.exe info.sii"
    os.system(cmdGaneDecrypt)
    time.sleep(2.0)
    os.remove("infoDecrypt.exe")
    print("\n🔔 | Status: infoDecrypt.exe has been removed. Please Wait!")
    time.sleep(1.0)
    


def main():

    def cwd():
        label = "📂 | Where I am:  |"
        labelLength = len(label)
        cwd = os.getcwd() + " |"
        cwdLength = len(cwd)
        print(
            "\n+",
            "-".center(labelLength - 1, "-"),
            "+",
            "-".center(cwdLength - 2, "-"),
            "+",
        )
        print("|", label, cwd)
        print(
            "+",
            "-".center(labelLength - 1, "-"),
            "+",
            "-".center(cwdLength - 2, "-"),
            "+\n",
        )
    # Index: 0
    # Path: 45545332424F52444F
    # Profile
    # Index: 1
    # Path: 52544853617665
    # Profile
    # Index: 2
    # Path: 666F72756D2E776F746D702E636F6D

    for index, game in enumerate(gameList):
        print("🎮|App :", gameList.get(game))
    if len(sys.argv) < 2:
        print("\n❌ | Error | ❌ \nℹ️ | Error: --gameName argument is required.")
        logging.error(" | Error: --gameName argument is required.")

    else:
        if sys.argv[1] == "ets" or sys.argv[1] == "ats":
            _selectGame = sys.argv[1]
            _selectGameResult = gameList.get(_selectGame)
            print("\nSelect Game: ", _selectGameResult)
            for index, game in enumerate(os.listdir(os.path.join(myDocumentsPath, _selectGameResult, "profiles"))):
                index = index + 1
                print("🎮| Profile -", index, ":", game)

            if len(sys.argv) < 3:
                print(
                    "\n❌ | Error | ❌ \nℹ️ | Error: --profileDisplayName argument is required.")
                logging.error(
                    " | Error: --profileDisplayName argument is required.")

            elif (len(sys.argv) < 4):
                _selectProfile = sys.argv[2]
                print("\n👤| Select Profile : ", _selectProfile)
                for index, save in enumerate(os.listdir(os.path.join(myDocumentsPath, _selectGameResult, "profiles", _selectProfile, "save"))):
                    index = index + 1
                    print("🎫| Save -", index, ":", save)

                print(
                    "\n❌ | Error | ❌ \nℹ️ | Error: --saveDisplayName argument is required.")
                logging.error(
                    " | Error: --saveDisplayName argument is required."),

            elif len(sys.argv) == 4:

                # Selected Profile
                _selectProfile = sys.argv[2]
                print("\n👤|Profile :", _selectProfile)

                # Selected Save
                _selectSave = sys.argv[3]
                print("🎫|Save :", _selectSave)

                # We get the path to the Save folder.
                _selectPath = os.path.join(myDocumentsPath, _selectGameResult,
                                           "profiles", _selectProfile, "save", _selectSave)
                print("\n📂|Path :", _selectPath)

                # We get the path to the Game.sii file.
                _selectSaveGameSiiPath = os.path.join(_selectPath, "game.sii")
                print("📂|Game SII Path :", _selectSaveGameSiiPath)

                # We get the path to the Info.sii file.
                _selectSaveInfoSiiPath = os.path.join(_selectPath, "info.sii")
                print("📂|Info SII Path :", _selectSaveInfoSiiPath)

                # Checking the existence of game.sii
                if os.path.exists(_selectSaveGameSiiPath):
                    print("🔔 | Status: game.sii file exists. Decrypting...")
                    os.chdir(_selectPath)
                    decryptGame()
                else:
                    print("\n❌ | Error | ❌ \nℹ️ | Error:", _selectProfile,
                          "-> ", _selectSave, "game.sii file does not exist.")
                    logging.error(
                        " | Error: " + _selectProfile + " -> " + _selectSave+" game.sii file does not exist.")

                # Checking the existence of info.sii
                if os.path.exists(_selectSaveInfoSiiPath):
                    print("🔔 | Status: info.sii file exists. Decrypting...")
                    os.chdir(_selectPath)
                    decryptInfo()
                else:
                    print("\n❌ | Error | ❌ \nℹ️ | Error:", _selectProfile,
                          "-> ", _selectSave, "info.sii file does not exist.")
                    logging.error(
                        " | Error: " + _selectProfile + " -> " + _selectSave+" info.sii file does not exist.")

            elif (len(sys.argv) > 4):
                print("\n❌ | Error | ❌ \nℹ️ | Error: Invalid argument count.")
                logging.error(" | Error: Invalid argument count.")
            else:
                pass
        else:
            print("\n❌ | Error | ❌ \nℹ️ | Error: Invalid argument count.")
            print(
                "⚠️ | Warning | ⚠️ \nℹ️ | Example Arguments Usage: ets/ats 21232312434232 quicksave.")
            logging.error(" | Error: Invalid argument count.")


try:
    main()
    input("\n🚪 | Press any key to exit :")
    # exit(1)
except Exception as e:
    logging.error("Error: %s", e.args)
