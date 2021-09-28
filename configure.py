from tkinter import (
    END,
    BooleanVar,
    Button,
    Checkbutton,
    Entry,
    Label,
    StringVar,
    Tk,
    mainloop,
    ttk,
)

from data_types import config, convert, log
from file_operation import File
from operations import get_date_time, write_log

__name__ = "__configure__"


class configure:
    def __init__(self) -> None:
        self.__config_file_path = "Data/configure.json"
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

    def change_keywords(self, keyword_list: [str], datatype: str) -> None:
        """
        Add / delete /change keyword  for fast access
        """
        try:
            config = self.__get_current_config()
            if config.add_or_change_keywords(
                datatype=datatype, keyword_list=keyword_list
            ):
                self.__update_config(new_config=config)
                print("Update Success")
            else:
                print("Error found. Unable to make changes")
        except Exception as e:
            print(f"configure > __add_keyword - {e}")

    def get_keywords(self, data_type: str) -> [str]:
        """
        get list of keywords
        """
        return self.__get_current_config().get_keywords(datatype=data_type)

    def get_status(self, status_of: str) -> bool:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_reminder_check(reminder check)
        """
        return self.__get_current_config().get_status(status_of=status_of)

    def set_status(self, status_of: str, do_show: bool) -> None:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_reminder_check(reminder check)
        """
        config = self.__get_current_config()
        if config.set_status(status_of=status_of, do_show=do_show):
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
            -> reminder check set true          To check if reminder pending during program startup
            -> reminder check set false         Not to check if reminder pending during program startup
            -> break                            Exit section
            -> quit / exit                      Exit program
        """
        )

    # def user_section(self) -> bool:
    #     try:
    #         input_list = []
    #         while True:
    #             user_input = input(">>> ").lower()
    #             # user_input_list = user_input.split()
    #             input_list.append(
    #                 log(
    #                     user_input=user_input,
    #                     section="configure",
    #                     date_time=get_date_time(),
    #                 )
    #             )
    #             if user_input in ["gui"]:
    #                 configure_gui()
    #             elif user_input in ["show"]:
    #                 self.show()
    #             elif user_input in ["help"]:
    #                 self.__help()
    #             elif user_input == "show reminder set true":
    #                 self.set_status(status_of="show reminder", do_show=True)
    #             elif user_input == "reminder check set true":
    #                 self.set_status(status_of="reminder check", do_show=True)
    #             elif user_input == "show reminder set false":
    #                 self.set_status(status_of="show reminder", do_show=False)
    #             elif user_input == "reminder check set false":
    #                 self.set_status(status_of="reminder check", do_show=False)
    #             elif user_input in ["kill", "break"]:
    #                 return False
    #             elif user_input in ["quit", "exit"]:
    #                 return True
    #             else:
    #                 print("Incorrect Command")
    #     except Exception as e:
    #         print(f"configure > user_section - {e}")
    #     finally:
    #         write_log(data_list=input_list)


class configure_gui:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Configure")
        self.root.minsize(600, 300)
        self.root.maxsize(600, 300)

        # show curresponding reminder set up
        self.show_reminder_label = Label(self.root, text="Show Curresponding Reminder")
        self.show_reminder_label.config(font="15")
        self.show_reminder_label.place(x=0, y=10)
        self.__show_reminder_status = BooleanVar()
        self.__show_reminder_status.set(self.__get_show_curresponding_reminder_status())
        self.show_reminder_checkbutton = Checkbutton(
            self.root, text="Show", variable=self.__show_reminder_status, font="15"
        )
        self.show_reminder_checkbutton.place(x=280, y=10)

        # start up reminder check set up
        self.check_reminder_label = Label(self.root, text="Start up Reminder check")
        self.check_reminder_label.config(font="15")
        self.check_reminder_label.place(x=0, y=40)
        self.__check_reminder_status = BooleanVar()
        self.__check_reminder_status.set(self.__get_startup_reminder_check_status())
        self.check_reminder_checkbutton = Checkbutton(
            self.root, text="Check", variable=self.__check_reminder_status, font="15"
        )
        self.check_reminder_checkbutton.place(x=280, y=40)

        # Folder keywords
        self.folder_keywords_label = Label(self.root, text="Folder Keywords")
        self.folder_keywords_label.config(font="15")
        self.folder_keywords_label.place(x=0, y=70)
        self.folder_keywords_textbox = Entry(self.root)
        self.folder_keywords_textbox.config(font="15", width=30)
        self.folder_keywords_textbox.place(x=280, y=70)

        # Process keywords
        self.process_keywords_label = Label(self.root, text="Process Keywords")
        self.process_keywords_label.config(font="15")
        self.process_keywords_label.place(x=0, y=100)
        self.process_keywords_textbox = Entry(self.root)
        self.process_keywords_textbox.config(font="15", width=30)
        self.process_keywords_textbox.place(x=280, y=100)

        # Website keywords
        self.website_keywords_label = Label(self.root, text="Website Keywords")
        self.website_keywords_label.config(font="15")
        self.website_keywords_label.place(x=0, y=130)
        self.website_keywords_textbox = Entry(self.root)
        self.website_keywords_textbox.config(font="15", width=30)
        self.website_keywords_textbox.place(x=280, y=130)

        # Status keywords
        self.status_keywords_label = Label(self.root, text="Status Keywords")
        self.status_keywords_label.config(font="15")
        self.status_keywords_label.place(x=0, y=160)
        self.status_keywords_textbox = Entry(self.root)
        self.status_keywords_textbox.config(font="15", width=30)
        self.status_keywords_textbox.place(x=280, y=160)

        # configure keywords
        self.configure_keywords_label = Label(self.root, text="Configure Keywords")
        self.configure_keywords_label.config(font="15")
        self.configure_keywords_label.place(x=0, y=190)
        self.configure_keywords_textbox = Entry(self.root)
        self.configure_keywords_textbox.config(font="15", width=30)
        self.configure_keywords_textbox.place(x=280, y=190)

        # Media keywords
        self.media_keywords_label = Label(self.root, text="Media Keywords")
        self.media_keywords_label.config(font="15")
        self.media_keywords_label.place(x=0, y=220)
        self.media_keywords_textbox = Entry(self.root)
        self.media_keywords_textbox.config(font="15", width=30)
        self.media_keywords_textbox.place(x=280, y=220)

        # update button
        self.update_button = Button(
            self.root, width=10, text="update", command=self.__update_configuration
        )
        self.update_button.config(font="15")
        self.update_button.place(x=330, y=260)
        self.__fill_data()
        mainloop()

    def __update_configuration(self) -> None:
        """
        Update changes made to configuration
        """
        # folder keywords
        __folder_keywrods = self.folder_keywords_textbox.get()
        if __folder_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="folder")
        ) != sorted(__folder_keywrods.split(",")):
            configure().change_keywords(
                datatype="folder", keyword_list=__folder_keywrods.split(",")
            )

        # process keywords
        __process_keywrods = self.process_keywords_textbox.get()
        if __process_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="process")
        ) != sorted(__process_keywrods.split(",")):
            configure().change_keywords(
                datatype="process", keyword_list=__process_keywrods.split(",")
            )

        # website keywords
        __website_keywrods = self.website_keywords_textbox.get()
        if __website_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="website")
        ) != sorted(__website_keywrods.split(",")):
            configure().change_keywords(
                datatype="website", keyword_list=__website_keywrods.split(",")
            )

        # media keywords
        __media_keywrods = self.media_keywords_textbox.get()
        if __media_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="media")
        ) != sorted(__media_keywrods.split(",")):
            configure().change_keywords(
                datatype="media", keyword_list=__media_keywrods.split(",")
            )

        # status keywords
        __status_keywrods = self.status_keywords_textbox.get()
        if __status_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="status")
        ) != sorted(__status_keywrods.split(",")):
            configure().change_keywords(
                datatype="status", keyword_list=__status_keywrods.split(",")
            )

        # configure keywords
        __configure_keywrods = self.configure_keywords_textbox.get()
        if __configure_keywrods not in ["", " "] and sorted(
            configure().get_keywords(data_type="configure")
        ) != sorted(__configure_keywrods.split(",")):
            configure().change_keywords(
                datatype="configure", keyword_list=__configure_keywrods.split(",")
            )

        # show curresponding reminder status update
        if (
            self.__show_reminder_status.get()
            != self.__get_show_curresponding_reminder_status()
        ):
            configure().set_status(
                status_of="show reminder", do_show=self.__show_reminder_status.get()
            )

        # check reminder status update
        if (
            self.__check_reminder_status.get()
            != self.__get_startup_reminder_check_status()
        ):
            configure().set_status(
                status_of="reminder check", do_show=self.__check_reminder_status.get()
            )

    def __fill_data(self) -> None:
        """
        Fill data in the fields
        """
        self.folder_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="folder"))
        )
        self.process_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="process"))
        )
        self.website_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="website"))
        )
        self.status_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="status"))
        )
        self.media_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="media"))
        )
        self.configure_keywords_textbox.insert(
            1, ",".join(configure().get_keywords(data_type="configure"))
        )

    def __get_show_curresponding_reminder_status(self) -> bool:
        """
        get show curresponding reminder status
        """
        return configure().get_status(status_of="show reminder")

    def __get_startup_reminder_check_status(self) -> bool:
        """
        get startup reminder check status
        """
        return configure().get_status(status_of="reminder check")


if __name__ == "__configure__":
    pass
    # configure_gui()
