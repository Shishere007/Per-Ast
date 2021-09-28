"""
Creating datatypes which is to be used in CLI program
and converting string data types to its original datatype form
Defined Data types :
    > Process
    > Folder
    > Website
    > Reminder
    > Mail  
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

    def __format__(self, format_spec: str) -> str:
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


class mail:
    """ 
        mail Datatype. with mail ID, from and to address.
        And mail subject and body
    """

    def __init__(
        self,
        new: bool = False,
        mail_id: int = 0,
        from_address: str = None,
        password: str = None,
        to_address: str = None,
        mail_subject: str = None,
        mail_body: str = None,
        mail_status: str = "pending",
        remark: str = None,
        added_date: datetime = None,
        sent_date: datetime = None,
    ) -> None:
        self.__mail_id = mail_id
        self.__from_address = from_address
        self.__password = password
        self.__to_address = to_address
        self.__mail_subject = mail_subject
        self.__mail_body = mail_body
        self.__mail_status = mail_status
        self.__remark = remark
        self.__added_date = self.__set_date(new=new, added_date=added_date)
        self.__sent_date = sent_date

    def __str__(self) -> str:
        return f"{{'ID': '{self.__mail_id}', 'From': '{self.__from_address}', 'Password': '{self.__password}', 'To': '{self.__to_address}', 'Subject': '{self.__mail_subject}', 'Body': '{self.__mail_body}', 'Status': '{self.__mail_status}', 'Remark': '{self.__remark}', 'Added_date': '{self.__added_date}', 'Sent_date': '{self.__sent_date}'}}"

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Mail ID     :   {self.__mail_id}
        From        :   {self.__from_address}
        To          :   {self.__to_address}
        Subject     :   {self.__mail_subject}
        Body        :   {self.__mail_body}
        Mail Status :   {self.__mail_status}
        Remark      :   {self.__remark}
        Added Date  :   {self.__added_date}
        Sent Date   :   {self.__sent_date}
        """

    def format(self) -> str:
        """
        Retunrs the Mail data formatted in specific order
        """
        return self.__format__()

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
        Convert mail datatype into dictionary datatype
        """
        dic = {}
        dic["ID"] = self.__mail_id
        dic["From"] = self.__from_address
        dic["Password"] = self.__password
        dic["To"] = self.__to_address
        dic["Subject"] = self.__mail_subject
        dic["Body"] = self.__mail_body
        dic["Status"] = self.__mail_status
        dic["Remark"] = self.__remark
        dic["Added_date"] = self.__added_date
        dic["Sent_date"] = self.__sent_date
        return dic

    def to_string(self) -> str:
        """
        Converet reminder to string
        """
        return self.__str__()

    def show(self) -> None:
        """
        Prints the Mail data in specific order
        """
        print(self.format())

    def get_id(self) -> int:
        """
        Retunrs ID of mail
        """
        return int(self.__mail_id)

    def get_status(self) -> str:
        """
        Retunrs Status of mail
        """
        return self.__mail_status

    def get_from_address(self) -> str:
        """
        Return from address
        """
        return self.__from_address

    def get_password(self) -> str:
        """
        Return the password of the mail
        """
        return self.__password

    def get_to_address(self) -> str:
        """
        Return from address
        """
        return self.__to_address

    def get_subject(self) -> str:
        """
        Return the subject of the mail
        """
        return self.__mail_subject

    def get_body(self) -> str:
        """
        Return the body of the mail
        """
        return self.__mail_body

    def set_status(self, status: str = "completed") -> None:
        """
        set Status to 'Completed' by default
        or to the specified one
        """
        self.__mail_status = status
        self.__sent_date = self.__get_date_time()

    def is_completed(self) -> bool:
        """
        Returns True if mail status is 'completed', 
        False otherwise
        """
        return self.__mail_status == "completed"

    def clear_password(self) -> None:
        """
        erases the stored password
        """
        self.__password = None

    def set_remark(self, remark: str) -> None:
        """
        set additional notes on mail. like saving the reason incase of 
        failure 
        """
        self.__remark = remark

    def __get_date_time(self) -> datetime:
        """
        return the current date
        """
        # get date time in 05-Mar-2020 02:01:30 PM format
        return datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")


class status:
    """
    Status data type. Store basic details like login type,
    reminder and mail pending status, things like that
    """

    def __init__(
        self,
        login_type: str = None,
        reminder_pending: bool = False,
        reminder_pending_count: int = 0,
        mail_pending: bool = False,
        mail_pending_count: int = 0,
        site_list_count: int = 0,
        folder_list_count: int = 0,
        process_list_count: int = 0,
    ) -> None:
        self.__login_type = login_type
        self.__reminder_pending = reminder_pending
        self.__reminder_pending_count = reminder_pending_count
        self.__mail_pending = mail_pending
        self.__mail_pending_count = mail_pending_count
        self.__site_list_count = site_list_count
        self.__folder_list_count = folder_list_count
        self.__process_list_count = process_list_count

    def __str__(self) -> None:
        return f"{{'login_type': '{self.__login_type}', 'mail_pending': '{self.__mail_pending}', 'mail_pending_count': '{self.__mail_pending_count}', 'reminder_pending': '{self.__reminder_pending}', 'reminder_pending_count': '{self.__reminder_pending_count}', 'site_list': '{self.__site_list_count}', 'folder_list': '{self.__folder_list_count}', 'process_list': '{self.__process_list_count}'}}"

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
        Mail Pending            :   {self.__mail_pending}
        Mail Pending Count      :   {self.__mail_pending_count}
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
        dic["mail_pending"] = self.__mail_pending
        dic["mail_pending_count"] = self.__mail_pending_count
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

    def get_mail_pending_status(self) -> bool:
        """
        True : Mail Pending\n
        False : Mail not Pending
        """
        return self.__mail_pending

    def get_mail_pending_count(self) -> int:
        """
        Pending Mail count
        """
        return self.__mail_pending_count

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

    def set_mail_pending_status(self, mail_status: bool) -> None:
        """
        Change if mail is pending or not
        True/False
        """
        self.__mail_pending = mail_status

    def set_mail_pending_count(self, mail_count: int) -> None:
        """
        Change pending mail Count
        """
        self.__mail_pending_count = mail_count

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
        start_up_mail_check: bool = True,
        start_up_reminder_check: bool = True,
        reminder_keywords: [str] = [],
        website_keywords: [str] = [],
        process_keywords: [str] = [],
        status_keywords: [str] = [],
        mail_keywords: [str] = [],
        folder_keywords: [str] = [],
        configure_keywords: [str] = [],
    ) -> None:
        self.__show_curresponding_reminder = show_curresponding_reminder
        self.__start_up_mail_check = start_up_mail_check
        self.__start_up_reminder_check = start_up_reminder_check
        self.__reminder_keywords = self.__set_reminder_keyword(
            keywords=reminder_keywords
        )
        self.__mail_keywords = self.__set_mail_keyword(keywords=mail_keywords)
        self.__folder_keywords = self.__set_folder_keyword(keywords=folder_keywords)
        self.__website_keywords = self.__set_website_keyword(keywords=website_keywords)
        self.__process_keywords = self.__set_process_keyword(keywords=process_keywords)
        self.__status_keywords = self.__set_status_keyword(keywords=status_keywords)
        self.__config_keywords = self.__set_config_keyword(keywords=configure_keywords)

    def __format__(self, format_spec: str = None) -> str:
        return f"""
        Show Currsesponding Reminder    :   {self.__show_curresponding_reminder}
        Startup Mail check              :   {self.__start_up_mail_check}
        Startup Reminder Check          :   {self.__start_up_reminder_check}
        Reminder Keywords               :   {" , ".join(self.__reminder_keywords)}
        Folder Keywords                 :   {" , ".join(self.__folder_keywords)}
        Process Keywords                :   {" , ".join(self.__process_keywords)}
        Website Keywords                :   {" , ".join(self.__website_keywords)}
        Mail Keywords                   :   {" , ".join(self.__mail_keywords)}
        Status Keywords                 :   {" , ".join(self.__status_keywords)}
        Configure Keywords              :   {" , ".join(self.__config_keywords)}
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
        dic["start_up_mail_check"] = self.__start_up_mail_check
        dic["start_up_reminder_check"] = self.__start_up_reminder_check
        dic["Reminder_Keywords"] = self.__reminder_keywords
        dic["Folder_Keywords"] = self.__folder_keywords
        dic["Process_Keywords"] = self.__process_keywords
        dic["Website_Keywords"] = self.__website_keywords
        dic["Mail_Keywords"] = self.__mail_keywords
        dic["Status_Keywords"] = self.__status_keywords
        dic["configure_keywords"] = self.__config_keywords
        return dic

    def get_status(self, status_of: str) -> bool:
        """
        Get status of Show_Currsesponding_Reminder(show reminder),
        start_up_mail_check(mail check),start_up_reminder_check(reminder check)
        """
        if status_of == "show reminder":
            return self.__show_curresponding_reminder
        elif status_of == "mail check":
            return self.__start_up_mail_check
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
        if "websitelist" not in keywords:
            keywords.append("websitelist")
        return keywords

    def __set_mail_keyword(self, keywords: [str]) -> [str]:
        """
        Making sure default keywords are present, 
        adding if not
        """
        if "mail" not in keywords:
            keywords.append("mail")
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

    def set_status(self, status_of: str, do_show: bool = True) -> bool:
        """
        Set status of Show_Currsesponding_Reminder(show reminder),
        start_up_mail_check(mail check),start_up_reminder_check(reminder check)
        """
        if status_of == "show reminder":
            self.__show_curresponding_reminder = do_show
        elif status_of == "mail check":
            self.__start_up_mail_check = do_show
        elif status_of == "reminder check":
            self.__start_up_reminder_check = do_show
        else:
            return False
        return True

    def add_keyword(self, datatype: str, keyword: str) -> bool:
        """
        Add new keyword for fast access
        """
        try:
            if datatype == "reminder":
                self.__reminder_keywords.append(keyword)
            elif datatype == "folder":
                self.__folder_keywords.append(keyword)
            elif datatype == "process":
                self.__process_keywords.append(keyword)
            elif datatype == "status":
                self.__status_keywords.append(keyword)
            elif datatype == "mail":
                self.__mail_keywords.append(keyword)
            elif datatype == "website":
                self.__website_keywords.append(keyword)
            elif datatype == "configure":
                self.__config_keywords.append(keyword)
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
            elif datatype == "mail":
                if not keyword in self.__mail_keywords:
                    raise Exception
                self.__mail_keywords.remove(keyword)
            elif datatype == "website":
                if not keyword in self.__website_keywords:
                    raise Exception
                self.__website_keywordss.remove(keyword)
            elif datatype == "configure":
                self.__config_keywords.remove(keyword)
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
            elif datatype == "mail":
                print(f"Keywords : {' , '.join(self.__mail_keywords)}")
            elif datatype == "website":
                print(f"Keywords : {' , '.join(self.__website_keywords)}")
            elif datatype == "configure":
                print(f"Keywords : {' , '.join(self.__config_keywords)}")
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
            elif datatype == "mail":
                return self.__mail_keywords
            elif datatype == "website":
                return self.__website_keywords
            elif datatype == "configure":
                return self.__config_keywords
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


class convert:
    """
    convert data written into file as string data into its original form
    for these data types
        > reminder
        > mail
        > process
        > folder
        > website
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

    def to_mail(self) -> mail:
        """
        Converts and returns the data in Mail datatype
        """
        try:
            return mail(
                mail_id=self.data["ID"],
                from_address=self.data["From"],
                to_address=self.data["To"],
                mail_subject=self.data["Subject"],
                mail_body=self.data["Body"],
                mail_status=self.data["Status"],
                added_date=self.data["Added_date"],
                sent_date=self.data["Sent_date"],
                remark=self.data["Remark"],
                password=self.data["Password"],
            )
        except Exception:
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
                mail_pending=self.data["mail_pending"],
                mail_pending_count=self.data["mail_pending_count"],
                reminder_pending=self.data["reminder_pending"],
                reminder_pending_count=self.data["reminder_pending_count"],
                site_list_count=self.data["site_list"],
                folder_list_count=self.data["folder_list"],
                process_list_count=self.data["process_list"],
            )
        except Exception as e:
            raise TypeError("Invalid Type Conversion")

    def to_config(self) -> config:
        """
        Converts and returns the data in config datatype
        """
        try:
            return config(
                show_curresponding_reminder=self.data["Show_Currsesponding_Reminder"],
                start_up_mail_check=self.data["start_up_mail_check"],
                start_up_reminder_check=self.data["start_up_reminder_check"],
                reminder_keywords=self.data["Reminder_Keywords"],
                folder_keywords=self.data["Folder_Keywords"],
                process_keywords=self.data["Process_Keywords"],
                website_keywords=self.data["Website_Keywords"],
                mail_keywords=self.data["Mail_Keywords"],
                status_keywords=self.data["Status_Keywords"],
                configure_keywords=self.data["configure_keywords"],
            )
        except Exception as e:
            # print(e)
            raise TypeError("Invalid Type Conversion")
    
    


if __name__ == "DataType":
    pass
