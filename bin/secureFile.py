from os import path, system
from pathlib import Path

from bin import encryption


def remove_non_existing_path(lines, remove_path_list):
    class_call_unhide = unhide()
    class_call_hide = hide()
    try:
        for item in remove_path_list:
            lines.remove(item)
        class_call_unhide.source_file()
        with open("bin\\Data\\mediaPath.txt", "w") as f:
            f.writelines(lines)
        class_call_hide.source_file()
    except Exception:
        pass


class hide:
    def __init__(self):
        self.class_call_encryption = encryption.dataEncryption()

    def source_code(self):
        try:
            file_path = "attrib +h +s C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\EncryptionCode.txt"
            system(file_path)
        except Exception:
            pass

    def source_file(self):
        source_file_list = [
            "C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\loginData.txt",
            "C:\\Users\\xxx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\mediaPath.txt",
            "C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data",
        ]
        try:
            for file_path in source_file_list:
                system(f"attrib +h +s {file_path}")
        except Exception as e:
            print(e)

    def media_file(self):
        try:
            remove_path_list = []
            with open("bin\\Data\\mediaPath.txt", "r") as f:
                lines = f.readlines()
            for item in lines:
                temp = item
                item = list(item)
                try:
                    item.remove("\n")
                except Exception:
                    pass
                item = "".join(item)
                decrypted_path = self.class_call_encryption.decryptData(item)
                if path.exists(decrypted_path):
                    system(f'attrib +h +s "{decrypted_path}"')
                else:
                    print("A file/folder is moved/deleted")
                    remove_path_list.append(temp)
                if len(remove_path_list) > 0:
                    remove_non_existing_path(lines, remove_path_list)
        except Exception as e:
            print(e)

    def add_media_path(self, file_path):
        try:
            encrypted_path = self.class_call_encryption.encyrptData(file_path)
            with open("bin\\Data\\mediaPath.txt", "r") as f:
                lines = f.readlines()
            lines_copy = []
            for item in lines :
                item = list(item)
                item.remove('\n')
                lines_copy.append("".join(item))
            if encrypted_path in lines_copy :
                return False
            with open("bin\\Data\\mediaPath.txt", "a") as f:
                f.write(encrypted_path)
                f.write("\n")
            return True
        except Exception as e:
            print(f'secureFile > hide.add_media_path :- {e}')

    def add_media(self):
        print(
            """
        Write path seperated by enter
        use 'stop/break' to stop adding paths
        """
        )
        try:
            while True:
                file_path = input(">>>")
                if file_path in ["break", "stop", "kill"]:
                    break
                if not Path(file_path).exists() or len(file_path) == 0:
                    print("wrong path")
                    continue
                if self.add_media_path(file_path) :
                    print("added")
                else :
                    print ('files already exists')
        except Exception as e:
            print(e)


class unhide:  # to unhide below specified items as needed
    def __init__(self):
        self.class_call_encryption = encryption.dataEncryption()

    def source_code(self):
        try:
            file_path = "attrib -h -s C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\EncryptionCode.txt"
            system(file_path)
        except Exception:
            pass

    def source_file(self):
        source_file_list = [
            "C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\loginData.txt",
            "C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data\\mediaPath.txt",
            "C:\\Users\\xx\\Documents\\GitHub\\Python-Automation-Pvt\\bin\\Data",
        ]
        try:
            for file_path in source_file_list:
                system(f"attrib -h -s {file_path}")
        except Exception as e:
            print(e)

    def media_file(self):
        try:
            remove_path_list = []
            with open("bin\\Data\\mediaPath.txt", "r") as f:
                lines = f.readlines()
            for item in lines:
                temp = item
                item = list(item)
                try:
                    item.remove("\n")
                except Exception:
                    pass
                item = "".join(item)
                decrypted_path = self.class_call_encryption.decryptData(item)
                if path.exists(decrypted_path):
                    system(f'attrib -h -s "{decrypted_path}"')
                else:
                    print("A file/folder is moved/deleted")
                    remove_path_list.append(temp)
                if len(remove_path_list) > 0:
                    remove_non_existing_path(lines, remove_path_list)
        except Exception as e:
            print(e)


class encryption_support:
    def __init__(self):
        self.class_call_hide = hide()
        self.class_call_unhide = unhide()
        self.class_call_encryption = encryption.encryptCommands()

    def change_encryption(self):
        self.class_call_unhide.source_code()
        self.class_call_unhide.source_file()
        self.class_call_encryption.change_encryption()
        self.class_call_hide.source_code()
        self.class_call_unhide.source_file()

    def decrypt_media_path(self):
        try:
            with open("bin\\Data\\mediaPath.txt", "r") as f:
                lines = f.readlines()
            decrypted_media_list = []
            for item in lines :
                item = list(item) 
                try :
                    item.remove('\n')
                except Exception :
                    pass
                decrypted_media_list.append(self.class_call_encryption.decrypt_data("".join(item)))
            return decrypted_media_list
        except Exception as e:
            print(f"SecureFile > encryption_support.decrypt_media_path :- {e}")


if __name__ == "__main__":
    pass
