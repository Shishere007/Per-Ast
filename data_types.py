"""
Creating datatypes which is to be used in CLI program
and converting string data types to its original datatype form
Defined Data types :
    > Process
    > Folder
    > Website
    > Reminder
    > Status
"""

from ast import literal_eval
from datetime import datetime

__name__ = "DataType"


class base_class:
    """ 
        Base Class Datatype. with titles, its .exe file location and codes
        for faster access
    """

    def __init__(self, title: str, location: str, codes: [str]) -> None:
        self.__title = title
        self.__location = location
        self.__codes = codes

    def __str__(self) -> str:
        return f"{{'Title':'{self.__title}','Location':'{self.__location}','codes':{self.__codes}}}"

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        {format_spec} Title       :   {self.__title}
        {format_spec} Location    :   {self.__location}
        {format_spec} Codes       :   {" , ".join(self.__codes)}
        """

    def format(self) -> str:
        return self.__format__()

    def to_dictionary(self) -> dict:
        """
        Convert current into dictionary datatype
        """
        dic = {}
        dic["Title"] = self.__title
        dic["Location"] = self.__location
        dic["codes"] = self.__codes
        return dic

    def get_title(self) -> str:
        """
        return object title
        """
        return self.__title

    def get_codes(self) -> [str]:
        """
        return codes used for fast access
        """
        return self.__codes

    def get_location(self) -> str:
        """
        Return the location saved
        """
        return self.__location

    def is_same(self, location: str) -> bool:
        """
        check if 'location' is same as this objects location
        and returns boolean
        """
        return self.__location == location


class process(base_class):
    """
        Process Datatype
    """

    def __init__(self, title: str, location: str, codes: [str]) -> None:
        super().__init__(title=title, location=location, codes=codes)

    def __format__(self, format_spec: str = "Process") -> str:
        return super().__format__(format_spec=format_spec)

    def show(self) -> None:
        """
        print data in specific format
        """
        print(self.__format__())

    def get_exe_name(self) -> str:
        """
        return executable file name(full)
        """
        return self.get_location().split("\\")[-1]


class folder(base_class):
    """
        Folder Datatype
    """

    def __init__(self, title: str, location: str, codes: [str]) -> None:
        super().__init__(title=title, location=location, codes=codes)

    def __format__(self, format_spec: str = "Folder") -> str:
        return super().__format__(format_spec=format_spec)

    def show(self) -> None:
        """
        print data in specific format
        """
        print(self.__format__())


class website(base_class):
    """
        Website Datatype
    """

    def __init__(self, title: str, location: str, codes: [str]) -> None:
        super().__init__(title=title, location=location, codes=codes)

    def __format__(self, format_spec: str = "Website"):
        return super().__format__(format_spec=format_spec)

    def show(self) -> None:
        """
        print data in specific format
        """
        print(self.__format__())


class reminder:
    """ 
        Reminder Datatype. with reminder ID, matter which is to be reminded,
        type of reminder and reminder status
    """

    def __init__(
        self,
        new: bool = False,
        reminder_id: int = None,
        reminder_data: str = None,
        reminder_type: str = None,
        reminder_status: str = "pending",
        added_date: datetime = None,
        completed_date: datetime = None,
    ) -> None:
        # private variables
        self.__reminder_id = reminder_id
        self.__reminder_data = reminder_data
        self.__reminder_type = reminder_type
        self.__added_date = self.__set_date(new=new, added_date=added_date)
        self.__reminder_status = reminder_status
        self.__completed_date = completed_date

    def __str__(self) -> str:
        return f"{{'ID':'{self.__reminder_id}', 'Data': '{self.__reminder_data}', 'Type': '{self.__reminder_type}', 'Added_on': '{self.__added_date}', 'Status': '{self.__reminder_status}', 'Completed_on': '{self.__completed_date}'}}"

    def to_string(self) -> str:
        """
        Converet reminder to string
        """
        return self.__str__()

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Reminder ID     :   {self.__reminder_id}
        Data            :   {self.__reminder_data}
        Type            :   {self.__reminder_type}
        Added On        :   {self.__added_date}     
        Status          :   {self.__reminder_status}
        Completed On    :   {self.__completed_date}
        """

    def __set_date(self, new: bool, added_date: datetime) -> datetime:
        """
        Arrange date
        """
        if new:
            return self.__get_date_time()
        else:
            return added_date

    def to_dictionary(self) -> dict:
        """
        Convert reminder into dictionary datatype
        """
        dic = {}
        dic["ID"] = self.__reminder_id
        dic["Data"] = self.__reminder_data
        dic["Type"] = self.__reminder_type
        dic["Added_on"] = self.__added_date
        dic["Status"] = self.__reminder_status
        dic["Completed_on"] = self.__completed_date
        return dic

    def format(self) -> str:
        """
        Returns the reminder in specific format
        """
        return self.__format__()

    def show(self) -> None:
        """
        Prints the reminder in specific format
        """
        print(self.format())

    def get_id(self) -> int:
        """
        Returns the ID of the reminder
        """
        return int(self.__reminder_id)

    def get_type(self) -> str:
        """
        Returns the Type of the reminder
        """
        return self.__reminder_type

    def get_status(self) -> str:
        """
        Returns the Status of the reminder
        """
        return self.__reminder_status

    def set_status(self, status: str = "completed") -> None:
        """
        set Status to 'Completed' by default
        or to the specified one
        """
        self.__reminder_status = status
        self.__completed_date = self.__get_date_time()

    def is_completed(self) -> bool:
        """
        Returns True if reminder status is 'completed', 
        False otherwise
        """
        return self.__reminder_status == "completed"

    def __get_date_time(self):
        """
        return the current date
        """
        # get date time in 05-Mar-2020 02:01:30 PM format
        return datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")


class status:
    """
    Status data type. Store basic details like login type,
    reminder and things like that
    """

    def __init__(
        self,
        login_type: str = None,
        reminder_pending: bool = False,
        reminder_pending_count: int = 0,
        site_list_count: int = 0,
        folder_list_count: int = 0,
        process_list_count: int = 0,
    ) -> None:
        self.__login_type = login_type
        self.__reminder_pending = reminder_pending
        self.__reminder_pending_count = reminder_pending_count
        self.__site_list_count = site_list_count
        self.__folder_list_count = folder_list_count
        self.__process_list_count = process_list_count

    def __str__(self) -> None:
        return f"{{'login_type': '{self.__login_type}', 'reminder_pending': '{self.__reminder_pending}', 'reminder_pending_count': '{self.__reminder_pending_count}', 'site_list': '{self.__site_list_count}', 'folder_list': '{self.__folder_list_count}', 'process_list': '{self.__process_list_count}'}}"

    def to_string(self) -> str:
        """
        Return data in string format
        """
        return self.__str__()

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Login Type              :   {self.__login_type}
        Reminder Pending        :   {self.__reminder_pending}
        Reminder Pending Count  :   {self.__reminder_pending_count}
        Folder List Count       :   {self.__folder_list_count}
        Site List Count         :   {self.__site_list_count}
        Process List Count      :   {self.__process_list_count}
        """

    def format(self) -> str:
        return self.__format__()

    def show(self) -> None:
        print(self.format())

    def to_dictionary(self) -> dict:
        """
        Convert status datatype into dictionary datatype
        """
        dic = {}
        dic["login_type"] = self.__login_type
        dic["reminder_pending"] = self.__reminder_pending
        dic["reminder_pending_count"] = self.__reminder_pending_count
        dic["site_list"] = self.__site_list_count
        dic["folder_list"] = self.__folder_list_count
        dic["process_list"] = self.__process_list_count
        return dic

    def get_login_type(self) -> str:
        """
        Return Login type
        """
        return self.__login_type

    def get_reminder_pending_status(self) -> bool:
        """
        True : Reminder Pending\n
        False : Reminder not Pending
        """
        return self.__reminder_pending

    def get_reminder_pending_count(self) -> int:
        """
        Pending Reminder count
        """
        return self.__reminder_pending_count

    def get_site_list_count(self) -> int:
        """
        Returns No of sites added in fast access list
        """
        return self.__site_list_count

    def get_folder_list_count(self) -> int:
        """
        Returns No of folder added in fast access list
        """
        return self.__folder_list_count

    def get_proces_list_count(self) -> int:
        """
        Returns No of process/app added in fast access list
        """
        return self.__process_list_count

    def set_login_type(self, login_type: str) -> None:
        """
        Change login type to user or master(Shishere)
        """
        self.__login_type = login_type

    def set_reminder_pending_status(self, reminder_status: bool) -> None:
        """
        Change if reminder is pending or not
        True/False
        """
        self.__reminder_pending = reminder_status

    def set_reminder_pending_count(self, reminder_count: int) -> None:
        """
        Change pending Reminder Count
        """
        self.__reminder_pending_count = reminder_count

    def set_site_list_count(self, site_count: int) -> None:
        """
        Change no of sites in fast access count
        """
        self.__site_list_count = site_count

    def set_folder_list_count(self, folder_count: int) -> None:
        """
        Change no of folder in fast access count
        """
        self.__folder_list_count = folder_count

    def set_process_list_count(self, process_count: int) -> None:
        """
        Change no of process/app in fast access count
        """
        self.__process_list_count = process_count


class config:
    def __init__(
        self,
        show_curresponding_reminder: bool = True,
        start_up_reminder_check: bool = True,
        reminder_keywords: [str] = [],
        website_keywords: [str] = [],
        process_keywords: [str] = [],
        status_keywords: [str] = [],
        folder_keywords: [str] = [],
        configure_keywords: [str] = [],
        media_keywords: [str] = [],
    ) -> None:
        self.__show_curresponding_reminder = show_curresponding_reminder
        self.__start_up_reminder_check = start_up_reminder_check
        self.__reminder_keywords = self.__set_reminder_keyword(
            keywords=reminder_keywords
        )
        self.__folder_keywords = self.__set_folder_keyword(keywords=folder_keywords)
        self.__website_keywords = self.__set_website_keyword(keywords=website_keywords)
        self.__process_keywords = self.__set_process_keyword(keywords=process_keywords)
        self.__status_keywords = self.__set_status_keyword(keywords=status_keywords)
        self.__config_keywords = self.__set_config_keyword(keywords=configure_keywords)
        self.__media_keywords = self.__set_media_keyword(keywords=media_keywords)

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Show Currsesponding Reminder    :   {self.__show_curresponding_reminder}
        Startup Reminder Check          :   {self.__start_up_reminder_check}
        Reminder Keywords               :   {" , ".join(self.__reminder_keywords)}
        Folder Keywords                 :   {" , ".join(self.__folder_keywords)}
        Process Keywords                :   {" , ".join(self.__process_keywords)}
        Website Keywords                :   {" , ".join(self.__website_keywords)}
        Status Keywords                 :   {" , ".join(self.__status_keywords)}
        Configure Keywords              :   {" , ".join(self.__config_keywords)}
        Media Keywords                  :   {" , ".join(self.__media_keywords)}
        """

    def format(self) -> str:
        return self.__format__()

    def show(self) -> None:
        """
        Print data in special form
        """
        print(self.__format__())

    def to_dictionary(self) -> dict:
        """
        Return datatype in dictionary format
        """
        dic = {}
        dic["Show_Currsesponding_Reminder"] = self.__show_curresponding_reminder
        dic["start_up_reminder_check"] = self.__start_up_reminder_check
        dic["Reminder_Keywords"] = self.__reminder_keywords
        dic["Folder_Keywords"] = self.__folder_keywords
        dic["Process_Keywords"] = self.__process_keywords
        dic["Website_Keywords"] = self.__website_keywords
        dic["Status_Keywords"] = self.__status_keywords
        dic["configure_keywords"] = self.__config_keywords
        dic["media_keywords"] = self.__media_keywords
        return dic

    def get_status(self, status_of: str) -> bool:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_reminder_check(reminder check)
        """
        if status_of == "show reminder":
            return self.__show_curresponding_reminder
        elif status_of == "reminder check":
            return self.__start_up_reminder_check
        else:
            return False

    def __set_reminder_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "reminder" not in keywords:
            keywords.append("reminder")
        if "rem" not in keywords:
            keywords.app("rem")
        return keywords

    def __set_process_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "process" not in keywords:
            keywords.append("process")
        if "processlist" not in keywords:
            keywords.append("processlist")
        if "app" not in keywords:
            keywords.append("app")
        return keywords

    def __set_folder_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "folder" not in keywords:
            keywords.append("folder")
        if "folderlist" not in keywords:
            keywords.append("folderlist")
        return keywords

    def __set_website_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "website" not in keywords:
            keywords.append("website")
        if "site" not in keywords:
            keywords.append("site")
        if "sitelist" not in keywords:
            keywords.append("sitelist")
        return keywords

    def __set_status_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "status" not in keywords:
            keywords.append("status")
        return keywords

    def __set_config_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "config" not in keywords:
            keywords.append("config")
        if "configure" not in keywords:
            keywords.app("configure")
        return keywords

    def __set_media_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "media" not in keywords:
            keywords.append("media")
        if "med" not in keywords:
            keywords.append("med")
        return keywords

    def set_status(self, status_of: str, do_show: bool = True) -> bool:
        """
        Set status of Show_Currsesponding_Reminder(show reminder),
        start_up_reminder_check(reminder check)
        """
        if status_of == "show reminder":
            self.__show_curresponding_reminder = do_show
        elif status_of == "reminder check":
            self.__start_up_reminder_check = do_show
        else:
            return False
        return True

    def add_or_change_keywords(self, datatype: str, keyword_list: [str]) -> bool:
        """
        Add / delete /change keyword  for fast access
        """
        try:
            if datatype == "reminder":
                self.__reminder_keywords = keyword_list
            elif datatype == "folder":
                self.__folder_keywords = keyword_list
            elif datatype == "process":
                self.__process_keywords = keyword_list
            elif datatype == "status":
                self.__status_keywords = keyword_list
            elif datatype == "website":
                self.__website_keywords = keyword_list
            elif datatype == "configure":
                self.__config_keywords = keyword_list
            elif datatype == "media":
                self.__media_keywords = keyword_list
            else:
                raise Exception
            return True
        except Exception:
            return False

    def remove_keyword(self, datatype: str, keyword: str) -> bool:
        """
        remove keyword for fast access
        """
        try:
            if datatype == "reminder":
                if not datatype in self.__reminder_keywords:
                    raise Exception
                self.__reminder_keywords.remove(keyword)
            elif datatype == "folder":
                if not datatype in self.__folder_keywords:
                    raise Exception
                self.__folder_keywords.remove(keyword)
            elif datatype == "process":
                if not keyword in self.__process_keywords:
                    raise Exception
                self.__process_keywords.remove(keyword)
            elif datatype == "status":
                if not keyword in self.__status_keywords:
                    raise Exception
                self.__status_keywords.remove(keyword)
            elif datatype == "website":
                if not keyword in self.__website_keywords:
                    raise Exception
                self.__website_keywords.remove(keyword)
            elif datatype == "configure":
                self.__config_keywords.remove(keyword)
            elif datatype == "media":
                self.__media_keywords.remove(keyword)
            else:
                raise Exception
            return True
        except Exception:
            return False

    def show_keyword(self, datatype: str) -> bool:
        """
        show keywords saved for fast access
        """
        try:
            if datatype == "reminder":
                print(f"Keywords : {' , '.join(self.__reminder_keywords)}")
            elif datatype == "folder":
                print(f"Keywords : {' , '.join(self.__folder_keywords)}")
            elif datatype == "process":
                print(f"Keywords : {' , '.join(self.__process_keywords)}")
            elif datatype == "status":
                print(f"Keywords : {' , '.join(self.__status_keywords)}")
            elif datatype == "website":
                print(f"Keywords : {' , '.join(self.__website_keywords)}")
            elif datatype == "configure":
                print(f"Keywords : {' , '.join(self.__config_keywords)}")
            elif datatype == "media":
                print(f"Keywords : {' , '.join(self.__media_keywords)}")
            else:
                raise Exception
            return True
        except Exception:
            return False

    def get_keywords(self, datatype: str) -> [str]:
        """
        get the list of keywords or specified section
        """
        try:
            if datatype == "reminder":
                return self.__reminder_keywords
            elif datatype == "folder":
                return self.__folder_keywords
            elif datatype == "process":
                return self.__process_keywords
            elif datatype == "status":
                return self.__status_keywords
            elif datatype == "website":
                return self.__website_keywords
            elif datatype == "configure":
                return self.__config_keywords
            elif datatype == "media":
                return self.__media_keywords
            else:
                raise Exception
        except Exception:
            return []


class log:
    def __init__(self, user_input: str, section: str, date_time: datetime) -> None:
        self.__user_input = user_input
        self.__section = section
        self.__date_time = date_time

    def __str__(self) -> str:
        return f"{self.__date_time} : {self.__section} > {self.__user_input}"

    def to_string(self) -> str:
        return self.__str__()


class media:
    def __init__(
        self,
        new: bool = False,
        media_id: int = None,
        media_name: str = None,
        category: str = None,
        media_type: str = None,
        episodes: int = None,
        duration: int = None,
        added_date: datetime = None,
        rewatched: int = 0,
    ) -> None:
        self.__new: bool = new
        self.__media_id: int = media_id
        self.__media_name: str = media_name
        self.__category: str = category
        self.__media_type: str = media_type
        self.__episodes: int = episodes
        self.__duration: int = duration
        self.__added_date: datetime = self.__set_date(new=new, added_date=added_date)
        self.__rewatched: int = rewatched

    def __str__(self) -> str:
        return f"{{'ID':'{self.__media_id}', 'Name': '{self.__media_name}', 'Type': '{self.__media_type}', 'Added_on': '{self.__added_date}', 'category': '{self.__category}', 'Episodes': '{self.__episodes}', 'Duration': '{self.__duration}', 'Rewatched':'{self.__rewatched}''}}"

    def to_string(self) -> str:
        """
        Converet reminder to string
        """
        return self.__str__()

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Media ID        :   {self.__media_id}
        Category        :   {self.__category}
        Name            :   {self.__media_name}
        Type            :   {self.__media_type}
        Added On        :   {self.__added_date}     
        Episodes        :   {self.__episodes}
        Duration        :   {self.__duration}
        Rewatched       :   {self.__rewatched}
        """

    def to_list(self) -> list:
        """
        Return data in a list[name,type,category,episodes,duration,rewatched]
        """
        return [
            self.__media_id,
            self.__media_name,
            self.__media_type,
            self.__category,
            self.__episodes,
            self.__duration,
            self.__rewatched,
        ]

    def __set_date(self, new: bool, added_date: datetime) -> datetime:
        """
        Arrange date
        """
        if new:
            return self.__get_date_time()
        else:
            return added_date

    def __get_date_time(self) -> datetime:
        """
        return the current date
        """
        # get date time in 05-Mar-2020 02:01:30 PM format
        return datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")

    def to_dictionary(self) -> dict:
        """
        Convert reminder into dictionary datatype
        """
        dic = {}
        dic["media_id"] = self.__media_id
        dic["media_name"] = self.__media_name
        dic["type"] = self.__media_type
        dic["added_on"] = self.__added_date
        dic["category"] = self.__category
        dic["episodes"] = self.__episodes
        dic["duration"] = self.__duration
        dic["rewatched"] = self.__rewatched
        return dic

    def format(self) -> str:
        """
        Returns the reminder in specific format
        """
        return self.__format__()

    def show(self) -> None:
        """
        Prints the reminder in specific format
        """
        print(self.format())

    def get_id(self) -> int:
        """
        Returns the ID of the reminder
        """
        return int(self.__media_id)

    def get_name(self) -> str:
        return self.__media_name

    def set_name(self, name: str) -> None:
        self.__media_name = name

    def get_type(self) -> str:
        return self.__media_type

    def set_type(self, media_type: str) -> None:
        self.__media_type = media_type

    def get_category(self) -> str:
        return self.__category

    def set_category(self, category: str) -> None:
        self.__category = category

    def get_episodes(self) -> int:
        return int(self.__episodes)

    def set_episodes(self, episodes: int) -> None:
        self.__episodes = int(episodes)

    def get_duration(self) -> int:
        return int(self.__duration)

    def set_duration(self, duration: int) -> None:
        self.__duration = duration

    def get_added_date(self) -> str:
        return self.__added_date

    def get_rewatched(self) -> int:
        return self.__rewatched

    def set_rewatched(self, rewatched: int) -> None:
        self.__rewatched = rewatched


class convert:
    """
    convert data written into file as string data into its original form
    for these data types
        > reminder
        > process
        > folder
        > website
        > media
    """

    def __init__(self, file_data: []) -> None:
        self.data = file_data

    def to_reminder(self) -> reminder:
        """
        Converts and returns the data in Reminder datatype
        """
        try:
            return reminder(
                reminder_id=self.data["ID"],
                reminder_data=self.data["Data"],
                reminder_type=self.data["Type"],
                reminder_status=self.data["Status"],
                added_date=self.data["Added_on"],
                completed_date=self.data["Completed_on"],
            )
        except Exception as e:
            print(e)
            raise TypeError("Invalid Type Conversion")

    def to_process(self) -> process:
        """
        Converts and returns the data in Process datatype
        """
        try:
            return process(
                title=self.data["Title"],
                location=self.data["Location"],
                codes=self.data["codes"],
            )
        except Exception:
            raise TypeError("Invalid Type Conversion")

    def to_folder(self) -> folder:
        """
        Converts and returns the data in Folder datatype
        """
        try:
            return folder(
                title=self.data["Title"],
                location=self.data["Location"],
                codes=self.data["codes"],
            )
        except Exception:
            raise TypeError("Invalid Type Conversion")

    def to_website(self) -> website:
        """
        Converts and returns the data in Website datatype
        """
        try:
            return website(
                title=self.data["Title"],
                location=self.data["Location"],
                codes=self.data["codes"],
            )
        except Exception:
            raise TypeError("Invalid Type Conversion")

    def to_status(self) -> status:
        """
        Converts and returns the data in Status datatype
        """
        try:
            return status(
                login_type=self.data["login_type"],
                reminder_pending=self.data["reminder_pending"],
                reminder_pending_count=self.data["reminder_pending_count"],
                site_list_count=self.data["site_list"],
                folder_list_count=self.data["folder_list"],
                process_list_count=self.data["process_list"],
            )
        except Exception:
            raise TypeError("Invalid Type Conversion")

    def to_config(self) -> config:
        """
        Converts and returns the data in config datatype
        """
        try:
            return config(
                show_curresponding_reminder=self.data["Show_Currsesponding_Reminder"],
                start_up_reminder_check=self.data["start_up_reminder_check"],
                reminder_keywords=self.data["Reminder_Keywords"],
                folder_keywords=self.data["Folder_Keywords"],
                process_keywords=self.data["Process_Keywords"],
                website_keywords=self.data["Website_Keywords"],
                status_keywords=self.data["Status_Keywords"],
                configure_keywords=self.data["configure_keywords"],
                media_keywords=self.data["media_keywords"],
            )
        except Exception:
            # print(e)
            raise TypeError("Invalid Type Conversion")

    def to_media(self) -> media:
        """
        Converts and returns the data in media datatype
        """
        try:
            return media(
                media_id=self.data["media_id"],
                media_name=self.data["media_name"],
                media_type=self.data["type"],
                added_date=self.data["added_on"],
                category=self.data["category"],
                episodes=self.data["episodes"],
                duration=self.data["duration"],
                rewatched=self.data["rewatched"],
            )
        except Exception as e:
            print(e)
            # raise TypeError("Invalid Type Conversion")


if __name__ == "DataType":
    pass
