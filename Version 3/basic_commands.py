from ast import literal_eval
from os import listdir, remove, startfile, system
from pathlib import Path

from configure import configure
from file_operation import File
from Folder_fast_access import folder_fast_access, add_folder_gui
from operations import clear_clip, print_list_items, show_date_time
from process_fast_access import process_fast_access, add_process_gui
from Reminder_section import reminder_section, add_reminder_gui
from website_fast_access import website_fast_access, add_website_gui
from media_section import media_section, add_media_gui, show_media_table_gui

try:
    from pyperclip import copy, paste
except Exception:
    print("please wait, installing missing modules")
    system("pip install pyperclip")
    from pyperclip import copy, paste


__name__ = "__basic_commands__"

current_location = Path("D:")

"""
        try:
            pass
        except Exception as e:
            print (f"basic_commands > __list_all_item_at_loc - {e}")
"""


class basic_commands:
    def __init__(self) -> None:
        self.__current_location = current_location
        self.__log_path = "Data/log.json"
        self.__log_file = File(file_location=self.__log_path)

    def __get_file_and_path(self, location: str) -> [str]:
        """
        return two Lists with all items in the given location ,\n
        one with full location and other with only file name
        """

        def __list_all_item_at_loc(location: str) -> [str]:
            """
            List all items in the given location
            """
            try:
                files_list = []
                for file in Path(location).glob("*"):
                    files_list.append(file)
                return files_list
            except Exception as e:
                print(
                    f"basic_commands > __get_file_and_path > __list_all_item_at_loc - {e}"
                )

        file_list_path = __list_all_item_at_loc(location=location)
        # from the path to the file , remove '\' and print the file name
        # after splitting the string into list, prints the last string
        # which will be the filename
        file_list = [str(item).split("\\")[-1].lower() for item in file_list_path]
        return file_list, file_list_path

    def __open(self, user_input: str) -> None:
        """
        To open the specified the path in windows explorer
        """
        try:
            user_input_list = user_input.split()
            # get the list of folders saved for fast access
            folder_list = folder_fast_access().get_folder_list()
            input_length = len(user_input_list)
            if input_length == 1:
                print(f"Opening {self.__current_location}")
                startfile(self.__current_location)
                return
            keyword = user_input_list[1]
            for item in folder_list:
                if keyword in item.get_codes():
                    location = item.get_location()
                    break
            else:
                file_list, file_list_path = self.__get_file_and_path(
                    location=self.__current_location
                )
                name = " ".join(user_input_list[1:])
                for item in file_list:
                    if item == name:
                        print(f"Opening {file_list_path[file_list.index(item)]}")
                        startfile(file_list_path[file_list.index(item)])
                        return
                    if item.__contains__(keyword):
                        location = file_list_path[file_list.index(item)]
                        break
                else:
                    print("wrong folder name or keyword")
                    return
            keywords_count = input_length
            if keywords_count == 2:
                print(f"Opening {location}")
                startfile(location)
                return
            for loopfolder_name in range(2, keywords_count):
                keyword = user_input_list[loopfolder_name]
                file_list, file_list_path = self.__get_file_and_path(location=location)
                name = " ".join(user_input_list[loopfolder_name:])
                for item in file_list:
                    if item == name:
                        print(f"Opening {file_list_path[file_list.index(item)]}")
                        startfile(file_list_path[file_list.index(item)])
                        return
                    if item.__contains__(keyword):
                        location = file_list_path[file_list.index(item)]
                        break
            print(f"Opening {location}")
            startfile(location)
        except Exception as e:
            print(f"basic_commands > __open - {e}")

    def __kill(self, user_input: str) -> None:
        """
        Terminate process' with kill keyword
        """
        try:
            user_input_list = user_input.split()
            """
            Add these to list
            task_list_temp = [
                ["RuntimeBroker.exe", "rtb", "runtimebroker"],
                ["WINWORD.exe", "word"],
                ["WindowsCamera.exe", "cam", "camera"],
                ["Code.exe", "code", "vscode"],
            ]"""
            task_list = process_fast_access().get_process_list()

            def running_process_list() -> [str]:
                """
                Get a list of currently running process
                """
                system("tasklist | clip")  # saves output of 'tasklist' to clipboard
                clip = paste()  # paste clipboard content to 'clip' folder_nameiable
                clip = clip.split("\n")
                clip = [item.split() for item in clip]
                process_list = []
                for item in clip:
                    try:
                        if item[0].__contains__(".exe"):
                            process_list.append(item[0])
                    except Exception:
                        pass
                return process_list

            process_list = running_process_list()
            # _ = [print (item) for item in process_list]
            def kill_all(process_name: str) -> None:
                for item in task_list:
                    if item.get_exe_name() in process_list:
                        codes = item.get_codes()
                        if process_name in codes or "cmd" in codes or "reload" in codes:
                            continue
                        # kill a task and its children given its .exe filename
                        system(f"taskkill /im {item.get_exe_name()} /t /f")

            try:
                pid = int(user_input_list[1])
                system(f"taskkill /f /pid {pid}")  # kill a task with its PID
                return False
            except Exception:
                pass
            if user_input_list[0] in ["kill"]:
                if (
                    len(user_input_list) == 1
                    or not "".join(user_input_list[1:]).isalpha()
                ):
                    return True
                elif user_input_list[1] == "all":
                    if len(user_input_list) > 2:
                        kill_all(process_name=user_input_list[2])
                    else:
                        kill_all(process_name="none")
                else:
                    for item in task_list:
                        if user_input_list[1] in item.get_codes():
                            process_name = item.get_exe_name()
                            if process_name in process_list:
                                system(f"taskkill /im {process_name} /t /f")
                            else:
                                print("Process is not running")
                            break
                    else:
                        print("not a app")
            else:
                print("incorrect command")
            clear_clip()
            return False
        except Exception as e:
            print(f"basic_commands > __Kill - {e}")

    def __help(self) -> None:
        print(
            """Command list
        -> show                         Show files/folders in Current Path
        -> show [language]              List medias of the given language [media]
        -> run [process]                Run a Process/Application
        -> kill [process]               Kill a Running Process
        -> open [foldername]            Open Folder in Current Path
        -> set path [new path]          Set new Path
        -> add path [path]              Add new file to hide list
        -> cmd [command]                To run CMD commands directly
        -> ! [commands]                 Internet related commands
        -> con?                         Check if Internet Connection
        -> clear                        Clear terminal
        -> clear temp                   Clear temporary junk files
        -> Special Sections
            ->> reminder                     Access reminder section
            ->> sitelist/site_list           Access sitelist section
            ->> processlist                  Access processlist section
            ->> filelist/folderlist          Access folder fast access section
            ->> hidefile/hide_file           Access file hiding section
        

        # For detailed command list look through README.md
        """
        )

    def __show(self, user_input: str) -> None:
        """
        Show items in the folder or specified location
        """
        try:
            user_input_list = user_input.split()
            folder_list = folder_fast_access().get_folder_list()
            input_length = len(user_input_list)
            if input_length in [2, 3, 4]:
                for item in folder_list:
                    # to show files in the saved file locations/saved folders
                    if user_input_list[1] in item.get_codes():
                        file_list, file_path_list = self.__get_file_and_path(
                            location=item.get_location()
                        )
                        if input_length == 3 and user_input_list[2] == "path":
                            print_list_items(file_list=file_path_list)
                        elif input_length == 2:
                            print_list_items(file_list=file_list)
                        else:
                            raise UserWarning
                        break
                else:
                    if input_length >= 3:
                        if user_input_list[1] in configure().get_keywords(
                            data_type="media"
                        ):
                            if user_input_list[2] == "status":
                                media_section().show_media_status()
                            else:
                                user_input_list.pop(1)
                                media_section().show_media_list(
                                    user_input=" ".join(user_input_list)
                                )
                            return
                    if not input_length == 2:
                        raise UserWarning
                        # return
                    if user_input_list[1] in ["path"]:
                        # list the files with path to them
                        print_list_items(file_list=self.__current_location.glob("*"))
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="configure"
                    ):
                        configure().show()
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="reminder"
                    ):
                        reminder_section().show_reminder()
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="website"
                    ):
                        website_fast_access().show_website_list()
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="process"
                    ):
                        process_fast_access().show_process_list()
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="folder"
                    ):
                        folder_fast_access().show_folder_list()
                    elif user_input_list[1] in configure().get_keywords(
                        data_type="media"
                    ):
                        media_section().show_media_list(user_input="show")
                    else:
                        raise UserWarning
            elif input_length == 1:
                # check to see if the path exists
                if self.__current_location.exists():
                    print_list_items(file_list=listdir(self.__current_location))
                else:
                    print("Invalid path")
            else:
                print("incorrent input")
        except UserWarning:
            print("Incorrect keyword found")
        except Exception as e:
            print(f"basic_commands > __show - {e}")

    def __setpath(self, user_input: str) -> None:
        """
        specifically set a new path
        """
        try:
            user_input_list = user_input.split()
            if user_input_list[1] in ["home"]:
                self.__current_location = Path("D:")
                print("path changed : ", self.__current_location)
            elif user_input_list[1] == "path":
                if Path(str(user_input_list[2]).upper()).exists():
                    self.__current_location = Path(str(user_input_list[2]).upper())
                    print("path changed : ", self.__current_location)
                else:
                    print("path doesn't exist")
            else:
                print("Incorrect keyword")
        except Exception as e:
            print(f"basic_commands > __setpath - {e}")

    def __currentPath(self) -> None:
        """
        print current location in the directory
        """
        print(f"current path >>> {self.__current_location}")

    def __select_directory(self, folder_name: str) -> None:
        """
        change directory by by selecting any folder in the current directly with keyword 'sd'
        """
        try:
            if folder_name == "":
                raise Exception
            for filename in self.__current_location.glob("*"):
                if str(filename).lower().__contains__(folder_name):
                    self.__current_location = filename
                    self.__currentPath()
                    return
            else:
                print("Wrong filename")
        except Exception:
            pass
        except Exception as e:
            print(f"basic_commands > __select_directory - {e}")

    def __clear(self, user_input: str) -> None:
        """
        To clear temp files, opens the folder if unable to do so
        """
        try:
            user_input_list = user_input.split()
            if user_input_list[1] in ["temp"]:
                location = Path("C:\\Users\\Shishere\\AppData\\Local\\Temp")
            elif user_input_list[1] in ["clip"]:
                clear_clip()
                return
            for file in location.glob("*"):
                try:
                    # remove the file from directory
                    remove(file)
                except Exception as e:
                    print(e)
                    # opens the location if there are some files which were unable to delete
                    # to delete manually
                    startfile(location)
            print("Cleared Successfully")
        except Exception as e:
            print(f"basic_commands > __clear - {e}")

    def __add_or_new(self, user_input: str) -> None:
        """
        Add new reminder,folder,process,website from main section
        """
        try:
            keyword = user_input.split()[1]
            if keyword in configure().get_keywords(data_type="reminder"):
                if user_input.__contains__("gui"):
                    add_reminder_gui()
                    return
                reminder_section().add_reminder()
            elif keyword in configure().get_keywords(data_type="folder"):
                if user_input.__contains__("gui"):
                    add_folder_gui()
                    return
                folder_fast_access().add_folder()
            elif keyword in configure().get_keywords(data_type="process"):
                if user_input.__contains__("gui"):
                    add_process_gui()
                    return
                process_fast_access().add_process()
            elif keyword in configure().get_keywords(data_type="website"):
                if user_input.__contains__("gui"):
                    add_website_gui()
                    return
                website_fast_access().add_website()
            elif keyword in configure().get_keywords(data_type="media"):
                add_media_gui()
            else:
                print("Incorrect Keyword")
        except Exception as e:
            print(f"basic_commands > __add_or_new - {e}")

    def __delete(self, user_input: str) -> None:
        """
        delete reminder,folder,process,website from main section
        """
        try:
            keyword = user_input.split()[1]
            try:
                send_input = "del " + user_input.split()[2]
            except Exception:
                send_input = "del"
            if keyword in configure().get_keywords(data_type="reminder"):
                reminder_section().delete_reminder(user_input=send_input)
            elif keyword in configure().get_keywords(data_type="folder"):
                folder_fast_access().delete_folder(user_input=send_input)
            elif keyword in configure().get_keywords(data_type="process"):
                process_fast_access().delete_process(user_input=send_input)
            elif keyword in configure().get_keywords(data_type="website"):
                website_fast_access().delete_website(user_input=send_input)
            else:
                print("Incorrect Keyword")
        except Exception as e:
            print(f"basic_commands > __delete - {e}")

    def __complete(self, user_input: str) -> None:
        """
        complete reminder from main section
        """
        try:
            keyword = user_input.split()[1]
            try:
                send_input = "comp " + user_input.split()[2]
            except Exception:
                send_input = "comp"
            if keyword in configure().get_keywords(data_type="reminder"):
                reminder_section().complete_reminder(user_input=send_input)
            else:
                print("Incorrect Keyword")
        except Exception as e:
            print(f"basic_commands > __complete - {e}")

    def __show_log(self) -> None:
        """
        Show complete list of command log
        """
        try:
            file_data = self.__log_file.read_data()
            for item in file_data:
                print(item)
        except Exception as e:
            print(f"basic_commands > __show_log - {e}")

    def user_section(self, user_input: str) -> bool:
        def length(user_input: str) -> bool:
            if len(user_input.split()) == 1:
                print("Incomplete command")
                return True
            return False

        try:
            keyword = user_input.split()[0]
            app_status = process_fast_access().run_process(keycode=user_input)
            if app_status == "shut":
                return True
            elif not app_status:
                if keyword in ["open"]:
                    self.__open(user_input=user_input)
                elif user_input in ["quit", "exit"]:
                    return True
                elif keyword in ["show"]:
                    self.__show(user_input=user_input)
                elif keyword in ["kill"]:
                    if self.__kill(user_input=user_input):
                        return True
                elif user_input == "help":
                    self.__help()
                elif user_input in ["path", "location", "loc"]:
                    self.__currentPath()
                elif keyword in ["sd"]:
                    self.__select_directory(folder_name=user_input.split()[1])
                elif keyword in ["set"]:
                    self.__setpath(user_input=user_input)
                elif keyword == "clear":
                    self.__clear(user_input=user_input)
                elif keyword in ["add", "new"]:
                    if not length(user_input=user_input):
                        self.__add_or_new(user_input=user_input)
                elif keyword in ["del", "delete"]:
                    if not length(user_input=user_input):
                        self.__delete(user_input=user_input)
                elif keyword in ["comp", "complete"]:
                    if not length(user_input=user_input):
                        self.__complete(user_input=user_input)
                elif keyword in ["now", "date", "time"]:
                    show_date_time()
                elif user_input in ["med status", "media status"]:
                    media_section().show_media_status()
                elif keyword in ["log"]:
                    self.__show_log()
                else:
                    print("incorrect Command")
                    return False

        except Exception as e:
            print(f"basic_commands > user_section - {e}")


if __name__ == "__basic_commands__":
    pass
