from ast import literal_eval
from getpass import getpass

from bin import encryption, secureFile


class login:
    def __init__(self):
        self.class_call_encryption = encryption.encryptCommands()
        self.class_call_secureFile_hide = secureFile.hide()
        self.class_call_secureFile_unhide = secureFile.unhide()
        self.class_call_secureFile_encryption_supprt = secureFile.encryption_support()

    def checkUser(self, cmd):
        try:
            if cmd.__contains__("change pass"):
                self.class_call_encryption.setPassword()
            elif cmd.__contains__("change enc"):
                if self.class_call_encryption.password_check(getpass("Password : ")):
                    self.class_call_secureFile_encryption_supprt.change_encryption()
                else:
                    print("NO ACCESS")
            else:
                self.user_login()
        except Exception as e:
            print(f'login > login.checkUser :- {e}')

    def hide_unhide(self, cmd):
        try:
            if cmd.__contains__("add"):
                self.class_call_secureFile_hide.add_media()
            elif cmd == "hide source":
                self.class_call_secureFile_hide.source_code()
            elif cmd == "hide all":
                self.class_call_secureFile_hide.source_file()
                self.class_call_secureFile_hide.media_file()
            elif cmd == "unhide source":
                if self.class_call_encryption.password_check(getpass("Password : ")):
                    self.class_call_secureFile_unhide.source_code()
                else:
                    raise UserWarning
            elif cmd == "unhide all":
                if self.class_call_encryption.password_check(getpass("Password : ")):
                    self.class_call_secureFile_unhide.source_file()
                    self.class_call_secureFile_unhide.media_file()
                else:
                    raise UserWarning
            elif cmd == "hidden files":
                if self.class_call_encryption.password_check(getpass("Password : ")):
                    if self.class_call_encryption.password_check(
                        getpass("Confirm Password : ")
                    ):
                        _ = [
                            print(item)
                            for item in self.class_call_secureFile_encryption_supprt.decrypt_media_path()
                        ]
                    else:
                        raise UserWarning
                else:
                    raise UserWarning
            else:
                print("wrong command")
        except UserWarning:
            print("Not Authorized")
        except Exception:
            pass

    def change_login_status(self, login_type):
        try:
            with open("bin\\Data\\status.txt", "r") as f:
                status = f.read()
            status = literal_eval(str(status))
            status["login_type"] = login_type
            with open("bin\\Data\\status.txt", "w") as f:
                status = f.write(str(status))
        except Exception:
            pass

    def user_login(self):
        password = getpass(">> Password : ")
        if self.class_call_encryption.password_check(password):
            print(
                """
            ---Shishere---
            ACCESS GRANTED
            """
            )
            self.change_login_status("admin")
            self.class_call_secureFile_unhide.source_file()
            self.class_call_secureFile_unhide.media_file()
        else:
            print(
                """
              ---User---
            ACCESS GRANTED
            """
            )
            self.change_login_status("user")
            self.class_call_secureFile_hide.source_file()
            self.class_call_secureFile_hide.media_file()


if __name__ == "__main__":
    pass
