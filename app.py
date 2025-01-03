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
print("*        【 Product Name : Scs ETS 2 - Save SII Decrypt 】      *")
print("*        【 Author: MQuel 】                                    *")
print("*        【 Github: github@murselsen 】                         *")
print("*        【 Discord: 35mursel 】                                *")
print("*        【 Version: v1 】                        b             *")
print("*        【 License: 2025 - 2030 】                             *")
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
SII_exe = os.path.join(os.getcwd(), "saveDecrypt.exe")


def exit(status):
    if status:
        input("🚪 | Press any key to exit :")
    else:
        return True


def decrypt(profilesMainDirsPath, profileDisplayName):
    print("🎮|Profile :", profileDisplayName)
    _selectProfilePath = os.path.join(os.getcwd(), profileDisplayName)
    os.chdir(_selectProfilePath)
    shutil.copyfile(SII_exe, os.getcwd() + "/saveDecrypt.exe")
    print("🔔 | Status: saveDecrypt.exe has been copied. Please Wait!")
    logging.info("🔔 | Status: saveDecrypt.exe has been copied. Please Wait!")
    time.sleep(1.0)
    cmdDecrypt = "saveDecrypt.exe profile.sii"
    print("🔔 | Status: Profile.sii files will be decrypted. Please Wait!")
    logging.info("🔔 | Status: Profile.sii files will be decrypted. Please Wait!")
    time.sleep(1.0)
    os.system(cmdDecrypt)
    print("🔔 | Status: profileDecrypt.exe has been removed. Please Wait!")
    logging.info("🔔 | Status: profileDecrypt.exe has been removed. Please Wait!")
    os.remove("profileDecrypt.exe")
    os.chdir(profilesMainDirsPath)


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
    print(sys.argv)
    for index, game in enumerate(gameList):
        print("🎮|App :", gameList.get(game))
    if sys.argv[1] == "ets" or sys.argv[1] == "ats":
        _selectGame = sys.argv[1]
        _selectGameResult = gameList.get(_selectGame)
        print("\nSelect Game: ", _selectGameResult)
        _selectGamePath = os.path.join(myDocumentsPath, _selectGameResult, "profiles")
        os.chdir(_selectGamePath)

        if len(sys.argv) > 2:
            _selectProfile = sys.argv[2]
            print("\nSelect Profile: ", _selectProfile)
            if os.path.isdir(os.path.join(os.getcwd(), _selectProfile)):
                # decrypt(os.getcwd(), _selectProfile)
                pass
            else:
                logging.warning(
                    f"⚠️ | Warning: Profile directory '{_selectProfile}' does not exist."
                )
        else:
            print(os.listdir(os.getcwd()))
            for profileDir_index, profileDir_displayName in enumerate(
                os.listdir(os.getcwd())
            ):
                profileDir_path = os.path.join(os.getcwd(), profileDir_displayName)
                print("Profile\nIndex:", profileDir_index, "\nPath:", profileDir_path)
                if os.path.isdir(profileDir_path):
                    # decrypt(os.getcwd(), profileDir_displayName)
                    pass
                else:
                    logging.warning(
                        f"⚠️ | Warning: Profile directory '{profileDir_displayName}' does not exist."
                    )


try:
    main()
    input("🚪 | Press any key to exit :")
    # exit(1)
except Exception as e:
    logging.error("Error: %s", e.args)
