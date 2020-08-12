# Files
## Python Files
    basic_commands.py
    browser_section.py
    configure.py
    create_blueprint.py
    data_types.py
    encryption.py
    file_operation.py
    Folder_fast_access.py
    gui_section.py
    media_section.py
    operations.py
    process_fast_access.py
    Reminder_section.py
    run.py
    website_fast_access.py


## Data Files
    categorys.json
    completed_reminder_data.json
    configure.json
    folder_data.json
    log.json
    mail_data.json
    media_data.json
    process_data.json
    reminder_data.json
    status.json



# Class and Functions
## basic_commands.py


    class basic_commands
        def __init__(self) -> None
        def __get_file_and_path(self, location: str) -> [str]
            def __list_all_item_at_loc(location: str) -> [str]
        def __open(self, user_input: str) -> None
        def __kill(self, user_input: str) -> None
                def running_process_list() -> [str]
                def kill_all(process_name: str) -> None
        def __help(self) -> None
        def __show(self, user_input: str) -> None
        def __setpath(self, user_input: str) -> None
        def __currentPath(self) -> None
        def __select_directory(self, folder_name: str) -> None
        def __clear(self, user_input: str) -> None
        def __add_or_new(self, user_input: str) -> None
        def __delete(self, user_input: str) -> None
        def __complete(self, user_input: str) -> None
        def __show_log(self) -> None
        def user_section(self, user_input: str) -> bool
            def length(user_input: str) -> bool


## browser_section.py


    class browser_section(website_fast_access)
        def __init__(self) -> None
        def __get_site(self, site_code: str) -> str
        def __google_search(self, query: str) -> str
        def __open_in_browser(self, web_site: str) -> None
        def __open_website(self, user_input: str) -> None
        def user_section(self, user_input: str) -> None


## configure.py


    class configure
        def __init__(self) -> None
        def show(self) -> None
        def __get_current_config(self) -> config
        def __update_config(self, new_config: config) -> None
        def __add_keyword_read_data(self, user_input: str) -> None
        def get_keywords(self, data_type: str) -> [str]
        def get_status(self, status_of: str) -> bool
        def __set_status(self, status_of: str, do_show: bool) -> None
        def __help(self) -> None
        def user_section(self) -> bool


## create_blueprint.py

    def create_file() -> None
    def write(lines: [str]) -> None
        def remove(string: str) -> str
                    def rem(string: str) -> str
    def write_methodes() -> None
    def get_py_files() -> list
    def write_files() -> None


## data_types.py


    class base_class
        def __init__(self, title: str, location: str, codes: [str]) -> None
        def __str__(self) -> str
        def __format__(self, format_spec: str = None) -> str
        def format(self) -> str
        def to_dictionary(self) -> dict
        def get_title(self) -> str
        def get_codes(self) -> [str]
        def get_location(self) -> str
        def is_same(self, location: str) -> bool

    class process(base_class)
        def __init__(self, title: str, location: str, codes: [str]) -> None
        def __format__(self, format_spec: str = "Process") -> str
        def show(self) -> None
        def get_exe_name(self) -> str

    class folder(base_class)
        def __init__(self, title: str, location: str, codes: [str]) -> None
        def __format__(self, format_spec: str = "Folder") -> str
        def show(self) -> None

    class website(base_class)
        def __init__(self, title: str, location: str, codes: [str]) -> None
        def __format__(self, format_spec: str = "Website")
        def show(self) -> None

    class reminder
        def __init__(self, new: bool = False, reminder_id: int = None, reminder_data: str = None, reminder_type: str = None, reminder_status: str = "pending", added_date: datetime = None, completed_date: datetime = None, ) -> None
        def __str__(self) -> str
        def to_string(self) -> str
        def __format__(self, format_spec: str = None) -> str
        def __set_date(self, new: bool, added_date: datetime) -> datetime
        def to_dictionary(self) -> dict
        def format(self) -> str
        def show(self) -> None
        def get_id(self) -> int
        def get_type(self) -> str
        def get_status(self) -> str
        def set_status(self, status: str = "completed") -> None
        def is_completed(self) -> bool
        def __get_date_time(self)

    class status
        def __init__(self, login_type: str = None, reminder_pending: bool = False, reminder_pending_count: int = 0, site_list_count: int = 0, folder_list_count: int = 0, process_list_count: int = 0, ) -> None
        def __str__(self) -> None
        def to_string(self) -> str
        def __format__(self, format_spec: str = None) -> str
        def format(self) -> str
        def show(self) -> None
        def to_dictionary(self) -> dict
        def get_login_type(self) -> str
        def get_reminder_pending_status(self) -> bool
        def get_reminder_pending_count(self) -> int
        def get_site_list_count(self) -> int
        def get_folder_list_count(self) -> int
        def get_proces_list_count(self) -> int
        def set_login_type(self, login_type: str) -> None
        def set_reminder_pending_status(self, reminder_status: bool) -> None
        def set_reminder_pending_count(self, reminder_count: int) -> None
        def set_site_list_count(self, site_count: int) -> None
        def set_folder_list_count(self, folder_count: int) -> None
        def set_process_list_count(self, process_count: int) -> None

    class config
        def __init__(self, show_curresponding_reminder: bool = True, start_up_reminder_check: bool = True, reminder_keywords: [str] = [], website_keywords: [str] = [], process_keywords: [str] = [], status_keywords: [str] = [], folder_keywords: [str] = [], configure_keywords: [str] = [], media_keywords: [str] = [], ) -> None
        def __format__(self, format_spec: str = None) -> str
        def format(self) -> str
        def show(self) -> None
        def to_dictionary(self) -> dict
        def get_status(self, status_of: str) -> bool
        def __set_reminder_keyword(self, keywords: [str]) -> [str]
        def __set_process_keyword(self, keywords: [str]) -> [str]
        def __set_folder_keyword(self, keywords: [str]) -> [str]
        def __set_website_keyword(self, keywords: [str]) -> [str]
        def __set_status_keyword(self, keywords: [str]) -> [str]
        def __set_config_keyword(self, keywords: [str]) -> [str]
        def __set_media_keyword(self, keywords: [str]) -> [str]
        def set_status(self, status_of: str, do_show: bool = True) -> bool
        def add_keyword(self, datatype: str, keyword: str) -> bool
        def remove_keyword(self, datatype: str, keyword: str) -> bool
        def show_keyword(self, datatype: str) -> bool
        def get_keywords(self, datatype: str) -> [str]

    class log
        def __init__(self, user_input: str, section: str, date_time: datetime) -> None
        def __str__(self) -> str
        def to_string(self) -> str

    class media
        def __init__(self, new: bool = False, media_id: int = None, media_name: str = None, category: str = None, media_type: str = None, episodes: int = None, duration: int = None, added_date: datetime = None, rewatched: int = 0, ) -> None
        def __str__(self) -> str
        def to_string(self) -> str
        def __format__(self, format_spec: str = None) -> str
        def __set_date(self, new: bool, added_date: datetime) -> datetime
        def __get_date_time(self) -> datetime
        def to_dictionary(self) -> dict
        def format(self) -> str
        def show(self) -> None
        def get_id(self) -> int
        def get_name(self) -> str
        def get_type(self) -> str
        def get_category(self) -> str
        def get_episodes(self) -> int
        def get_duration(self) -> int
        def get_added_date(self) -> str
        def get_rewatched(self) -> int

    class convert
        def __init__(self, file_data: []) -> None
        def to_reminder(self) -> reminder
        def to_process(self) -> process
        def to_folder(self) -> folder
        def to_website(self) -> website
        def to_status(self) -> status
        def to_config(self) -> config
        def to_media(self) -> media


## encryption.py


    class encryption
        def __init__(self) -> None
        def __get_encryption_code(self) -> dict
        def encode(self, data: str) -> str
        def decode(self, data: str) -> str


## file_operation.py


    class File
        def __init__(self, file_location: str) -> None
        def __create_file(self, file_location: str) -> None
        def read_data(self) -> list
        def append_one_data(self, data_to_append: str) -> bool
        def append_one_data_string(self, data_to_append: str) -> bool
        def delete_one_data(self, file_data: list, data_to_delete: str) -> bool
        def rewrite_entire_data(self, file_data: list) -> bool
        def empty_file(self) -> bool
        def is_empty(self) -> bool
        def line_count(self) -> int
        def add_list_of_data(self, data_list: list) -> None


## Folder_fast_access.py


    class folder_fast_access(change_status)
        def __init__(self) -> None
        def add_folder(self) -> None
        def __read_data_for_new_folder(self) -> None
        def get_folder_list(self) -> [folder]
        def __add_new_folder(self, new_folder: str) -> None
        def delete_folder(self, user_input: str) -> None
        def __delete_folder_read_data(self, user_input: str) -> None
        def __delete_folder(self, folder_code: str) -> None
        def show_folder_list(self) -> None
        def folder_help(self) -> None
        def __change_folder_status(self) -> None
        def user_section(self) -> bool


## gui_section.py


    class add_media_gui
        def __init__(self) -> None
        def __clear_field(self) -> None
        def __submit_data(self) -> None
        def __add_duration(self)
        def __set_episode_count(self)


## media_section.py


    class media_section
        def __init__(self) -> None
        def add_media(self) -> None
        def get_category_list(self) -> list
        def get_new_media_id(self) -> int
        def new_media(self, new_media: media) -> None
        def show_media_list(self, category: str) -> None
        def show_media_status(self) -> None
        def show_category(self) -> None
        def __is_duplicate(self, new_media: media) -> bool
        def __add_category(self) -> None
        def help(self) -> None
        def user_section(self) -> bool

    class add_media_gui
        def __init__(self) -> None
        def __clear_field(self) -> None
        def __submit_data(self) -> None
        def __add_duration(self)
        def __set_episode_count(self)


## operations.py

    def write_log(data_list: list) -> None
    def is_input_kill(data: str) -> bool
    def clear_screen() -> None
    def clear_clip() -> None
    def print_list_items(file_list: list) -> None
    def remove_char_from_string(string: str, character: str) -> str
    def add_character(string: str, character_1: str, character_2: str) -> str
    def complete_website(site: str) -> str
    def is_null_string(string: str) -> bool
    def is_connected() -> bool
    def internet_connection() -> None
    def get_date_time() -> datetime
    def show_date_time() -> None
    def get_date() -> date
    def is_a_website(site: str) -> bool
    def minutes_to_day_hour_min(time: int)
    def get_duration_of_movie(movie_name: str, movie_category: str) -> int

    class duplicate
        def __init__(self, data_list: list, data_type: str) -> None
        def get_converted_list(self) -> list
        def string_to_folder(self, data_list: list) -> [folder]
        def string_to_website(self, data_list: list) -> [website]
        def string_to_process(self, data_list: list) -> [process]
        def string_to_reminder(self, data_list: list) -> [reminder]
        def string_to_media(self, data_list: list) -> [media]
        def __convert(self, data_type, data_list: list) -> []
        def is_keyword_exist(self, keyword_list: list) -> bool
        def is_file_exists(self, location: str) -> bool

    class change_status
        def __init__(self) -> None
        def __get_status(self) -> status
        def __write_status_to_file(self, current_status: status) -> None
        def show_status(self) -> None


## process_fast_access.py


    class process_fast_access(change_status)
        def __init__(self) -> None
        def add_process(self) -> None
        def __read_data_for_new_process(self) -> None
        def __add_new_process(self, new_process: process) -> None
        def delete_process(self, user_input: str) -> None
        def __delete_process_read_data(self, keycode: str) -> None
        def __delete_process(self, keycode: str) -> None
        def run_process(self, keycode: str) -> bool
        def show_process_list(self) -> None
        def __process_help(self) -> None
        def __change_process_status(self) -> None
        def get_process_list(self) -> [process]
        def user_section(self) -> bool


## Reminder_section.py


    class reminder_section(change_status)
        def __init__(self) -> None
        def add_reminder(self) -> None
        def __add_reminder_read_data(self) -> None
        def auto_reminder(self, reminder_data: str, reminder_type: str) -> None
        def __sort_reminder_list(self, reminder_list=[str]) -> [reminder]
        def __add_reminder(self, reminder_data: str, reminder_type: str) -> bool
        def __delete_all_reminder(self) -> None
        def show_reminder(self) -> None
        def __show_reminders(self, user_input: str) -> None
            def show(reminder_list: [], do_convert: bool = False) -> None
        def __get_reminder_id(self, user_input: str) -> bool
        def complete_reminder(self, user_input: str) -> None
        def __task_completed_read_data(self, user_input: str) -> None
        def __complete_task(self, reminder_id: int) -> None
        def delete_reminder(self, user_input: str) -> None
        def __delete_task_read_data(self, user_input: str) -> None
        def __delete_task(self, reminder_id: int) -> None
                def find(reminder_list: [reminder]) -> int
        def show_curresponding_reminder(self, reminder_type: str) -> None
        def __pending_task_count(self) -> int
        def __change_reminder_status(self) -> None
        def __is_pending_task_present(self) -> bool
        def __help(self) -> None
        def startup_reminder_check(self) -> None
        def user_section(self) -> bool


## run.py


    class run
        def __init__(self) -> None
        def start(self) -> None
        def __start_up_check(self) -> None
        def __main_function(self) -> None


## website_fast_access.py


    class website_fast_access(change_status)
        def __init__(self) -> None
        def add_website(self) -> None
        def __read_data_for_new_website(self) -> None
        def __add_new_website(self, new_website: website) -> bool
        def delete_website(self, user_input: str) -> None
        def __delete_website_read_data(self, user_input: str) -> None
        def __delete_website(self, website_code: str) -> None
        def show_website_list(self) -> None
        def website_help(self) -> None
        def __change_website_status(self) -> None
        def user_section(self) -> bool


