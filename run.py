from configure import configure
from data_types import log
from Folder_fast_access import folder_fast_access
from Mail_section import mail_section
from operations import change_status, get_date_time, internet_connection, write_log
from Reminder_section import reminder_section
from basic_commands import basic_commands
from browser_section import browser_section
from process_fast_access import process_fast_access
from website_fast_access import website_fast_access

__name__ = "__run__"


class run:
    def __init__(self) -> None:
        self.__start_up_check()
        self.__basic = basic_commands()

    def start(self) -> None:
        """
        Start the main programme
        """
        self.__main_function()

    def __start_up_check(self) -> None:
        """
        Start up mail and reminder check
        """
        # check if mails are pendig , if yes try sending them if internet connection is available
        if configure().get_status(status_of="mail check"):
            mail_section().startup_mail_check()
        # check if reminder's are pending , show prompt to see them
        if configure().get_status(status_of="reminder check"):
            reminder_section().startup_reminder_check()

    def __main_function(self) -> None:
        """
        Main function
        """
        try:
            input_list = []
            print("Type break/stop to exit section")
            while True:
                user_input = input("> ").lower()
                input_list.append(
                    log(
                        user_input=user_input, section="main", date_time=get_date_time()
                    )
                )
                # user_input_list = user_input.split()
                # input_length = len(user_input_list)
                if (
                    len(set(user_input)) == 0
                    or len(set(user_input)) == 1
                    and not user_input.isalnum()
                ):
                    continue
                if user_input[0] == "!":
                    browser_section().user_section(user_input=user_input)
                # to access mail section
                elif user_input in configure().get_keywords(data_type="mail"):
                    if mail_section().user_section():
                        break
                # to check if internet connection is available
                elif user_input in configure().get_keywords(data_type="reminder"):
                    if reminder_section().user_section():
                        break
                elif user_input == "status":
                    change_status().show_status()
                elif user_input in configure().get_keywords(data_type="website"):
                    if website_fast_access().user_section():
                        break
                elif user_input in configure().get_keywords(data_type="process"):
                    if process_fast_access().user_section():
                        break
                elif user_input in configure().get_keywords(data_type="folder"):
                    if folder_fast_access().user_section():
                        break
                elif user_input in configure().get_keywords(data_type="configure"):
                    if configure().user_section():
                        break
                elif user_input == "con?":
                    internet_connection()
                else:
                    if self.__basic.user_section(user_input=user_input):
                        break
        except Exception as e:
            print(f"run > __main_function :- {e}")
        finally:
            write_log(data_list=input_list)


if __name__ == "__run__":
    run().start()
