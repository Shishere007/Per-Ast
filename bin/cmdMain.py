from ast import literal_eval
from getpass import getpass
from os import listdir, remove, startfile, system
from pathlib import Path

from pyperclip import paste

from bin import encryption

path = Path("D:")


class list_item:
    def __init__(self):
        self.path = path

    def listAllItem(self, path):  # list all item in the specified directory
        returnList = []
        for file in self.path.glob("*"):
            returnList.append(file)
            print(file)
        return returnList

    # to list the specified language movies or tv series
    def movies_or_tv_series(self, media_type):
        try:
            returnList = []
            media_path_list = {
                # replace media loc by media location
                # if there is multiple locations, type it seperated by comma
                # should follow the pattern ['media loc1','media loc2']
                "anime": [],
                "english": [],
                "korean": [],
                "malayalam": [],
                "tamil": [],
                "hindi": [],
            }
            if media_type in ["all", "media"]:
                for path_list in media_path_list.values():
                    for path in path_list:
                        for file in Path(path).glob("*"):
                            returnList.append(file)
            else:
                for path in media_path_list[media_type]:
                    for file in Path(path).glob("*"):
                        returnList.append(file)
            return returnList
        except Exception as e:
            print(f"cmdMain >movies_or_tv_series :- {e}")


class commands:
    def __init__(self):
        self.path = path
        self.class_call_list_item = list_item()
        self.class_call_reminder = reminder()

    def open(self, cmdList):  # to open the specified the path in windows explorer
        try:
            # correct foder location will be
            media_path_list = {
                "anime": "xx:\\xx\\Anime",
                "anime2": "xx:\\xx\\Anime",
                "eng": "xx:\\xx\\English",
                "english": "xx:\\xx\\English",
                "kor": "xx:\\xx\\Korean",
                "korean": "xx:\\x\\Korean",
                "tamil": ":\\xx\\Tamil",
                "malayalam":"xx:\\xx\\Malayalam",
                "mal": "xx:\\xx\\Malayalam",
                "hindi": "xx:\\xx\\Hindi",
                "music": "xx:\\Music",
            }
            if len(cmdList) == 1:
                startfile(self.path)
            else:
                if cmdList[1] in media_path_list.keys():
                    startfile(Path(media_path_list[cmdList[1]]))
                else:
                    for filename in self.path.glob("*"):
                        if str(filename).lower().__contains__(" ".join(cmdList[1:])):
                            startfile(filename)
                            return
                    else:
                        print("nothing of given name found")
        except Exception as e:
            print(f"cmdMail > commands.open :- {e}")

    def quit(self):  # to close the program
        quit(0)

    def play(self, cmdList):  # to play a media file
        def search_file(media):  # searches for the file's existence in the media list
            try:
                for folderName in media:
                    try:
                        # to check episode number is specified and do accordingly
                        # if not specified raised exception
                        if type(int(cmdList[-1])) == int:
                            if (
                                str(folderName)
                                .lower()
                                .__contains__(" ".join((cmdList[2 : len(cmdList) - 1])))
                            ):
                                print(folderName)
                                startfile(folderName)
                                tempList = [file for file in folderName.glob("*")]
                                print(tempList[int(cmdList[-1]) - 1])
                                if not tempList[0].is_dir():
                                    if len(cmdList) == 4:
                                        startfile(tempList[int(cmdList[3]) - 1])
                                    else:
                                        startfile(tempList[0])
                                break

                    except Exception:
                        if (
                            str(folderName)
                            .lower()
                            .__contains__(" ".join((cmdList[2:])))
                        ):
                            startfile(folderName)
                            tempList = [file for file in folderName.glob("*")]
                            print(tempList[0])
                            if not tempList[0].is_dir():
                                startfile(tempList[0])
                            break
                else:
                    print("no such file or directory")
            except Exception:
                pass

        # if only 'play' command is found, then check the current folder for
        # media files and play if exist, if not shows error

        media_type_list = [
            ["anime"],
            ["malayalam", "mal"],
            ["tamil"],
            ["korean", "kor"],
            ["hindi"],
            ["english", "eng", "hollywood"],
        ]
        if len(cmdList) == 1:
            try:
                for item in self.path.glob("*"):
                    temp = str(item).split(".")[-1]
                    if temp in ["mkv", "mp4", "mp3", "avi"]:
                        startfile(self.path)
                        startfile(item)
                        quit(0)
                        return
                    else:
                        print("No Media file found")
                        return
            except Exception as e:
                print(e)
        else:
            for item in media_type_list:
                if cmdList[1] in item:
                    if len(cmdList) == 2:
                        print("specify  the file")
                    else:
                        media = self.class_call_list_item.movies_or_tv_series(item[0])
                        search_file(media)
                        break
            else:
                print("keyword error")

    def run(self, cmdList):
        try:
            if cmdList[1] == "help":
                print(
                    """run [apps]
                -> mega
                -> firefox
                -> chromium
                -> telegram
                -> Github
                -> Dev-Cpp
                -> Notepad++
                -> netbeans
                -> taskmanager
                -> cmd [cmd command]
                -> teamviewer
                """
                )
            else:
                if not self.processCall(cmdList[1]):
                    print("app not found")
        except Exception:
            print("syntax error")

    def processCall(self, var):
        # this list follows this pattern..
        # ['file path', code names to open this app/file ]
        # the following is of my system apps, configure it to yours
        task_path = [
            ["C:xx\\MEGAsync.exe", "mega"],
            [
                "C:xx\\netbeans64.exe",
                "nb",
                "netbeans",
            ],
            [
                "C:xx\\chrome.exe",
                "chromium",
                "chr",
            ],
            ["C:\\Windows\\System32\\Taskmgr.exe", "task", "taskmanager"],
            ["C:xx\\firefox.exe", "firefox", "ff"],
            ["C:\\Windows\\System32\\cmd.exe", "cmd"],
            [
                "C:\\Users\\xx\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
                "git",
                "github",
            ],
            ["C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe", "idm"],
            ["C:\\Program Files\\Telegram Desktop\\Telegram.exe", "tel", "telegram"],
            [
                "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe",
                "teamviewer",
                "team",
            ],
            ["C:\\Program Files (x86)\\Notepad++\\notepad++.exe", "ntp", "notepad++"],
            ["C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe", "devc", "devcpp"],
            ["run.py", "reload",],
        ]
        cmd_command_list = {
            "tasklist": "tasklist",
            "tasklist det": "tasklist /v",
            "clear": "cls",
            "shut": "shutdown -s",
            "shutdown": "shutdown -s",
            "hibernate": "shutdown -h",
            "hiber": "shutdown -h",
            "logoff": "shutdown -l",
            "resatrt": "shutdown -r",
        }
        try:
            if var in cmd_command_list:
                system(f"{cmd_command_list[var]}")
            elif var in ["groove", "groov", "gr"]:
                system("start mswindowsmusic:")
                print("running...")
            elif var in ["vscode", "code"]:
                system("code")
                print("running...")
            elif var in ["cam", "camera"]:
                system("start microsoft.windows.camera:")
                print("running...")
            elif var.__contains__("cmd"):
                try:
                    if len(var.split()) == 1:
                        self.processCall("cmd")
                    else:  # to run CMD commands directly
                        cmd_command = " ".join(list(var.split())[1:])
                        system(f"{cmd_command}")
                except Exception:
                    pass
            else:
                for item in task_path:
                    if var in item[1:]:
                        if Path(item[0]).exists() :
                            startfile(Path(item[0]))
                            break
                        else :
                            return False
                else:
                    return False
                # returns true or false that will help to now if such keyword is assigned to
                # any task, if yes , app will open, if not can proceed to next condition checking
            self.class_call_reminder.show_curresponding_reminder(var)
            return True
        except Exception:
            pass

    def kill(self, cmdList):
        try:
            task_list = {
                "mega": "MEGAsync.exe",
                "ntp": "notepad++.exe",
                "word": "WINWORD.exe",
                "git": "GitHubDesktop.exe",
                "github": "GitHubDesktop.exe",
                "chr": "chrome.exe",
                "chrome": "chrome.exe",
                "idm": "IDMan.exe",
                "rtb": "RuntimeBroker.exe",
                "ff": "firefox.exe",
                "firefox": "firefox.exe",
                "mozilla": "firefox.exe",
                "code": "Code.exe",
                "nb": "netbeans64.exe",
                "netbeans": "netbeans64.exe",
                "team": "TeamViewer.exe",
                "pot": "PotPlayerMini64.exe",
                "tel": "Telegram.exe",
                "telegram": "Telegram.exe",
                "intelliJ": "idea64.exe",
                "idea": "idea64.exe",
                "ij": "idea64.exe",
                "scene builder": "SceneBuilder.exe",
                "scene": "SceneBuilder.exe",
                "sb": "SceneBuilder.exe",
                "cam": "WindowsCamera.exe",
                "camera": "WindowsCamera.exe",
            }

            check_list = {
                1: ["firefox.exe", "ff", "firefox", "mozilla"],
                2: ["Code.exe", "code"],
                4: ["netbeans64.exe", "nb", "netbeans"],
                5: ["TeamViewer.exe", "team", "teamviewer"],
                6: ["PotPlayerMini64.exe", "pot", "potplayer"],
                7: ["MEGAsync.exe", "mega", "megasync"],
                8: ["IDMan.exe", "idm"],
                9: ["MEGAsync.exe", "mega"],
            }

            def running_process_list():  # get a list of currently running process
                system("tasklist | clip")  # saves output of 'tasklist' to clipboard
                clip = paste()  # paste clipboard content to 'clip' variable
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
            def kill_all(check):
                task_name = list(set(task_list.values()))
                if check in check_list.keys():
                    task_name.remove(check_list[check][0])
                for item in task_name:
                    if item in process_list:
                        # kill a task and its children given its .exe filename
                        system(f"taskkill /im {item} /t /f")

            try:
                pid = int(cmdList[1])
                system(f"taskkill /f /pid {pid}")  # kill a task with its PID
                return
            except Exception:
                pass
            if len(cmdList) == 1 or not "".join(cmdList[1:]).isalpha():
                quit(0)
            elif cmdList[1] == "me":
                # to perform things like
                # restart, shut down, hibernate
                try:
                    if cmdList[2] == "r":  # To resart
                        kill_type = "r"
                    elif cmdList[2] == "l":  # To log off
                        kill_type = "l"
                    elif cmdList[2] == "h":  # To Hibernate
                        system(f"shutdown -h")
                        return
                except Exception:
                    kill_type = "s"  # To shutdown
                finally:
                    kill_all(0)
                    system(f"shutdown -{kill_type}")  # conmand execution
            elif cmdList[1] == "all":
                try:
                    check = 0
                    for item in check_list.keys():
                        if cmdList[2] in check_list[item]:
                            check = item
                            break
                except Exception:
                    pass
                kill_all(check)
            else:
                if cmdList[1] in task_list.keys():
                    item = task_list[cmdList[1]]
                    if item in process_list:
                        system(f"taskkill /im {item} /t /f")
                    else:
                        print("Process is not running")
                else:
                    print("not a app")
        except Exception as e:
            print(e)
            print("syntax error")

    def help(self):
        print(
            """Command list
        -> show                         Show files/folders in Current Path
        -> show [language]              List medias of the given language [media]
        -> run [process]                Run a Process/Application
        -> kill [process]               Kill a Running Process
        -> play [type] [part of name]   Play Media File
        -> open [foldername]            Open Folder in Current Path
        -> set path [new path]          Set new Path
        -> add path [path]              Add new file to hide list
        -> reminder                     Access reminder section
        -> mail                         Access mail section
        -> cmd [command]                To run CMD commands directly
        -> ! [commands]                 Internet related commands
        -> con?                         Check if Internet Connection
        -> clear                        Clear terminal
        -> clear temp                   Clear temporary junk files
        """
        )

    def show(self, cmdList):
        try:
            media_type_list = [
                ["anime"],
                ["malayalam", "mal"],
                ["tamil"],
                ["korean", "kor"],
                ["hindi"],
                ["english", "eng", "hollywood"],
                ["media"],
            ]
            if len(cmdList) > 1:
                for item in media_type_list:
                    if cmdList[1] in item:
                        media_files = self.class_call_list_item.movies_or_tv_series(
                            item[0]
                        )
                        # from the path to the file , remove '\' and print the file name
                        # after splitting the string into list, prints the last string
                        # which will be the filename
                        _ = [print(str(item).split("\\")[-1]) for item in media_files]
                        break
                else:
                    if cmdList.__contains__("path"):
                        # list the files with path to them
                        for file in self.path.glob("*"):
                            print(file)
                    elif cmdList.__contains__("reminder"):
                        self.class_call_reminder.show_reminders("pending")
                    else:
                        print("keyword error")
            else:
                # check to see if the path exists
                if self.path.exists():
                    for filename in listdir(self.path):
                        print(filename)
                else:
                    print("path error")
        except Exception as e:
            print(e)

    def setpath(self, cmdList):
        try:
            if cmdList[1] == "path":
                if Path(str(cmdList[2]).upper()).exists():
                    self.path = Path(str(cmdList[2]).upper())
                    print("path changed : ", self.path)
                else:
                    print("path doesn't exist")
        except Exception:
            print("syntax error")

    def currentPath(self):
        print(f"current path >>> {self.path}")

    def select_directory(self, var):
        try:
            if var == "":
                raise Exception
            for filename in self.path.glob("*"):
                if str(filename).lower().__contains__(var):
                    self.path = filename
                    self.currentPath()
                    return
            else:
                print("Wrong filename")
        except Exception:
            pass
        except Exception as e:
            print(e)

    def clear_temp(self):  # to clear temp files, opens the folder if unable to do so
        # provide correct folder path
        temp_file_path = Path("C:\\Users\\xx\\AppData\\Local\\Temp")
        for file in temp_file_path.glob("*"):
            try:
                remove(file)
            except Exception as e:
                print(e)
                startfile(temp_file_path)
        print("Cleared Successfully")

    def status(self):
        try:
            with open("bin\\Data\\status.txt", "r") as f:
                status = literal_eval(str(f.read()))
            print(
                f"""
                Login Type      :   {status['login_type']}
                Pending Mail    :   {status['mail_pending_count']}
                Pending Task    :   {status['reminder_pending_count']}
            """
            )
        except Exception:
            pass


class reminder:  # class reminder. contains all functions related to reminder feature
    def __init__(self):
        self.class_call_encryption = encryption.encryptCommands()

    def add_reminder(self, reminder_data, reminder_type):  # to add new reminder
        reminder = {}
        try:
            with open("bin\\Data\\reminder.txt", "r") as f:
                reminder_list = f.readlines()
            try:
                while True:
                    reminder_list.remove("\n")
            except Exception:
                pass
            if len(reminder_list) == 0:
                reminder_count = 0
            else:
                item = literal_eval(reminder_list[-1])
                reminder_count = item["id"]
            reminder_count += 1
            # update reminder data into a dictionary to store into a text file
            reminder["id"] = reminder_count
            reminder["data"] = reminder_data
            reminder["status"] = "pending"
            if reminder_type.isalpha():
                reminder["type"] = reminder_type
            else:
                reminder["type"] = "none"
            with open("bin\\Data\\reminder.txt", "a") as f:
                f.write(str(reminder))
                f.write("\n")
            self.change_reminder_status()
            print("Task/reminder added successfully")
        except Exception as e:
            print("sfdsf", e)

    def delete_all_tasks(self):  # delete all the reminders in the file
        try:
            if self.is_pending_task_present():
                choice = input("Pending task present.\nDelete all (y/n) ? : ")
                if choice in ["y", "yes"]:
                    with open("bin\\Data\\reminder.txt", "w"):
                        pass
                    print("All reminders cleared")
                    self.change_reminder_status()
        except Exception as e:
            print(e)

    # to see the reminder list by preference
    def show_reminders(self, reminder_status):
        try:
            flag_count = 0
            with open("bin\\Data\\reminder.txt", "r") as f:
                reminder_list = f.readlines()
            try:
                while True:
                    reminder_list.remove("\n")
            except Exception:
                pass
            if reminder_status in ["pending", "completed", "all", "error"]:
                for item in reminder_list:
                    # convert 'item' into its original datatype
                    item = literal_eval(str(item))
                    if reminder_status in ["pending", "completed"]:
                        if item["status"] != reminder_status:
                            continue
                    flag_count += 1
                    print(
                        f"""
                        ID          :   {item['id']}
                        Reminder    :   {item['data']}
                        Status      :   {item['status']}
                        Type        :   {item['type']}
                    """
                    )
                if flag_count == 0:
                    if reminder_status == "pending":
                        print("No Pending Tasks")
                    elif reminder_status == "completed":
                        print("No Completed Tasks")
                    else:
                        print("No tasks/reminders found")
            else:
                for item in reminder_list:
                    item = literal_eval(str(item))
                    if item["type"] == reminder_status and item["status"] == "pending":
                        flag_count += 1
                        print(
                            f"""
                        ID          :   {item['id']}
                        Reminder    :   {item['data']}
                        Status      :   {item['status']}
                        Type        :   {item['type']}
                    """
                        )
                if flag_count == 0:
                    print(
                        """
                    There are no tasks of given type
                    or
                    wrong reminder type
                    """
                    )

        except Exception as e:
            print(f"cmdMail > reminder.show_reminder :- {e}")

    def task_completed(self, reminder_id):  # to set a task as completed
        try:
            with open("bin\\Data\\reminder.txt", "r") as f:
                reminder_list = f.readlines()
            try:
                while True:
                    reminder_list.remove("\n")
            except Exception:
                pass
            for loopVar in range(len(reminder_list)):
                item = literal_eval(str(reminder_list[loopVar]))
                if item["id"] == reminder_id:
                    # updates the reminder status
                    if not item["status"] == "completed":
                        item["status"] = "completed"
                    else:
                        print("Already completed Task")
                        return
                    reminder_list[loopVar] = item
                    break
            else:
                print("Wrong reminder ID")
                return
            with open("bin\\Data\\reminder.txt", "w") as f:
                for item in reminder_list:
                    f.write(str(item))
                    f.write("\n")
            # to change data in the status file according to the changes made here
            self.change_reminder_status()
            print("Task/reminder updated successfully")
        except Exception as e:
            print(f"cmdMain > reminder.task_completed :- {e}")

    def delete_task(self, reminder_id):  # to delete a specific task
        try:
            with open("bin\\Data\\reminder.txt", "r") as f:
                reminder_list = f.readlines()
            try:
                while True:
                    reminder_list.remove("\n")
            except Exception:
                pass
            for loopVar in range(len(reminder_list)):
                item = literal_eval(str(reminder_list[loopVar]))
                if item["id"] == reminder_id:
                    if item["status"] == "pending":
                        choice = input("task is not yet completed!\nDelete(y/n) ? : ")
                        if choice in ["y", "yes"]:
                            reminder_list.pop(loopVar)
                            break
                        else:
                            return
            else:
                print("Wrong reminder ID")
                return
            with open("bin\\Data\\reminder.txt", "w") as f:
                for item in reminder_list:
                    f.write(str(item))
                    f.write("\n")
            self.change_reminder_status()
            print("Task/reminder deleted successfully")
        except Exception as e:
            print(f"cmdMain > reminder.delete_task :- {e}")

    def is_pending_task_present(self):  # checks if there is pending task
        try:
            pending_task_count = 0
            with open("bin\\Data\\reminder.txt", "r") as f:
                reminder_list = f.readlines()
            try:
                while True:
                    reminder_list.remove("\n")
            except Exception:
                pass
            for item in reminder_list:
                # convert string to dictionary
                item = literal_eval(str(item))
                if item["status"] == "pending":
                    pending_task_count += 1
            if pending_task_count == 0:
                return False
            else:
                return pending_task_count
        except Exception as e:
            print(f"cmdMain > reminder.is_pending_task_present :- {e}")

    # reminder section, reading options from user
    # reads choice and does the corresponding tasks
    def reminder_control(self):
        print("use break or stop to quit reminder/task section")
        while True:
            try:
                user_input = input(">>> ")
                if (
                    len(set(user_input)) == 0
                    or len(set(user_input)) == 1
                    and not user_input.isalnum()
                ):
                    continue
                elif user_input in ["add", "new"]:
                    reminder_data = input("reminder/Task : ")
                    if reminder_data == "kill":
                        continue
                    reminder_type = input("Type : ")
                    self.add_reminder(reminder_data, reminder_type)
                elif user_input.__contains__("comp"):
                    if self.is_pending_task_present():
                        try:
                            task_id = literal_eval(user_input.split()[-1])
                            if type(task_id) == int:
                                self.task_completed(task_id)
                                continue
                        except Exception:
                            try:
                                task_id = input("Task ID : ")
                                if type(literal_eval(task_id)) == int:
                                    self.task_completed(int(task_id))
                            except Exception:
                                pass
                    else:
                        print("No Pending Task found")
                elif user_input.__contains__("del"):
                    if self.class_call_encryption.password_check(
                        (getpass("Password : "))
                    ):
                        try:
                            id = literal_eval(user_input.split()[-1])
                            if type(id) == int:
                                self.delete_task(id)
                                continue
                        except Exception:
                            user_input_copy = user_input.split()
                            if len(user_input_copy) == 1:
                                task_id = input("Task ID : ")
                                try:
                                    if int(task_id):
                                        pass
                                except Exception:
                                    continue
                                self.delete_task(task_id)
                            elif user_input_copy[-1] == "all":
                                if self.class_call_encryption.password_check(
                                    (getpass("Confirm Password : "))
                                ):
                                    self.delete_all_tasks()
                                else:
                                    print("No Access")
                            else:
                                print("keyword error")
                    else:
                        print("No Access")
                elif list(user_input.split())[0] == "show":
                    if len(user_input.split()) == 1 or user_input.__contains__("pend"):
                        self.show_reminders("pending")
                    elif user_input.__contains__("com"):
                        self.show_reminders("completed")
                    elif user_input.__contains__("all"):
                        self.show_reminders("all")
                    else:
                        self.show_reminders(list(user_input.split())[1])
                elif user_input == "help":
                    print(
                        """
                        Command List
                        -> add/new      add new task
                        -> show         view taks [pending,completed,all]
                        -> delete       delete task
                        -> pending      check if pending task present
                    """
                    )
                elif user_input == "pending":
                    pending_task_count = self.is_pending_task_present()
                    if pending_task_count:
                        print(f"There is {pending_task_count} pending task present")
                    else:
                        print(f"There is 0 pending task present")
                elif user_input in ["break", "stop", "kill"]:
                    return
                elif user_input in ["quit", "exit"]:
                    quit(0)
                else:
                    print("not a command")
            except Exception:
                pass

    # to check whether reminder are pending
    def startup_reminder_check(self):
        try:
            with open("bin\\Data\\status.txt", "r") as f:
                status = f.read()
            status = literal_eval(str(status))
            if status["reminder_pending"]:
                print("Press Enter to pass, y/yes to check")
                user_response = input(
                    f"There are {status['reminder_pending_count']} pending reminders.\nwould you like to check ? "
                )
                if user_response.lower() in ["yes", "y"]:
                    self.show_reminders("pending")
                    print("type 'reminder' to access reminder section\n")
        except Exception as e:
            print(e)

    # change reminder status in the status file
    def change_reminder_status(self):
        try:
            with open("bin\\Data\\status.txt", "r") as f:
                status = f.read()
            status = literal_eval(str(status))
            pending_task_count = self.is_pending_task_present()
            if pending_task_count:
                status["reminder_pending"] = True
                status["reminder_pending_count"] = pending_task_count
            else:
                status["reminder_pending"] = False
                status["reminder_pending_count"] = 0
            with open("bin\\Data\\status.txt", "w") as f:
                f.write(str(status))
        except Exception as e:
            print(f"cmdMain > reminder.change_reminder_status :- {e}")

    # show reminders curresponding to a spcific app when that app is opened
    def show_curresponding_reminder(self, reminder_type):
        try:
            flag = True
            if self.is_pending_task_present():
                with open("bin\\Data\\reminder.txt", "r") as f:
                    task_list = f.readlines()
                try:
                    while True:
                        task_list.remove("\n")
                except Exception:
                    pass
                for item in task_list:
                    item = literal_eval(str(item))
                    if item["type"] == reminder_type and item["status"] == "pending":
                        if flag:
                            print("There are tasks pending related to this app")
                            flag = False
                        print(
                            f"""
                    ID          :   {item['id']}
                    Reminder    :   {item['data']}
                    Status      :   {item['status']}
                    Type        :   {item['type']}
                            """
                        )
        except Exception as e:
            print(f"cmdMain > reminder.show_curresponding_reminder :- {e}")


class CMDcall:
    class_call_command = commands()
    class_call_reminder = reminder()

    def cmdCommand(self, user_input):
        try:
            if not self.class_call_command.processCall(user_input):
                if user_input.__contains__("open"):
                    self.class_call_command.open(user_input.split())
                elif user_input in ["quit","exit"]:
                    self.class_call_command.quit()
                elif user_input.__contains__("show"):
                    self.class_call_command.show(user_input.split())
                elif user_input.__contains__("play"):
                    self.class_call_command.play(user_input.split())
                elif user_input.__contains__("run"):
                    self.class_call_command.run(user_input.split())
                elif user_input.__contains__("kill"):
                    self.class_call_command.kill(user_input.split())
                elif user_input == "help":
                    self.class_call_command.help()
                elif user_input == "path":
                    self.class_call_command.currentPath()
                elif user_input.__contains__("sd"):
                    self.class_call_command.select_directory(
                        " ".join(user_input.split(" ")[1:])
                    )
                elif user_input.__contains__("set"):
                    self.class_call_command.setpath(user_input.split())
                elif user_input in ["reminder", "task"]:
                    self.class_call_reminder.reminder_control()
                elif user_input == "clear temp":
                    self.class_call_command.clear_temp()
                elif user_input == "status":
                    self.class_call_command.status()
                else:
                    print("not a command")
        except Exception:
            pass


if __name__ == "__main__":
    pass
