from ast import literal_eval
from getpass import getpass
from smtplib import SMTP

from requests import ConnectionError, get

from bin import encryption

# user 'pip3 install requests' to install 'requests' module


class internet_connection:
    def __init__(self):
        self.class_call_encryption = encryption.dataEncryption()

    """
    def enable_connection(self) :
        os.system("netsh interface set interface ""Wi-Fi"" ENABLED")
    
    def disable_connection(self) : 
        os.system("netsh interface set interface 'Wi-Fi' DISABLED") 
    # to check if the system is connected to internet
    """
    # to check if connected to internet
    # if connection is available
    def is_connected(self):
        url = "http://www.google.com/"
        timeout = 5
        try:
            _ = get(url, timeout=timeout)
            return True
        except ConnectionError:
            return False

    # send mail with text only
    def send_mail(self, email_data):
        try:
            from_address = email_data["from_address"]
            to_address = email_data["to_address"]
            subject = email_data["subject"]
            body = email_data["body"]
            password = self.decrypt_password(email_data["password"])
            server = SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(from_address, password)
            message = f"Subject : {subject}  \n\n\n{body}"
            server.sendmail(from_address, to_address, message, body)
            server.quit()
            return True
        except Exception as e:
            return e

    def encrypt_password(self, password):
        encrypted_password = self.class_call_encryption.encyrptData(password)
        return encrypted_password

    def decrypt_password(self, password):
        decrypted_password = self.class_call_encryption.decryptData(password)
        return decrypted_password


class mail_data_control:
    def __init__(self):
        self.class_call = internet_connection()

    def quit_section(self, user_input):
        if user_input in ["kill", "stop", "break"]:
            return True
        return False

    def send_new_mail(self, mail_type):
        def add_mail_to_list():
            try:
                with open("bin\\Data\\mailData.txt", "r") as f:
                    mail_list = f.readlines()
                try:
                    while True:
                        mail_list.remove("\n")
                except Exception:
                    pass
                if len(mail_list) == 0:
                    mail_count = 0
                else:
                    item = literal_eval(mail_list[-1])
                    mail_count = item["id"]
                mail_count += 1
                email_data["id"] = mail_count
                with open("bin\\Data\\mailData.txt", "a") as f:
                    f.write(str(email_data))
                    f.write("\n")
            except Exception as e:
                print(e)

        email_data = {}
        if mail_type == "new":
            while True:
                from_address = input("From Address : ").lower()
                if self.quit_section(from_address):
                    return
                if from_address.__contains__("@") and from_address.__contains__(".com"):
                    if from_address.__contains__("gmail"):
                        break
                    else:
                        print("invalid mail id")
                        continue
                else:
                    print("invalid mail id")
                    continue
        else:
            # provide a mail id
            from_address = 'mail_id'
        while True:
            to_address = input("To  Address : ").lower()
            if self.quit_section(to_address):
                return
            if to_address.__contains__("@") and to_address.__contains__(".com"):
                if (
                    to_address.__contains__("gmail")
                    or to_address.__contains__("outlook")
                    or to_address.__contains__("hotmail")
                    or to_address.__contains__("yahoo")
                ):
                    break
                else:
                    print("invalid mail id")
                    continue
            else:
                print("invalid mail id")
                continue
        email_data = {
            "from_address": from_address,
            "password": self.class_call.encrypt_password(getpass("Password : ")),
            "to_address": to_address,
            "subject": input("Subject : "),
            "body": input("Email Body : "),
            "status": "pending",
        }
        if self.class_call.is_connected():
            return_data = self.class_call.send_mail(email_data)
            if return_data == True:
                print("Success")
            else:
                print("unable to send email")
                if str(return_data).__contains__("not accepted"):
                    print("invalid email or password")
                else:
                    email_data["error"] = str(return_data)
                    add_mail_to_list()
        else:
            print(
                "no internet connection.\nEmail will be sent when system goes online next"
            )
            self.change_mail_status()
            add_mail_to_list()

    def is_mail_pending(self):
        try:
            pending_mail_count = 0
            with open("bin\\Data\\mailData.txt", "r") as f:
                mail_list = f.readlines()
            try:
                while True:
                    mail_list.remove("\n")
            except Exception:
                pass
            for loopVar in range(len(mail_list)):
                item = literal_eval(str(mail_list[loopVar]))
                if item["status"] == "pending":
                    pending_mail_count += 1
            if pending_mail_count == 0:
                return 0
            return pending_mail_count
        except Exception as e:
            print(f'internet > is_mail_pending :- {e}')

    def send_pending_mail(self):
        try:
            with open("bin\\Data\\mailData.txt", "r") as f:
                mail_list = f.readlines()
            try:
                while True:
                    mail_list.remove("\n")
            except Exception:
                pass
            for loopVar in range(len(mail_list)):
                item = literal_eval(str(mail_list[loopVar]))
                if item["status"] == "pending":
                    return_data = self.class_call.send_mail(item)
                    if return_data == True:
                        item["status"] = "completed"
                        item["password"] = ""
                        mail_list[loopVar] = item
                    else:
                        item["status"] = "error"
                        item["error"] = return_data
                        item["password"] = ""
                        mail_list[loopVar] = item
            with open("bin\\Data\\mailData.txt", "w") as f:
                for item in mail_list:
                    f.write(str(item))
                    f.write("\n")
            return True
        except Exception:
            return False

    def clear_list(self, status):
        try:
            with open("bin\\Data\\mailData.txt", "r") as f:
                mail_list = f.readlines()
            try:
                while True:
                    mail_list.remove("\n")
            except Exception:
                pass
            with open("bin\\Data\\mailData.txt", "w") as f:
                for item in mail_list:
                    item = literal_eval(str(mail_list[item]))
                    if item["status"] == status:
                        continue
                    f.write(str(item))
                    f.write("\n")
        except Exception as e:
            print(e)

    def clear_mail_list(self):
        try:
            with open("bin\\Data\\mailData.txt", "w"):
                pass
        except Exception:
            pass

    def show_mail(self, mail_type):
        try:
            with open("bin\\Data\\mailData.txt", "r") as f:
                mail_list = f.readlines()
            try:
                while True:
                    mail_list.remove("\n")
            except Exception:
                pass
            if len(mail_list) == 0:
                print("No mail found")
            elif self.is_mail_pending() == 0 and mail_type == "pending":
                print("No pending mail found")
            elif len(mail_list) - self.is_mail_pending() == 0:
                print("No Sent mail found")
            else:
                for mail_data in mail_list:
                    flag = False
                    mail_data = literal_eval(str(mail_data))
                    if mail_type in ["all", mail_data["status"]]:
                        flag = True
                    if flag:
                        print(
                            f"""
                                ID      : {mail_data['id']}
                                From    : {mail_data['from_address']}
                                To      : {mail_data['to_address']}
                                Subject : {mail_data['subject']}
                                Status  : {mail_data['status']}
                            """
                        )
                        if mail_type == "error":
                            print(
                                f"""
                                Error   : {mail_data['error']}
                            """
                            )
        except Exception as e:
            print(e)

    def change_mail_status(self):
        try:
            with open("bin\\Data\\status.txt", "r") as f:
                status = f.read()
            status = literal_eval(str(status))
            pending_mail_count = self.is_mail_pending()
            if pending_mail_count:
                status["mail_pending"] = True
                status["mail_pending_count"] = pending_mail_count
            else:
                status["mail_pending"] = False
                status["mail_pending_count"] = 0
            with open("bin\\Data\\status.txt", "w") as f:
                f.write(str(status))
        except Exception as e:
            print(f'change_mail_definition :- {e}')

    def command_list(self):
        print(
            """
            -> send             Send new email
            -> send new         send email from user's mail
            -> show [type]      To check email list
            -> pending          To check if emails are pending
            -> clear [type]     Clear emails from list
        """
        )


class control_section:
    def __init__(self):
        self.class_call_internet = internet_connection()
        self.class_call = mail_data_control()
        self.class_call_encryption = encryption.encryptCommands()

    def startup_mail_check(self):
        with open("bin\\Data\\status.txt", "r") as f:
            status = f.read()
        status = literal_eval(str(status))
        if status["mail_pending_count"] != 0:
            if self.class_call_internet.is_connected():
                print("Attempting to send pending mail(s). \n Please wait")
                if self.class_call.send_pending_mail():
                    print("Success")
                else:
                    print("Some error found system will try again")
            else:
                print(
                    f"There are {self.class_call.is_mail_pending()} pending mail(s) \n System will try to send when Internet Connection is available"
                )

    def user_section(self):
        print("use break or stop to quit Email section")
        self.class_call.change_mail_status()
        while True:
            try :
                user_input = input(">>> ").lower()
                if user_input == "send":
                    self.class_call.send_new_mail("none")
                elif user_input == "send new":
                    self.class_call.send_new_mail("new")
                elif user_input.__contains__("send pend"):
                    if self.class_call.is_mail_pending() != 0:
                        if self.class_call_internet.is_connected():
                            self.class_call.send_pending_mail()
                        else:
                            print("No Internet Connection")
                    else:
                        print("No Pending mail found")
                elif user_input == "pending":
                    print(f"There are {self.class_call.is_mail_pending()} pending mails")
                elif list(user_input.split())[0] == 'clear' :
                    if self.class_call_encryption.password_check(getpass("Password : ")):
                        if user_input.__contains__("all"):
                            self.class_call.clear_mail_list()
                        elif user_input.__contains__("pend"):
                            self.class_call.clear_list("pending")
                        elif user_input.__contains__("comp"):
                            self.class_call.clear_list("completed")
                        elif user_input.__contains__("error"):
                            self.class_call.clear_list("error")
                        else:
                            print("not a command")
                    else:
                        print("NO ACCESS")
                elif list(user_input.split())[0] == 'show' :
                    if len(user_input.split()) == 1 or user_input.__contains__("pend"):
                        self.class_call.show_mail("pending")
                    elif user_input.__contains__("com"):
                        self.class_call.show_mail("completed")
                    elif user_input.__contains__("error"):
                        self.class_call.show_mail("error")
                    elif user_input.__contains__("all"):
                        self.class_call.show_mail("all")
                    else:
                        print("not a command")
                elif user_input in ["kill", "stop", "break"]:
                    break
                elif user_input in ["help", "commands"]:
                    self.class_call.command_list()
                elif user_input in ['quit','exit'] :
                    quit(0)
                else:
                    print("not a command")
            except Exception :
                pass

if __name__ == "__main__":
    pass
