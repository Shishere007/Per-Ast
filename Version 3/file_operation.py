import json

__name__ = "file_operation"
"""Methodes:-
    > read_data()
    > append_one_data(data_to_append)
    > rewrite_entire_data(file_data)
    > empty_file()
    > is_empty()
    > line_count()
"""


class File:
    """
    file related operations
    """

    def __init__(self, file_location: str) -> None:
        self.file_location = file_location
        self.__create_file(file_location=self.file_location)

    def __create_file(self, file_location: str) -> None:
        """
        Creates a file at the given location 
        if the specified file doesn't exist
        """
        try:
            with open(file=file_location, mode="r"):
                pass
        except Exception:
            self.empty_file()

    def read_data(self) -> list:
        """
        Read data from file return it as list
        """
        try:
            with open(file=self.file_location, mode="r") as file:
                file_data = json.load(file)
            return file_data
        except Exception as e:
            print(f"file_operation > read - {e}")

    def append_one_data(self, data_to_append: str) -> bool:
        """
        Add one data to the file
        """
        try:
            file_data = self.read_data()
            new_data = data_to_append.to_dictionary()
            file_data.append(new_data)
            with open(file=self.file_location, mode="w") as file:
                json.dump(file_data, file)
            return True
        except Exception as e:
            print(f"file_operation > append_one_data - {e}")
        return False

    def append_one_data_string(self, data_to_append: str) -> bool:
        """
        Add one string data to the file
        """
        try:
            file_data = self.read_data()
            file_data.append(data_to_append)
            with open(file=self.file_location, mode="w") as file:
                json.dump(file_data, file)
            return True
        except Exception as e:
            print(f"file_operation > append_one_data - {e}")
        return False

    def delete_one_data(self, file_data: list, data_to_delete: str) -> bool:
        """
        Delete one data from the file
        Send the data_to_delete in dic form
        """
        try:
            file_data.remove(data_to_delete)
            with open(file=self.file_location, mode="w") as file:
                json.dump(file_data, file)
            return True
        except Exception as e:
            print(f"file_operation > delete_one_data - {e}")
        return False

    def rewrite_entire_data(self, file_data: list) -> bool:
        """
        Rewrite the entire data to file after erasing the file
        """
        try:
            new_data = []
            for item in file_data:
                new_data.append(item.to_dictionary())
            with open(file=self.file_location, mode="w") as file:
                json.dump(new_data, file)
            return True
        except Exception as e:
            print(f"file_operation > rewrite - {e}")
        return False

    def empty_file(self) -> bool:
        """
        Empty file by erasing all data in it
        """
        try:
            with open(file=self.file_location, mode="w") as file:
                json.dump([], file)
            return True
        except Exception as e:
            print(f"file_operation > empty_file - {e}")
        return False

    def is_empty(self) -> bool:
        """
        Returns True if file is empty
        False otherwise
        """
        try:
            if self.read_data() == []:
                return True
            return False
        except Exception as e:
            print(f"file_operation > is_empty - {e}")

    def line_count(self) -> int:
        """
        Returns no of lines of data written in the file
        """
        try:
            file_data = self.read_data()
            return len(file_data)
        except Exception as e:
            print(f"file_operation > line_count - {e}")

    def add_list_of_data(self, data_list: list) -> None:
        """
        Write a list of data to a file
        """
        try:
            file_data = self.read_data()
            for item in data_list:
                file_data.append(item.to_dictionary())
            with open(file=self.file_location, mode="w") as file:
                json.dump(file_data, file)
        except Exception as e:
            print(f"file_operation > add_list_of_data - {e}")
        finally:
            pass


if __name__ == "file_operation":
    pass
