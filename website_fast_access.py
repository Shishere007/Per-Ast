from pathlib import Path

from data_types import convert, log, website
from file_operation import File
from operations import (
    change_status,
    clear_screen,
    complete_website,
    duplicate,
    get_date_time,
    is_a_website,
    is_input_kill,
    write_log,
)

__name__ = "__website_fast_access__"


class website_fast_access(change_status):
    """
    Save website for fast access with keyword
    """

    def __init__(self) -> None:
        super().__init__()
        self.__website_data_path = "Data/website_data.json"
        self.__website_file = File(file_location=self.__website_data_path)

    def add_website(self) -> None:
        """
        To add website from main section
        """
        self.__read_data_for_new_website()

    def __read_data_for_new_website(self) -> None:
        """
        Read data for adding new website
        """
        try:
            self.__dupe = duplicate(
                data_list=self.__website_file.read_data(), data_type="website"
            )
            website_name = input("website Name : ")
            if is_input_kill(data=website_name):
                return
            site = input("website Location(Full) : ")
            if is_input_kill(data=site):
                return
            if not is_a_website(site=site):
                print("Doesnt seems to be valid website")
                return
            # completes the website by adding 'www' and 'https://'
            site = complete_website(site=site)
            # check if the location is alraedy in list
            if self.__dupe.is_file_exists(location=site):
                print("website is already in list")
                return
            print("Type the keywords for faster access seperated buy comma")
            website_codes = input("website codes : ").split(",")
            if self.__dupe.is_keyword_exist(keyword_list=website_codes):
                print("one of the keyword is already in use")
                return
            new_website = website(
                title=website_name, location=site, codes=website_codes
            )
            if not self.__add_new_website(new_website=new_website):
                print("Unable to add new website")
        except Exception as e:
            print(f"website_fast_access > __read_data_for_new_website- {e}")

    def __add_new_website(self, new_website: website) -> bool:
        """
        Add new website for access
        """
        try:
            if not self.__website_file.append_one_data(data_to_append=new_website):
                return False
            print("New website is added Successfully ")
            self.__change_website_status()
            return True
        except Exception as e:
            print(f"website_fast_access > __add_new_website- {e}")
        return False

    def delete_website(self, user_input: str) -> None:
        """
        To delete a website as completed from main section
        """
        self.__delete_website_read_data(user_input=user_input)

    def __delete_website_read_data(self, user_input: str) -> None:
        """
        Delete a website from list
        """
        try:
            if len(user_input.split()) > 1:
                website_code = " ".join(user_input.split()[1:])
            else:
                website_code = input("website code : ")
            if website_code.isalpha():
                self.__delete_website(website_code=website_code)
            else:
                print("incorrent input")
        except Exception as e:
            print(f"website_fast_access > __delete_website_read_data- {e}")

    def __delete_website(self, website_code: str) -> None:
        try:
            website_list = self.__website_file.read_data()
            for item in website_list:
                if website_code in convert(file_data=item).to_website().get_codes():
                    self.__website_file.delete_one_data(
                        file_data=website_list, data_to_delete=item
                    )
                    self.__change_website_status()
                    print("website deleted from list")
                    return
            else:
                print(f" No website found with '{website_code}' keyword'")
        except Exception as e:
            print(f"website_fast_access > __delete_website- {e}")

    def show_website_list(self) -> None:
        """
        Show all the fast access website list
        """
        try:
            website_list = self.__website_file.read_data()
            if len(website_list) == 0:
                print("list is empty")
                return
            for item in website_list:
                convert(file_data=item).to_website().show()
        except Exception as e:
            print(f"website_fast_access > show_website_list- {e}")

    def website_help(self) -> None:
        """
        Website command list
        """
        print(
            """
            Command list
            -> add/new      add new website to fast access list
            -> del/delete   remove website from list
            -> show         List all website list          
        """
        )

    def __change_website_status(self) -> None:
        """
        change no of website count status data
        """
        try:
            current_status = self._change_status__get_status()
            current_status.set_site_list_count(
                site_count=self.__website_file.line_count()
            )
            self._change_status__write_status_to_file(current_status=current_status)
        except Exception as e:
            print(f"website_fast_access > __change_website_status- {e}")

    def user_section(self) -> bool:
        """
        User section for adding removing website's from list
        """
        try:
            input_list = []
            print("Type break/stop to exit section")
            while True:
                user_input = str(input(">>>"))
                input_list.append(
                    log(
                        user_input=user_input,
                        section="website",
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
                    self.__read_data_for_new_website()
                elif user_input.split()[0] in ["del", "delete"]:
                    self.__delete_website_read_data(user_input=user_input)
                elif user_input in ["help"]:
                    self.website_help()
                elif user_input in ["show"]:
                    self.show_website_list()
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
            print(f"website_fast_access > user_section - {e}")
        finally:
            write_log(data_list=input_list)


if __name__ == "__website_fast_access__":
    pass
