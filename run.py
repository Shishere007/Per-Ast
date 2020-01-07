from bin import broswer, cmdMain, internet, login


class main_class:
    def __init__(self):
        self.class_call_cmd = cmdMain.CMDcall()
        self.class_call_browser = broswer.commandCall()
        self.class_call_login = login.login()
        self.class_call_cmd_reminder = cmdMain.reminder()
        self.class_call_internet = internet.control_section()
        self.class_call_internet_connection = internet.internet_connection()

    def startup(self):
        self.class_call_internet.startup_mail_check()
        self.class_call_cmd_reminder.startup_reminder_check()

    def main_function(self):
        try:
            user_input = input("> ").lower()
            if (
                len(set(user_input)) == 0
                or len(set(user_input)) == 1
                and not user_input.isalnum()
            ):
                raise UserWarning
            if user_input[0] == "!":
                if len(user_input.split()) > 1:
                    if self.class_call_internet_connection.is_connected():
                        self.class_call_cmd_reminder.show_curresponding_reminder("ff")
                        self.class_call_browser.broswerCommand(user_input)
                    else:
                        print("No Internet Connection")
            elif user_input.__contains__("login") or user_input.__contains__("change"):
                self.class_call_login.checkUser(user_input)
            elif user_input.__contains__("hide") or user_input in [
                "add path",
                "hidden files",
            ]:
                self.class_call_login.hide_unhide(user_input)
            elif user_input.__contains__("mail"):
                self.class_call_internet.user_section()
            elif user_input == "con?":
                if self.class_call_internet_connection.is_connected():
                    print("Internet connection is available")
                else:
                    print("No Internet Connection")
            else:
                self.class_call_cmd.cmdCommand(user_input)
        except UserWarning:
            pass
        except Exception as e:
            print(f"run > main_class.main_function :- {e}")


if __name__ == "__main__":
    run = main_class()
    run.startup()
    print("use 'help' to get command list")
    while True:
        run.main_function()
