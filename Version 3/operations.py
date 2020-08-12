import json
from datetime import date, datetime
from os import system

from data_types import (
    config,
    convert,
    folder,
    media,
    process,
    reminder,
    status,
    website,
)
from file_operation import File

try:
    from bs4 import BeautifulSoup
except Exception:
    print("please wait, installing missing modules")
    system("pip install bs4")
    from bs4 import BeautifulSoup
try:
    from requests.api import get
except Exception:
    print("please wait, installing missing modules")
    system("pip install requests")
    from requests.api import get


__name__ = "__operations__"


def write_log(data_list: list) -> None:
    """
    Write the log to the file
    """
    file_data = File(file_location="Data/log.json").read_data()
    if file_data == None:
        file_data = []
    for item in data_list:
        if item == "":
            continue
        file_data.append(item.to_string())
    with open("Data/log.json", "w") as file:
        json.dump(file_data, file)


def is_input_kill(data: str) -> bool:
    """
    Return True if data is 'kill',
    False otherwise
    """
    return data in ["kill"]


def clear_screen() -> None:
    """
    The CLI screen
    """
    system("cls")


def clear_clip() -> None:
    """
    Clear last pasted item in clipboard
    """
    system(f"echo.|clip")


def print_list_items(file_list: list) -> None:
    """
    print all items in the list
    """
    for file_name in file_list:
        print(file_name)


def remove_char_from_string(string: str, character: str) -> str:
    """
    return a new string without the specified character
    """
    string_list = list(string)
    string_list.remove(character)
    return "".join(string_list)


def add_character(string: str, character_1: str, character_2: str) -> str:
    """
    Add character_2 after the first character_1
    """
    string_list = list(string)
    index = string_list.index(character_1) + 1
    new_list = string_list[:index] + [character_2] + string_list[index:]
    return "".join(new_list)


def complete_website(site: str) -> str:
    """
    checks if site contains 'http://' or 'https://', if not
    adds it return the site
    """
    if not (site.__contains__("https://") or site.__contains__("http://")):
        site = "http://" + site
    return site


def is_null_string(string: str) -> bool:
    """
    Check if string is null and return bool accordingly
    """
    return string == ""


def is_connected() -> bool:
    """
    Check if system is connected internet and return in boolean
    """
    url = "http://www.google.com/"
    timeout = 5
    try:
        _ = get(url, timeout=timeout)
        return True
    except Exception:
        return False


def internet_connection() -> None:
    """
    Check if internet connection is avillable and show 
    corresponding message, if internet connection is available or not
    """
    if is_connected():
        print("Internet connection is available")
    else:
        print("No Internet Connection")


def get_date_time() -> datetime:
    """
    return the current date
    """
    # get date time in 05-Mar-2020 02:01:30 PM format
    return datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")


def show_date_time() -> None:
    """
    Show current date and time
    """
    print(get_date_time())



def get_date() -> date:
    """
    return the current date
    """
    # get date in 01-Jan-2020 format
    return date.today().strftime("%d-%b-%Y")


def is_a_website(site: str) -> bool:
    """
    Check if given is a valid website by checking the presents of
    domains like ".com",".net" return boolean
    """
    if (
        site.__contains__(".com")
        or site.__contains__(".net")
        or site.__contains__(".org")
        or site.__contains__(".in")
        or site.__contains__(".co.in")
        or site.__contains__("net")
    ):
        return True
    return False


def minutes_to_day_hour_min(time: int):
    """
    Convert minutes to DAy HOUR MINUT format
    eg:
    100 minutes ->  0 days, 1 hours, 40 mins
    """
    days = 0
    hours = 0
    mins = 0
    days = time // 1440
    leftover_minutes = time % 1440
    hours = leftover_minutes // 60
    mins = time - (days * 1440) - (hours * 60)
    return str(days) + " days, " + str(hours) + " hours, " + str(mins) + " mins. "


def get_duration_of_movie(movie_name: str, movie_category: str) -> int:
    """
    Get duration of a movie, if unable to find returns zero
    """
    duration_in_min = 0
    try:
        print("Fetching data, please wait")
        if movie_name == "" and movie_category == "":
            return 0
        page_data = get(
            f"https://www.google.com/search?q={movie_name}+{movie_category}+movie+duration"
        )
        soup = BeautifulSoup(page_data.content, features="html.parser")
        duration_data = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
        duration_str_form = duration_data.split("‧")[
            2
        ]  ##Gives the duration of the movie
        duration_split = duration_str_form.split(" ")
        for item in duration_split:
            if item in ["", " "]:
                continue
            elif item.__contains__("h"):
                duration_in_min += int("".join(list(item)[:-1:])) * 60
            elif item.__contains__("m"):
                duration_in_min += int("".join(list(item)[:-1:]))
    except Exception:
        print("error found")
        duration_in_min = 0
    finally:
        print(duration_in_min)
        return duration_in_min


class duplicate:
    """
    to check if a keyword or file already exists
    and also covert a list strings to their original datatype
    like folder, process, website
    """

    def __init__(self, data_list: list, data_type: str) -> None:
        self.__data_list = self.__convert(data_list=data_list, data_type=data_type)

    def get_converted_list(self) -> list:
        """
        get converted data list
        """
        return self.__data_list

    def __string_to_folder(self, data_list: list) -> [folder]:
        """
        convert all data in data_list to folder datatype and return as list
        """
        folder_list = []
        for item in data_list:
            folder_list.append(convert(file_data=item).to_folder())
        return folder_list

    def __string_to_website(self, data_list: list) -> [website]:
        """
        convert all data in data_list to website datatype and return as list
        """
        website_list = []
        for item in data_list:
            website_list.append(convert(file_data=item).to_website())
        return website_list

    def __string_to_process(self, data_list: list) -> [process]:
        """
        convert all data in data_list to process datatype and return as list
        """
        process_list = []
        for item in data_list:
            process_list.append(convert(file_data=item).to_process())
        return process_list

    def __string_to_reminder(self, data_list: list) -> [reminder]:
        """
        convert all data in data_list to reminder datatype and return as list
        """
        reminder_list = []
        for item in data_list:
            reminder_list.append(convert(file_data=item).to_reminder())
        return reminder_list

    def __string_to_media(self, data_list: list) -> [media]:
        """
        convert all data in data_list to media datatype and return as list
        """
        media_list = []
        for item in data_list:
            media_list.append(convert(file_data=item).to_media())
        return media_list

    def __convert(self, data_type, data_list: list) -> []:
        """
        Convert all data in list into specified dataype and return as list
        """
        if data_type == "process":
            return self.__string_to_process(data_list=data_list)
        elif data_type == "folder":
            return self.__string_to_folder(data_list=data_list)
        elif data_type == "website":
            return self.__string_to_website(data_list=data_list)
        elif data_type == "reminder":
            return self.__string_to_reminder(data_list=data_list)
        elif data_type == "media":
            return self.__string_to_media(data_list=data_list)

    def is_keyword_exist(self, keyword_list: list) -> bool:
        """
        Check if 'keyword' is already  being used as fast access 
        keyword in in the given list of files
        """

        try:
            for item in self.__data_list:
                codes = item.get_codes()
                for keyword in keyword_list:
                    if keyword in codes:
                        return True
            return False
        except Exception as e:
            print(f"operation > is_keyword_exist - {e}")

    def is_file_exists(self, location: str) -> bool:
        """
        Check if the file/site/process with given location/address 
        aleady exists
        """
        try:
            for item in self.__data_list:
                if item.is_same(location=location):
                    return True
            return False
        except Exception as e:
            print(f"operation > is_file_exists - {e}")


class change_status:
    """
    pre-defined commands to change read and change status data
    """

    def __init__(self) -> None:
        self.__status_file_path = "Data/status.json"
        self.__status_file = File(file_location=self.__status_file_path)

    def __get_status(self) -> status:
        """
        Return the current status data
        """
        return convert(file_data=self.__status_file.read_data()[0]).to_status()

    def __write_status_to_file(self, current_status: status) -> None:
        """
        write the changed new status to file
        """
        self.__status_file.rewrite_entire_data(file_data=[current_status])

    def show_status(self) -> None:
        """
        Show current status
        """
        self.__get_status().show()


if __name__ == "__operations__":
    pass
