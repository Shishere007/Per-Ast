from os import startfile, system
from pathlib import Path
from tkinter import END, Button, Entry, Label, StringVar, Tk, mainloop, ttk
from configure import configure
from data_types import convert, log, process
from file_operation import File
from operations import (
    change_status,
    clear_clip,
    clear_screen,
    duplicate,
    get_date_time,
    is_input_kill,
    write_log,
)
from Reminder_section import reminder_section

__name__ = "__process_fast_access__"


class process_fast_access(change_status):
    """
    Save process for fast access with keyword
    """

    def __init__(self) -> None:
        super().__init__()
        self.__process_data_path = "Data/process_data.json"
        self.__process_file = File(file_location=self.__process_data_path)

    def add_process(self) -> None:
        """
        To add process from main section
        """
        self.__read_data_for_new_process()

    def __read_data_for_new_process(self) -> None:
        """
        Read data for adding new process
        """
        try:
            self.__dupe = duplicate(
                data_list=self.__process_file.read_data(), data_type="process"
            )
            keycode = input("process Name : ")
            if is_input_kill(data=keycode):
                return
            process_location = input("process Location(Full) : ")
            if is_input_kill(data=process_location):
                return
            # check if location exists
            if not Path(process_location).exists():
                print("Invalid process location")
                return
            # check if the location is alraedy in list
            if self.__dupe.is_file_exists(location=process_location):
                print("process is already in list")
                return
            print("Type the keywords for faster access seperated buy comma")
            keycodes = input("process codes : ").split(",")
            if is_input_kill(data=keycodes[0]):
                return
            if self.__dupe.is_keyword_exist(keyword_list=keycodes):
                print(f"one of the keyword is already in use")
                return
            new_process = process(
                title=keycode, location=process_location, codes=keycodes
            )
            self.__add_new_process(new_process=new_process)
        except Exception as e:
            print(f"process_fast_access > __read_data_for_new_process- {e}")

    def add_new_process(self, title: str, location: str, codes: [str]) -> bool:
        """
        Add new process from outside the class(public fucntion)
        """
        self.__dupe = duplicate(
            data_list=self.__process_file.read_data(), data_type="process"
        )
        if not Path(location).exists():
            print("Invalid process location")
            return False
        if self.__dupe.is_file_exists(location=location):
            print("process is already in list")
            return False
        keycodes = codes.split(",")
        if self.__dupe.is_keyword_exist(keyword_list=keycodes):
            print(f"one of the keyword is already in use")
            return False
        self.__add_new_process(
            new_process=process(title=title, location=location, codes=keycodes)
        )
        return True

    def __add_new_process(self, new_process: process) -> None:
        """
        Add new process for access
        """
        try:
            if not self.__process_file.append_one_data(data_to_append=new_process):
                print("Unable to add new process")
                return
            print("New process is added Successfully ")
            self.__change_process_status()
        except Exception as e:
            print(f"process_fast_access > __add_new_process- {e}")

    def delete_process(self, user_input: str) -> None:
        """
        To delete a process as completed from main section
        """
        self.__delete_process_read_data(keycode=user_input)

    def __delete_process_read_data(self, keycode: str) -> None:
        """
        Delete a process from list
        """
        try:
            if len(keycode.split()) > 1:
                keycode = " ".join(keycode.split()[1:])
            else:
                keycode = input("process code : ")
            if keycode.isalpha():
                self.__delete_process(keycode=keycode)
            else:
                print("incorrent input")
        except Exception as e:
            print(f"process_fast_access > __delete_process_read_data- {e}")

    def __delete_process(self, keycode: str) -> None:
        try:
            process_list = self.__process_file.read_data()
            for item in process_list:
                if keycode in convert(file_data=item).to_process().get_codes():
                    if self.__process_file.delete_one_data(
                        file_data=process_list, data_to_delete=item
                    ):
                        self.__change_process_status()
                        print("process deleted from list")
                    else:
                        print("Unable to delete data")
                    return
            else:
                print(f" No process found with '{keycode}' keyword'")
        except Exception as e:
            print(f"process_fast_access > __delete_process- {e}")

    def run_process(self, keycode: str) -> bool:
        """
        start the process with keyword saved 
        """
        try:
            cmd_command_list = {
                "tasklist": "tasklist",
                "tasklist det": "tasklist /v",
                "clear": "cls",
                "shut": "shutdown -s",
                "shutdown": "shutdown -s",
                "hibernate": "shutdown -h",
                "hiber": "shutdown -h",
                "logoff": "shutdown -l",
                "restart": "shutdown -r",
            }
            process_list = self.get_process_list()
            if keycode in ["rtb", "runtimebroker"]:
                return False
            elif keycode in cmd_command_list.keys():
                system(f"{cmd_command_list[keycode]}")
                if keycode in ["shut", "shutdown", "restart"]:
                    return "shut"
                clear_clip()
            elif keycode in ["groove", "groov", "gr"]:
                system("start mswindowsmusic:")
                print("opening groov")
            elif keycode in ["code", "vscode"]:
                system("code")
                print("opening code")
            elif keycode in ["cam", "camera"]:
                system("start microsoft.windows.camera:")
                print("opening camera")
            elif keycode.__contains__("cmd") and len(keycode.split()) > 1:
                try:
                    # to run CMD commands directly
                    cmd_command = " ".join(list(keycode.split())[1:])
                    system(f"{cmd_command}")
                except Exception:
                    pass
            else:
                for item in process_list:
                    if keycode in item.get_codes():
                        startfile(Path(item.get_location()))
                        print(f"Opening {item.get_title()}")
                        break
                else:
                    return False
            # returns true or false that will help to now if such keyword is assigned to
            # any task, if yes , app will open, if not can proceed to next condition checking
            # to show reminders/task related this app if exists
            if configure().get_status(status_of="show reminder"):
                reminder_section().show_curresponding_reminder(process_codes=keycode)
            return True
        except Exception as e:
            print(f"process_fast_access > run_process- {e}")

    def show_process_list(self) -> None:
        """
        Show all the fast access process list
        """
        try:
            process_list = self.__process_file.read_data()
            if len(process_list) == 0:
                print("list is empty")
                return
            for item in process_list:
                convert(file_data=item).to_process().show()
        except Exception as e:
            print(f"process_fast_access > show_process_list- {e}")

    def __process_help(self) -> None:
        print(
            """
            Command list
            -> add/new      add new process to fast access list
            -> del/delete   remove process from list
            -> show         List all process list          
        """
        )

    def __change_process_status(self) -> None:
        """
        change no of process count status data
        """
        try:
            current_status = self._change_status__get_status()
            current_status.set_process_list_count(
                process_count=self.__process_file.line_count()
            )
            self._change_status__write_status_to_file(current_status=current_status)
        except Exception as e:
            print(f"process_fast_access > __change_process_status- {e}")

    def get_process_list(self) -> [process]:
        """
        Get list of process saved for fast access
        """
        return duplicate(
            data_list=self.__process_file.read_data(), data_type="process"
        ).get_converted_list()

    def user_section(self) -> bool:
        """
        User section for adding removing process's from list
        """
        try:
            input_list = []
            print("Type break/stop to exit section")
            while True:
                keycode = str(input(">>>"))
                input_list.append(
                    log(
                        user_input=keycode, section="process", date_time=get_date_time()
                    )
                )
                if (
                    len(set(keycode)) == 0
                    or len(set(keycode)) == 1
                    and not keycode.isalnum()
                ):
                    continue
                if keycode in ["new", "add"]:
                    self.__read_data_for_new_process()
                elif keycode.split()[0] in ["del", "delete"]:
                    self.__delete_process_read_data(keycode=keycode)
                elif keycode in ["help"]:
                    self.process_help()
                elif keycode in ["show"]:
                    self.show_process_list()
                elif keycode in ["status"]:
                    change_status().show_status()
                elif keycode in ["quit", "exit"]:
                    return True
                elif keycode in ["break", "stop", "kill"]:
                    False
                elif keycode in ["clear"]:
                    clear_screen()
                else:
                    print("incorrect input")

        except Exception as e:
            print(f"process_fast_access > user_section - {e}")
        finally:
            write_log(data_list=input_list)


class add_process_gui:
    """
    GUI to add new process to list
    """

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title(f"Add Process")
        self.root.minsize(500, 300)
        self.root.maxsize(500, 300)

        # ID Label and text box
        self.title_label = Label(self.root, text="Title")
        self.title_label.config(font="15")
        self.title_label.place(x=0, y=0)
        self.title_textbox = Entry(self.root)
        self.title_textbox.config(font="15")
        self.title_textbox.place(x=140, y=0)

        # reminder data label and textbox
        self.location_label = Label(self.root, text="Location")
        self.location_label.config(font="15")
        self.location_label.place(x=0, y=60)
        self.location_textbox = Entry(self.root, width="30")
        self.location_textbox.config(font="15")
        self.location_textbox.place(x=140, y=60)

        # reminder type label and textbox
        self.codes_label = Label(self.root, text="Codes")
        self.codes_label.config(font="15")
        self.codes_label.place(x=0, y=120)
        self.codes_textbox = Entry(self.root)
        self.codes_textbox.config(font="15")
        self.codes_textbox.place(x=140, y=120)

        # Submit button
        self.submit_button = Button(
            self.root, width=10, text="Submit", command=self.__submit_data
        )
        self.submit_button.place(x=120, y=200)

        # Clear button
        self.clear_button = Button(
            self.root, width=10, text="Clear", command=self.__clear_field
        )
        self.clear_button.place(x=250, y=200)

        mainloop()

    def __clear_field(self) -> None:
        """
        Clear all text fields
        """
        self.title_textbox.delete(0, END)
        self.location_textbox.delete(0, END)
        self.codes_textbox.delete(0, END)

    def __submit_data(self) -> None:
        """
        Submit data and save it to file
        """
        try:
            __process_title = self.title_textbox.get()
            __process_location = self.location_textbox.get()
            __process_codes = self.codes_textbox.get()
            if (
                __process_location in ["", " "]
                or __process_codes in [" ", ""]
                or __process_title in [" ", ""]
            ):
                return
            if process_fast_access().add_new_process(
                title=__process_title,
                location=__process_location,
                codes=__process_codes,
            ):
                # exit()
                self.__clear_field()
        except Exception:
            pass


if __name__ == "__process_fast_access__":
    pass
    # add_process_gui()
