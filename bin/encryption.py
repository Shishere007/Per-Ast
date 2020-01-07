from ast import literal_eval
from getpass import getpass
from random import choice, randint, shuffle


"""
use the following syntax tio convert str to dictionary
temp2 = literal_eval(str(temp))

"""


class encryptionCodeCreation:
    def charList(self):
        other = "~!@#$%^&*()_+`-" '""=[]}{;:,./<>?\\| *'
        char = []
        for item in range(97, 123):
            char.append(chr(item))
        for item in range(65, 91):
            char.append(chr(item))
        for item in range(10):
            char.append(str(item))
        for item in list(other):
            char.append(item)
        return char

    def genrateSequence(self, digitCount):
        start = int("".join(["1" for _ in range(digitCount)]))
        end = int("".join(["9" for _ in range(digitCount)]))
        sequence = []
        while True:
            item = str(randint(start, end))
            if item.__contains__("0") or item in sequence:
                continue
            sequence.append(item)
            if len(sequence) == 100:
                break
        return sequence

    def makeEncryptionCode(self):
        try:
            charList = self.charList()
            encrypt_code = {}
            sequence = self.genrateSequence(randint(11, 50))
            shuffle(sequence)
            for item in charList:
                random_number = choice(sequence)
                encrypt_code[item] = random_number
                sequence.remove(random_number)
            with open("bin\\Data\\EncryptionCode.txt", "w") as f:
                f.write(str(encrypt_code))
        except Exception as e:
            print(e)


class dataEncryption:
    def __init__(self):
        self.class_call_encryption = encryptionCodeCreation()

    def encyrptData(self, data):
        try:
            charList = list(data)
            encyrptedDataList = []
            with open("bin\\Data\\EncryptionCode.txt", "r") as f:
                encyrptionCode = literal_eval(f.readline())
            digitCount = len(encyrptionCode["a"])
            for item in charList:
                encyrptedDataList.append(encyrptionCode[item])
            encyrptedDataList.append(str(digitCount))
            encyrptedData = "".join(encyrptedDataList)
            return encyrptedData
        except Exception as e:
            print(e)
    # decrypt the given data
    def decryptData(self, data):
        try:
            codeCharList = []
            decryptedCode = []
            data = list(data)
            digitCount = int("".join(data[-2:]))
            data.pop(-1)
            data.pop(-1)
            data = "".join(data)
            for loopVar in range(0, len(data), digitCount):
                codeCharList.append(data[loopVar : loopVar + digitCount])
            with open("bin\\Data\\EncryptionCode.txt", "r") as f:
                encyrptionCode = literal_eval(f.readline())
            key = list(encyrptionCode.keys())
            value = list(encyrptionCode.values())
            for item in codeCharList:
                decryptedCode.append(key[value.index(item)])
            decryptedCode = "".join(decryptedCode)
            return decryptedCode
        except Exception as e:
            print(f'encryption > dataEncryption.decryptData :- {e}')

    def change_encryption(self):
        self.class_call_encryption.makeEncryptionCode()

    def change_mediafile_encryption_phase_1(self):
        try:
            decrypted_path_list = []
            with open("bin\\Data\\mediaPath.txt", "r") as f:
                lines = f.readlines()
            for item in lines:
                temp = list(item)
                try:
                    temp.remove("\n")
                except Exception:
                    pass
                item = "".join(temp)
                decrypted_path_list.append(self.decryptData(item))
            return decrypted_path_list
        except Exception as e:
            print(e)

    def change_mediafile_encryption_phase_2(self, decrypted_path_list):
        try:
            with open("bin\\Data\\mediaPath.txt", "w") as f:
                for item in decrypted_path_list:
                    try:
                        encrypted_path = self.encyrptData(item)
                        f.write(encrypted_path)
                        f.write("\n")
                    except Exception as e:
                        print(e)
        except Exception as ex:
            print(ex)

    def change_password_encryption_phase_1(self):
        try:
            with open("bin\\Data\\loginData.txt", "r") as f:
                decrypted_password = self.decryptData(f.read())
            return decrypted_password
        except Exception as e:
            print(e)

    def change_password_encryption_phase_2(self, decrypted_password):
        try:
            encrypted_password = self.encyrptData(decrypted_password)
            with open("bin\\Data\\loginData.txt", "w") as f:
                f.write(encrypted_password)
        except Exception as e:
            print(e)


class encryptCommands:
    def __init__(self):
        self.class_call_encryption = dataEncryption()

    def password_check(self, password):
        try:
            with open("bin\\Data\\loginData.txt", "r") as f:
                stored_password = f.read()
            if password == self.class_call_encryption.decryptData(stored_password):
                return True
            return False
        except Exception:
            return False

    def change_password(self):
        try:
            new_password = getpass("new Password : ")
            encryptedData = self.class_call_encryption.encyrptData(new_password)
            with open("bin\\Data\\loginData.txt", "w") as f:
                f.write(encryptedData)
            print("Password Changed")
        except Exception:
            print("ACCESS RESTRICTED")

    def setPassword(self):
        try:
            while True:
                old_password = getpass("old Password : ")
                if not self.password_check(old_password):
                    print("password doesn't match")
                    break
                self.change_password()
                break
        except Exception:
            pass

    def change_encryption(self):
        try:
            decrypted_path_list = (
                self.class_call_encryption.change_mediafile_encryption_phase_1()
            )
            decrypted_password = (
                self.class_call_encryption.change_password_encryption_phase_1()
            )
            self.class_call_encryption.change_encryption()
            print("Encryption Changed")
            self.class_call_encryption.change_mediafile_encryption_phase_2(
                decrypted_path_list
            )
            self.class_call_encryption.change_password_encryption_phase_2(
                decrypted_password
            )
            print("Corresponding changes have made to data")
        except Exception as e:
            print(e)
    
    def encrypt_data(self,data) :
        return self.class_call_encryption.encyrptData(data)
    
    def decrypt_data(self, data) :
        return self.class_call_encryption.decryptData(data)


if __name__ == "__main__":
    pass
