from data_types import convert, log, config
from file_operation import File
from operations import get_date_time, write_log

__name__ = "__configure__"


class configure:
    def __init__(self) -> None:
        self.__config_file_path = "Data\configure.json"
        self.__config_file = File(file_location=self.__config_file_path)

    def show(self) -> None:
        """
        Show current Configuration
        """
        print("\n\t\t\t<<< Configuration >>>")
        self.__get_current_config().show()

    def __get_current_config(self) -> config:
        """
        get current configuration
        """
        return convert(file_data=self.__config_file.read_data()[0]).to_config()

    def __update_config(self, new_config: config) -> None:
        """
        write changed confog to file
        """
        self.__config_file.rewrite_entire_data(file_data=[new_config])

    def __add_keyword_read_data(self, user_input: str) -> None:
        try:
            pass
        except Exception as e:
            print(f"configure > __add_keyword_read_data - {e}")

    def get_keywords(self, data_type: str) -> [str]:
        """
        get list of keywords
        """
        return self.__get_current_config().get_keywords(datatype=data_type)

    def get_status(self, status_of: str) -> bool:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_mail_check(mail check),start_up_reminder_check(reminder check)
        """
        return self.__get_current_config().get_status(status_of=status_of)

    def __set_status(self, status_of: str, do_show: bool) -> None:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_mail_check(mail check),start_up_reminder_check(reminder check)
        """
        config = self.__get_current_config()
        return_val = config.set_status(status_of=status_of, do_show=do_show)
        if return_val:
            self.__update_config(new_config=config)
            print("Change updated")
        else:
            print("Error found. Unable to make changes")

    def __help(self) -> None:
        """
        Show command list
        """
        print(
            """
            Command list

            -> show reminder set true           Show remidners curresponding to a app
            -> show reminder set false          Do not show reminders curresponding to a app
            -> mail check set true              To check if mail pending during program startup
            -> mail check set false             Not to check if mail pending during program startup
            -> reminder check set true          To check if reminder pending during program startup
            -> reminder check set false         Not to check if reminder pending during program startup
            -> break                            Exit section
            -> quit / exit                      Exit program
        """
        )

    def user_section(self) -> bool:
        try:
            input_list = []
            while True:
                user_input = input(">>> ").lower()
                user_input_list = user_input.split()
                input_list.append(
                    log(
                        user_input=user_input,
                        section="configure",
                        date_time=get_date_time(),
                    )
                )
                if user_input in ["show"]:
                    self.show()
                elif user_input in ["help"]:
                    self.__help()
                elif user_input == "show reminder set true":
                    self.__set_status(status_of="show reminder", do_show=True)
                elif user_input == "mail check set true":
                    self.__set_status(status_of="mail check", do_show=True)
                elif user_input == "reminder check set true":
                    self.__set_status(status_of="reminder check", do_show=True)
                elif user_input == "show reminder set false":
                    self.__set_status(status_of="show reminder", do_show=False)
                elif user_input == "mail check set false":
                    self.__set_status(status_of="mail check", do_show=False)
                elif user_input == "reminder check set false":
                    self.__set_status(status_of="reminder check", do_show=False)
                elif user_input in ["kill", "break"]:
                    return False
                elif user_input in ["quit", "exit"]:
                    return True
                else:
                    print("Incorrect Command")
        except Exception as e:
            print(f"configure > user_section - {e}")
        finally:
            write_log(data_list=input_list)


if __name__ == "__configure__":
    pass
