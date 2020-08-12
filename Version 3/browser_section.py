import webbrowser

from website_fast_access import website_fast_access
from data_types import convert
from operations import add_character, is_connected, remove_char_from_string
from Reminder_section import reminder_section

__name__ = "__browser__"


class browser_section(website_fast_access):
    def __init__(self) -> None:
        super().__init__()

    def __get_site(self, site_code: str) -> str:
        """
        return site if site_code exists, false otherwise
        """
        for item in self._website_fast_access__website_file.read_data():
            site = convert(file_data=item).to_website()
            if site_code in site.get_codes():
                print(f"Opening {site.get_location()}")
                return site.get_location()
        else:
            return False

    def __google_search(self, query: str) -> str:
        """
        make query google search query
        """
        try:
            print("Searching in google")
            return f"https://www.google.com/search?q={query}"
        except Exception:
            print("error")

    def __open_in_browser(self, web_site: str) -> None:
        """
        open website in default browser
        """
        try:
            webbrowser.open(web_site)
        except Exception as e:
            print(f"operation > __open_in_browser - {e}")

    def __open_website(self, user_input: str) -> None:
        """
        pre saved websites,
        modify the code and join it with webiste list
        """
        try:
            user_input_list = user_input.split()
            keyword = " ".join(user_input_list[1:])
            if len(user_input_list) < 4:
                site = self.__get_site(site_code=keyword)
            else:
                site = False
            if not site:
                input_length = len(user_input_list)
                keyword = user_input_list[1]
                if keyword.__contains__("git"):
                    site = "https://github.com/Shishere007"
                    if input_length > 2:
                        site = f"https://github.com/{user_input_list[2]}"
                elif keyword in ["youtube", "yt"]:
                    site = "https://www.youtube.com/"
                    if input_length > 2:
                        search_item = "+".join(user_input_list[2:])
                        site = f"https://www.youtube.com/results?search_query={search_item}"
                elif keyword == "steam":
                    site = "https://store.steampowered.com/"
                    if input_length > 2:
                        search_item = "+".join(user_input_list[2:])
                        site = (
                            f"https://store.steampowered.com/search/?term={search_item}"
                        )
                elif keyword in ["flipkart", "flip"]:
                    if input_length > 2:
                        query = "+".join(user_input_list[2:])
                        site = f"https://www.flipkart.com/search?q={query}"
                    else:
                        site = "https://www.flipkart.com"
                elif keyword in ["amazon"]:
                    if input_length > 2:
                        query = "+".join(user_input_list[2:])
                        site = f"https://www.amazon.in/s?k={query}"
                    else:
                        site = "https://www.amazon.in"
                else:
                    # add a verification question , if find it needed in future
                    query = "+".join(user_input_list[1:])
                    site = self.__google_search(query=query)
            self.__open_in_browser(web_site=site)
        except Exception as e:
            print(f"browser_section > __open_website - {e}")

    def user_section(self, user_input: str) -> None:
        try:
            user_input_list = user_input.split()
            input_length = len(user_input_list)
            if len(set((user_input_list[0]))) != 1:
                if remove_char_from_string(string=user_input,character="!") == "":
                    return False
                user_input = add_character(
                    string=user_input, character_1="!", character_2=" "
                )
                input_length += 1
            if input_length > 1:
                if is_connected():
                    reminder_section().show_curresponding_reminder("firefox")
                    self.__open_website(user_input=user_input)
                else:
                    print("Internet connection is not available")
        except Exception as e:
            print(f"browser_section > user_section - {e}")
    