from pathlib import Path
from tkinter import END, Button, Entry, Label, StringVar, Tk, mainloop, ttk

from data_types import convert, folder, log
from file_operation import File
from operations import (
    change_status,
    clear_screen,
    duplicate,
    get_date_time,
    is_input_kill,
    write_log,
)

__name__ = "__folder_fast_access__"


class folder_fast_access(change_status):
    """
    Save folder for fast access with keyword
    """

    def __init__(self) -> None:
        super().__init__()
        self.__folder_data_path = "Data/folder_data.json"
        self.__folder_file = File(file_location=self.__folder_data_path)

    def add_folder(self) -> None:
        """
        To add folder from main section
        """
        self.__read_data_for_new_folder()

    def __read_data_for_new_folder(self) -> None:
        """
        Read data for adding new folder
        """
        try:
            self.__dupe = duplicate(
                data_list=self.__folder_file.read_data(), data_type="folder"
            )
            folder_name = input("Folder Name : ")
            if is_input_kill(data=folder_name):
                return
            folder_location = input("Folder Location(Full) : ")
            if is_input_kill(data=folder_location):
                return
            # check if location exists
            if not Path(folder_location).exists():
                print("Invalid folder location")
                return
            # check if the location is alraedy in list
            if self.__dupe.is_file_exists(location=folder_location):
                print("Folder is already in list")
                return
            print("Type the keywords for faster access seperated buy comma")
            folder_codes = input("Folder codes : ").split(",")
            if self.__dupe.is_keyword_exist(keyword_list=folder_codes):
                print(f"one of the keyword is already in use")
                return
            new_folder = folder(
                title=folder_name, location=folder_location, codes=folder_codes
            )
            self.__add_new_folder(new_folder=new_folder)
        except Exception as e:
            print(f"folder_fast_access > __read_data_for_new_folder- {e}")

    def get_folder_list(self) -> [folder]:
        """
        Get list of folders saved for fast access
        """
        return duplicate(
            data_list=self.__folder_file.read_data(), data_type="folder"
        ).get_converted_list()

    def add_new_folder(self, title: str, location: str, codes: [str]) -> bool:
        """
        Add new process from outside the class(public fucntion)
        """
        self.__dupe = duplicate(
            data_list=self.__folder_file.read_data(), data_type="process"
        )
        if not Path(location).exists():
            print("Invalid folder location")
            return False
        if self.__dupe.is_file_exists(location=location):
            print("folder is already in list")
            return False
        keycodes = codes.split(",")
        if self.__dupe.is_keyword_exist(keyword_list=keycodes):
            print(f"one of the keyword is already in use")
            return False
        self.__add_new_folder(
            new_folder=folder(title=title, location=location, codes=keycodes)
        )
        return True

    def __add_new_folder(self, new_folder: folder) -> None:
        """
        Add new folder for access
        """
        try:
            if not self.__folder_file.append_one_data(data_to_append=new_folder):
                print("Unable to add new folder")
                return
            print("New folder is added Successfully ")
            self.__change_folder_status()
        except Exception as e:
            print(f"folder_fast_access > __add_new_folder- {e}")

    def delete_folder(self, user_input: str) -> None:
        """
        To delete a folder as completed from main section
        """
        self.__delete_folder_read_data(user_input=user_input)

    def __delete_folder_read_data(self, user_input: str) -> None:
        """
        Delete a folder from list
        """
        try:
            if len(user_input.split()) > 1:
                folder_code = " ".join(user_input.split()[1:])
            else:
                folder_code = input("Folder code : ")
            if folder_code.isalpha():
                self.__delete_folder(folder_code=folder_code)
            else:
                print("incorrent input")
        except Exception as e:
            print(f"folder_fast_access > __delete_folder_read_data- {e}")

    def __delete_folder(self, folder_code: str) -> None:
        try:
            folder_list = self.__folder_file.read_data()
            for item in folder_list:
                if folder_code in convert(file_data=item).to_folder().get_codes():
                    self.__folder_file.delete_one_data(
                        file_data=folder_list, data_to_delete=item
                    )
                    self.__change_folder_status()
                    print("Folder deleted from list")
                    return
            else:
                print(f" No folder found with '{folder_code}' keyword'")
        except Exception as e:
            print(f"folder_fast_access > __delete_folder- {e}")

    def show_folder_list(self) -> None:
        """
        Show all the fast access folder list
        """
        try:
            folder_list = self.__folder_file.read_data()
            if len(folder_list) == 0:
                print("list is empty")
                return
            for item in folder_list:
                convert(file_data=item).to_folder().show()
        except Exception as e:
            print(f"folder_fast_access > show_folder_list- {e}")

    def folder_help(self) -> None:
        """
        Shows command list
        """
        print(
            """
            Command list
            -> add/new      add new folder to fast access list
            -> del/delete   remove folder from list
            -> show         List all folder list          
        """
        )

    def __change_folder_status(self) -> None:
        """
        change no of folder count status data
        """
        try:
            current_status = self._change_status__get_status()
            current_status.set_folder_list_count(
                folder_count=self.__folder_file.line_count()
            )
            self._change_status__write_status_to_file(current_status=current_status)
        except Exception as e:
            print(f"folder_fast_access > __change_folder_status- {e}")

    def user_section(self) -> bool:
        """
        User section for adding removing folder's from list
        """
        try:
            input_list = []
            print("Type break/stop to exit section")
            while True:
                user_input = str(input(">>>"))
                input_list.append(
                    log(
                        user_input=user_input,
                        section="folder",
                        date_time=get_date_time(),
                    )
                )
                if (
                    len(set(user_input)) == 0
                    or len(set(user_input)) == 1
                    and not user_input.isalnum()
                ):
                    continue
                if user_input in ["new", "add"]:
                    self.__read_data_for_new_folder()
                elif user_input.split()[0] in ["del", "delete"]:
                    self.__delete_folder_read_data(user_input=user_input)
                elif user_input in ["help"]:
                    self.folder_help()
                elif user_input in ["show"]:
                    self.show_folder_list()
                elif user_input in ["status"]:
                    change_status().show_status()
                elif user_input in ["quit", "exit"]:
                    return True
                elif user_input in ["break", "stop", "kill"]:
                    return False
                elif user_input in ["clear"]:
                    clear_screen()
                else:
                    print("incorrect input")

        except Exception as e:
            print(f"folder_fast_access > user_section - {e}")
        finally:
            write_log(data_list=input_list)


class add_folder_gui:
    """
    GUI to add new folder to list
    """

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title(f"Add folder")
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
            __folder_title = self.title_textbox.get()
            __folder_location = self.location_textbox.get()
            __folder_codes = self.codes_textbox.get()
            if (
                __folder_location in ["", " "]
                or __folder_codes in [" ", ""]
                or __folder_title in [" ", ""]
            ):
                return
            if folder_fast_access().add_new_folder(
                title=__folder_title, location=__folder_location, codes=__folder_codes,
            ):
                # exit()
                self.__clear_field()
        except Exception:
            pass


if __name__ == "__folder_fast_access__":
    pass
    # add_folder_gui()
