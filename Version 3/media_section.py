from ast import literal_eval
from os import startfile
from tkinter import END, Button, Entry, Label, StringVar, Tk, mainloop, ttk

from data_types import convert, log, media
from file_operation import File
from operations import (
    clear_screen,
    duplicate,
    get_date_time,
    get_duration_of_movie,
    minutes_to_day_hour_min,
    write_log,
)

# import gui_section_intermediate

# from add_media_gui import add_media_gui

__name__ = "__media__"


class media_section:
    def __init__(self) -> None:
        self.__media_data_file_path = "Data/media_data.json"
        self.__media_data_file = File(file_location=self.__media_data_file_path)
        self.__category_file_path: str = "Data/categorys.json"
        self.__category_file: File = File(file_location=self.__category_file_path)

    def get_category_list(self) -> list:
        """
        Get the list of category
        """
        return self.__category_file.read_data()

    def get_new_media_id(self) -> int:
        """
        Get the  id for the new media
        """
        media_data = self.__media_data_file.read_data()
        if len(media_data) == 0:
            media_id = 1
        else:
            __last_media = convert(file_data=media_data[-1]).to_media()
            media_id = __last_media.get_id() + 1
        return media_id

    def binary_search(self, data_list: [media], media_id: int) -> int:
        """
        Return the index of required data in the list.\n
        Returns -1, if not found
        """
        lower_limit, higher_limit = 0, len(data_list) - 1
        while lower_limit <= higher_limit:
            middle = (lower_limit + higher_limit) // 2
            if data_list[middle].get_id() == media_id:
                return middle

            if data_list[middle].get_id() > media_id:
                higher_limit = middle - 1

            elif data_list[middle].get_id() < media_id:
                lower_limit = middle + 1
        return -1

    def rewrite_entire_media_data(self, data_to_rewrite: [media]) -> bool:
        """
        to rewite all media data When a edit is made
        """
        if self.__media_data_file.rewrite_entire_data(
            file_data=sorted(data_to_rewrite, key=lambda med: med.get_id())
        ):
            return True
        return False

    def new_media(self, new_media: media) -> None:
        '''
        Add new media
        '''
        if not self.__is_duplicate(new_media=new_media):
            self.__media_data_file.append_one_data(data_to_append=new_media)
            print("New media added")
        else:
            print("Provided item already exists")

    def show_media_list(self, user_input: str) -> None:
        try:
            category = user_input.split()[1].capitalize()
            if category.__contains__("Gui"):
                raise Exception
        except Exception:
            category = "All"
        if category not in self.get_category_list() + ["All"]:
            print("Incorrect Category")
            return
        if user_input.lower().__contains__("gui"):
            show_media_table_gui(media_category=category)
            return
        none_exists: bool = True
        media_list = self.get_media_list()
        if category == "All":
            for item in media_list:
                convert(file_data=item).to_media().show()
                # print(convert(file_data=item).to_media())
            return
        for item in media_list:
            converted_item: media = convert(file_data=item).to_media()
            if category == converted_item.get_category():
                none_exists = False
                converted_item.show()
        if none_exists:
            print("No media found in the given category")

    def get_media_list(self) -> list:
        """
        Get all list of all saved media
        """
        return self.__media_data_file.read_data()

    def show_media_status(self) -> None:
        """
        List the media data status.

        """
        print("please wait, might take some time")
        media_list = self.get_media_list()
        media_list = duplicate(
            data_list=media_list, data_type="media"
        ).get_converted_list()
        media_count_dic = {}
        episode_count = {}
        total_time = {}
        total_rewatch = {}
        for item in media_list:
            if not item.get_category() in media_count_dic:
                media_count_dic[item.get_category()] = {"Series": 0, "Movie": 0}
                total_time[item.get_category()] = {"Series": 0, "Movie": 0}
                episode_count[item.get_category()] = 0
                total_rewatch[item.get_category()] = 0
                # media_count_dic[item.get_category()] += 1
            media_count_dic[item.get_category()][item.get_type()] += 1
            total_rewatch[item.get_category()] += item.get_rewatched()
            __show_duration = item.get_episodes() * item.get_duration()
            total_time[item.get_category()][item.get_type()] += (__show_duration) + (
                item.get_rewatched() * __show_duration
            )
            episode_count[item.get_category()] += item.get_episodes()
            # for item in media_count_dic.values():

        print(
            f"""
            ####################################################
                    {len(self.get_category_list())} categories
                    {sum([item["Series"] for item in media_count_dic.values()])} Series
                    {sum([item["Movie"] for item in media_count_dic.values()])} Movies
                TOTAL OF
                    {sum([item["Series"] for item in media_count_dic.values()])+sum([item["Movie"] for item in media_count_dic.values()])} Shows
                    {sum(episode_count.values())} Episodes
                    {sum(total_rewatch.values())} Rewatches
                    {minutes_to_day_hour_min(sum([item["Series"] for item in total_time.values()])+sum([item["Movie"] for item in total_time.values()]))}
            ####################################################         
        """
        )
        for item in media_count_dic:
            print(
                f"""
                > {item.upper()}:-
                    Series:        
                        {media_count_dic[item]["Series"]} Shows
                        {minutes_to_day_hour_min(total_time[item]["Series"])}
                    Movie:
                        {media_count_dic[item]["Movie"]} Shows
                        {minutes_to_day_hour_min(total_time[item]["Movie"])}
                    Total:
                        {media_count_dic[item]["Series"]+media_count_dic[item]["Movie"]} Shows
                        {episode_count[item]} Episodes
                        {total_rewatch[item]} Rewatches
                        {minutes_to_day_hour_min(total_time[item]["Series"] + total_time[item]["Movie"])}
            ####################################################
            """
            )

    def show_category(self) -> None:
        print("<<CATEGORY>>")
        for item in self.get_category_list():
            print(item)

    def __is_duplicate(self, new_media: media) -> bool:
        """
        Check if the provided media already and return true or false
        """
        media_data = self.__media_data_file.read_data()
        for item in media_data:
            converted_item = convert(file_data=item).to_media()
            if (
                new_media.get_name().lower() == converted_item.get_name().lower()
                and new_media.get_category() == converted_item.get_category()
            ):
                return True
        else:
            return False

    def __add_category(self) -> None:
        """
        Add new category
        """
        category = str(input("Category : "))
        self.__category_file.append_one_data_string(data_to_append=category)
        print("New Category added")

    def help(self) -> None:
        print(
            """
            add/new                 :   Add new media
            add/new cat/category    :   Add new category
            status                  :   Show media status
            show [category]         :   show media in specified category
            show all                :   show all media
            show status             :   show media status
            clear                   :   clear screen
            quit/exit               :   exit program
            cat/category            :   show category list

        """
        )

    def user_section(self) -> bool:
        """
        reminder section, reading options from user
        reads choice and does the corresponding tasks
        """
        print(
            "use break or stop to quit reminder/task section.\nUse help to get command list"
        )
        while True:
            try:
                input_list = []
                user_input = input(">>> ")
                input_list.append(
                    log(
                        user_input=user_input,
                        section="media",
                        date_time=get_date_time(),
                    )
                )
                user_input_list = user_input.split()
                if (
                    len(set(user_input)) == 0
                    or len(set(user_input)) == 1
                    and not user_input.isalnum()
                ):
                    continue
                elif user_input == "help":
                    self.help()
                elif user_input_list[0] in ["add", "new"]:
                    if len(user_input_list) == 1:
                        add_media_gui()
                    elif user_input_list[1] in ["cat", "category"]:
                        self.__add_category()
                    else:
                        print("incorrect keyword")
                elif user_input == "status":
                    self.show_media_status()
                elif user_input_list[0] == "show":
                    if len(user_input_list) == 1:
                        continue
                    elif user_input_list[1] == "status":
                        self.show_media_status()
                    elif user_input_list[1] in ["category", "cat"]:
                        self.show_category()
                    else:
                        self.show_media_list(user_input=user_input)
                elif user_input in ["clear"]:
                    clear_screen()
                elif user_input in ["break", "stop", "kill"]:
                    return False
                elif user_input in ["quit", "exit"]:
                    return True
            except Exception:
                pass
            finally:
                write_log(data_list=input_list)


class add_media_gui:
    """
    Gui interface to add new media to database
    """

    def __init__(self) -> None:
        # Get category list
        self.category_list: list = media_section().get_category_list()

        # get last media id , generate new media id
        self.__media_id = media_section().get_new_media_id()
        # GUI design

        self.__root = Tk()
        self.__root.title("Add Media")
        self.__root.minsize(400, 300)
        self.__root.maxsize(400, 300)

        # ID Label and text box
        self.id_label = Label(self.__root, text="ID")
        self.id_label.config(font="15")
        self.id_label.place(x=0, y=0)
        self.id_textbox = Entry(self.__root)
        self.id_textbox.config(font="15", width=20)
        self.id_textbox.place(x=160, y=0)
        self.id_textbox.insert(1, self.__media_id)
        self.id_textbox.configure(state="readonly")

        # Language Label and Combo box
        self.__category_label = Label(self.__root, text="Category")
        self.__category_label.config(font="15")
        self.__category_label.place(x=0, y=30)
        self.n = StringVar()
        self.category = ttk.Combobox(self.__root, width=18, textvariable=self.n)
        self.category.config(font="15")
        self.category["values"] = self.category_list
        self.category.place(x=160, y=30)
        self.category.current()
        self.category.configure(state="readonly")

        # Media Type Label and Combo box
        self.type_label = Label(self.__root, text="Type")
        self.type_label.config(font="15")
        self.type_label.place(x=0, y=60)
        self.m = StringVar()
        self.media_type = ttk.Combobox(self.__root, width=18, textvariable=self.m)
        self.media_type.config(font="15")
        self.media_type["values"] = ("Series", "Movie")
        self.media_type.place(x=160, y=60)
        self.media_type.current()
        self.media_type.configure(state="readonly")

        # Title Label and Tet=xt box
        self.title_label = Label(self.__root, text="Title")
        self.title_label.config(font="15")
        self.title_label.place(x=0, y=90)
        self.title_textbox = Entry(self.__root)
        self.title_textbox.config(font="15")
        self.title_textbox.place(x=160, y=90)

        # Episodes Label and Texr box
        self.episodes_label = Label(self.__root, text="No of Episodes")
        self.episodes_label.config(font="15")
        self.episodes_label.place(x=0, y=120)
        self.episodes_textbox = Entry(self.__root)
        self.episodes_textbox.config(font="15")
        self.episodes_textbox.place(x=160, y=120)

        # Duration Label and Texr box
        self.duration_label = Label(self.__root, text="Duration per Episode")
        self.duration_label.config(font="15")
        self.duration_label.place(x=0, y=150)
        self.duration_textbox = Entry(self.__root)
        self.duration_textbox.config(font="15")
        self.duration_textbox.place(x=160, y=150)

        # Rewatched Label and Texr box
        self.rewatched_label = Label(self.__root, text="Rewatched")
        self.rewatched_label.config(font="15")
        self.rewatched_label.place(x=0, y=180)
        self.rewatched_textbox = Entry(self.__root)
        self.rewatched_textbox.config(font="15")
        self.rewatched_textbox.place(x=160, y=180)
        self.rewatched_textbox.insert(1, 0)

        # Submit button
        self.submit_button = Button(
            self.__root, width=10, text="Submit", command=self.__submit_data
        )
        self.submit_button.config(font="15")
        self.submit_button.place(x=80, y=230)

        # Clear button
        self.clear_button = Button(
            self.__root, width=10, text="Clear", command=self.__clear_field
        )
        self.clear_button.config(font="15")
        self.clear_button.place(x=200, y=230)

        # Movie duration search button
        self.search_button = Button(
            self.__root, width=3, height=1, text="S", command=self.__add_duration
        )
        self.search_button.place(x=350, y=150)

        mainloop()

    def __clear_field(self) -> None:
        """
        Clear all text fields
        """

        self.id_textbox.configure(state="normal")
        self.id_textbox.delete(0, END)
        self.id_textbox.insert(1, media_section().get_new_media_id())
        self.id_textbox.configure(state="readonly")

        self.category.delete(0, END)
        self.media_type.delete(0, END)
        self.title_textbox.delete(0, END)
        self.episodes_textbox.delete(0, END)
        self.duration_textbox.delete(0, END)
        self.rewatched_textbox.delete(0, END)
        self.rewatched_textbox.insert(1, 0)

    def __submit_data(self) -> None:
        """
        Submit data and save it to file
        """
        try:
            # new_media = media(media_id=media_id,media_nam)
            __episodes = self.episodes_textbox.get()
            __duration = self.duration_textbox.get()
            __name = self.title_textbox.get()
            __category = self.category.get()
            __media_type = self.media_type.get()
            __rewatched = self.rewatched_textbox.get()
            try:
                __episodes = int(__episodes)
                __duration = int(__duration)
                __rewatched = int(__rewatched)
                if __name == "" or __category == "" or __media_type == "":
                    raise Exception
            except Exception:
                return
            new_media = media(
                new=True,
                media_id=self.__media_id,
                media_name=__name,
                duration=__duration,
                episodes=__episodes,
                category=__category,
                media_type=__media_type,
                rewatched=__rewatched,
            )
            media_section().new_media(new_media=new_media)
            # exit()
            self.__clear_field()
        except Exception:
            pass

    def __add_duration(self):
        self.duration_textbox.insert(
            1,
            get_duration_of_movie(
                movie_name=self.title_textbox.get(), movie_category=self.category.get()
            ),
        )

    def __set_episode_count(self):
        # to auto entry episode count as 1 if show type is Movie
        if self.category.get() == "Movie":
            self.episodes_textbox.insert(1, 1)


class show_media_table_gui:
    """
    Show media list in GUI window
    """

    def __init__(self, media_category: str = "All") -> None:
        self.__media_category = media_category
        self.__category_list = ["All"] + media_section().get_category_list()

        self.__root = Tk()
        self.__root.title("Media Data Table")
        self.__root.minsize(900, 800)
        self.__root.maxsize(900, 800)

        # category selection in GUI
        self.__category_label = Label(self.__root, text="Category :")
        self.__category_label.place(x=10, y=20)
        self.__n = StringVar()
        self.__category_combobox = ttk.Combobox(
            self.__root, width=18, textvariable=self.__n
        )
        self.__category_combobox["values"] = self.__category_list
        self.__category_combobox.place(x=120, y=20)
        self.__category_combobox.current()
        self.__category_combobox.configure(state="readonly")

        # search button
        self.submit_button = Button(
            self.__root, width=10, text="Search", command=self.__sort_data
        )
        self.submit_button.place(x=300, y=20)

        # desing media_table
        self.__media_table = ttk.Treeview(
            self.__root, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="35"
        )
        self.__media_table.place(x=20, y=60)

        self.__media_table.column("#1", width="50")
        self.__media_table.heading(1, text="Sl.No")

        # self.__media_table.column("#0", width="50")
        # self.__media_table.heading(0, text="ID")

        self.__media_table.column("#2", width="300")
        self.__media_table.heading(2, text="Name")

        self.__media_table.column("#3", width="100")
        self.__media_table.heading(3, text="Type")

        self.__media_table.column("#4", width="100")
        self.__media_table.heading(4, text="Category")

        self.__media_table.column("#5", width="100")
        self.__media_table.heading(5, text="Episodes")

        self.__media_table.column("#6", width="100")
        self.__media_table.heading(6, text="Duration/Ep(min)")

        self.__media_table.column("#7", width="100")
        self.__media_table.heading(7, text="Rewatched")

        # adding scroll bar
        self.__media_data_scrollbar = ttk.Scrollbar(
            self.__root, orient="vertical", command=self.__media_table.yview
        )
        self.__media_table.configure(yscroll=self.__media_data_scrollbar.set)
        # self.__media_data_scrollbar.place(x=880,y=60)
        self.__media_data_scrollbar.pack(side="right", fill="y")

        # adding values into media_table
        self.__show_values(media_category=self.__media_category)

        # when double clicked on a row
        self.__media_table.bind("<Double-1>", self.__on_double_click)

        mainloop()

    def __sort_data(self) -> None:
        self.__show_values(media_category=self.__category_combobox.get())

    def __show_values(self, media_category: str) -> None:
        """
        Adding data to media_table
        """
        # delete all rowns from table
        self.__media_table.delete(*self.__media_table.get_children())

        media_list = media_section().get_media_list()
        sl_no = 0
        self.__media_dic = {}
        for item in media_list:
            if media_category == "All":
                sl_no += 1
                self.__media_dic[sl_no] = convert(file_data=item).to_media().to_list()
                self.__media_table.insert(
                    "", "end", values=[sl_no] + self.__media_dic[sl_no][1::],
                )
                continue
            med = convert(file_data=item).to_media()
            if med.get_category() == media_category:
                sl_no += 1
                self.__media_dic[sl_no] = med.to_list()
                self.__media_table.insert(
                    "", "end", values=[sl_no] + self.__media_dic[sl_no][1::]
                )

    def __on_double_click(self, event) -> None:
        """
        To do event when double clicked on a row in table
        """

        # clicked_media_id =
        edit_media_gui(
            media_to_edit_id=self.__media_dic[
                int(
                    self.__media_table.item(
                        self.__media_table.selection()[0], "values"
                    )[0]
                )
            ][0]
        )
        # print(self.__media_table.item(self.__media_table.selection()[0], "values")[0])
        pass
        # edit_media_gui(media)


class edit_media_gui:
    """
    Gui interface to edit media data
    """

    def __init__(self, media_to_edit_id: int) -> None:
        self.__media_id = media_to_edit_id
        # Get category list
        self.category_list: list = media_section().get_category_list()

        # get converted list.
        self.converted_media_list = duplicate(
            data_list=media_section().get_media_list(), data_type="media"
        ).get_converted_list()
        # index of the required media in list
        self.index: int = media_section().binary_search(
            data_list=self.converted_media_list, media_id=self.__media_id,
        )
        # media to edit
        self.__media_to_edit = self.converted_media_list[self.index]
        # GUI design

        self.__root = Tk()
        self.__root.title("Edit Media")
        self.__root.minsize(400, 300)
        self.__root.maxsize(400, 300)

        # ID Label and text box
        self.id_label = Label(self.__root, text="ID")
        self.id_label.config(font="15")
        self.id_label.place(x=0, y=0)
        self.id_textbox = Entry(self.__root)
        self.id_textbox.config(font="15", width=20)
        self.id_textbox.place(x=160, y=0)

        # Language Label and Combo box
        self.__category_label = Label(self.__root, text="Category")
        self.__category_label.config(font="15")
        self.__category_label.place(x=0, y=30)
        self.n = StringVar()
        self.category = ttk.Combobox(self.__root, width=18, textvariable=self.n)
        self.category.config(font="15")
        self.category["values"] = self.category_list
        self.category.place(x=160, y=30)
        self.category.current()

        # Media Type Label and Combo box
        self.type_label = Label(self.__root, text="Type")
        self.type_label.config(font="15")
        self.type_label.place(x=0, y=60)
        self.m = StringVar()
        self.media_type = ttk.Combobox(self.__root, width=18, textvariable=self.m)
        self.media_type.config(font="15")
        self.media_type["values"] = ("Series", "Movie")
        self.media_type.place(x=160, y=60)
        self.media_type.current()

        # Title Label and Tet=xt box
        self.title_label = Label(self.__root, text="Title")
        self.title_label.config(font="15")
        self.title_label.place(x=0, y=90)
        self.title_textbox = Entry(self.__root)
        self.title_textbox.config(font="15")
        self.title_textbox.place(x=160, y=90)

        # Episodes Label and Texr box
        self.episodes_label = Label(self.__root, text="No of Episodes")
        self.episodes_label.config(font="15")
        self.episodes_label.place(x=0, y=120)
        self.episodes_textbox = Entry(self.__root)
        self.episodes_textbox.config(font="15")
        self.episodes_textbox.place(x=160, y=120)

        # Duration Label and Texr box
        self.duration_label = Label(self.__root, text="Duration per Episode")
        self.duration_label.config(font="15")
        self.duration_label.place(x=0, y=150)
        self.duration_textbox = Entry(self.__root)
        self.duration_textbox.config(font="15")
        self.duration_textbox.place(x=160, y=150)

        # Rewatched Label and Texr box
        self.rewatched_label = Label(self.__root, text="Rewatched")
        self.rewatched_label.config(font="15")
        self.rewatched_label.place(x=0, y=180)
        self.rewatched_textbox = Entry(self.__root)
        self.rewatched_textbox.config(font="15")
        self.rewatched_textbox.place(x=160, y=180)
        # self.rewatched_textbox.insert(1, 0)

        # add values to fields
        self.id_textbox.insert(1, self.__media_id)
        self.id_textbox.configure(state="readonly")

        self.category.insert(1, self.__media_to_edit.get_category())
        self.category.configure(state="readonly")

        self.media_type.insert(1, self.__media_to_edit.get_type())
        self.media_type.configure(state="readonly")

        self.title_textbox.insert(1, self.__media_to_edit.get_name())
        self.episodes_textbox.insert(1, self.__media_to_edit.get_episodes())
        self.duration_textbox.insert(1, self.__media_to_edit.get_duration())
        self.rewatched_textbox.insert(1, self.__media_to_edit.get_rewatched())

        # update button
        self.update_button = Button(
            self.__root, width=10, text="Update", command=self.__update_data
        )
        self.update_button.config(font="15")
        self.update_button.place(x=170, y=230)

        # Movie duration search button
        self.search_button = Button(
            self.__root, width=3, height=1, text="S", command=self.__add_duration
        )
        self.search_button.place(x=350, y=150)

        mainloop()

    def __update_data(self) -> None:
        """
        Submit data and save it to file
        """
        try:
            edited: bool = False
            # new_media = media(media_id=media_id,media_nam)
            __episodes = self.episodes_textbox.get()
            __duration = self.duration_textbox.get()
            __name = self.title_textbox.get()
            __category = self.category.get()
            __media_type = self.media_type.get()
            __rewatched = self.rewatched_textbox.get()
            try:
                __episodes = int(__episodes)
                __duration = int(__duration)
                __rewatched = int(__rewatched)
                if __name == "" or __category == "" or __media_type == "":
                    raise Exception
            except Exception:
                return

            if self.__media_to_edit.get_name() != __name:
                edited = True
                self.__media_to_edit.set_name(name=__name)
            if self.__media_to_edit.get_category() != __category:
                edited = True
                self.__media_to_edit.set_category(category=__category)
            if self.__media_to_edit.get_type() != __media_type:
                edited = True
                self.__media_to_edit.set_type(media_type=__media_type)
            if self.__media_to_edit.get_duration() != __duration:
                edited = True
                self.__media_to_edit.set_duration(duration=__duration)
            if self.__media_to_edit.get_episodes() != __episodes:
                edited = True
                self.__media_to_edit.set_episodes(episodes=__episodes)
            if self.__media_to_edit.get_rewatched() != __rewatched:
                edited = True
                self.__media_to_edit.set_rewatched(rewatched=__rewatched)

            if edited:
                self.converted_media_list.pop(self.index)
                self.converted_media_list.append(self.__media_to_edit)
                if media_section().rewrite_entire_media_data(
                    data_to_rewrite=self.converted_media_list
                ):
                    print("Data updated")
                    return
        except Exception as e:
            print(e)
            pass

    def __add_duration(self):
        self.duration_textbox.insert(
            1,
            get_duration_of_movie(
                movie_name=self.title_textbox.get(), movie_category=self.category.get()
            ),
        )


if __name__ == "__media__":
    pass
    # show_media_table_gui(media_category="All")
    # add_media_gui()
