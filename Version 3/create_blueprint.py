from pathlib import Path
from os import getcwd

__name__ = "__blueprint__"

"""
Create blueprint of python file
"""
# file_name = "Blueprint.md"
file_name = "Blueprint.md"
current_path = getcwd()


def create_file() -> None:
    """
    Create file if doesnt exist, erase if exists
    """
    with open(file=file_name, mode="w"):
        pass


def write(lines: [str]) -> None:
    def remove(string: str) -> str:
        return "    " + "".join(list(string)[:-2]) + "\n"

    # new_list = []
    temp_list = []
    flag = False
    with open(file=file_name, mode="a") as file:
        for item in lines:
            if flag:

                def rem(string: str) -> str:
                    temp = list(string)
                    while temp[0] == " ":
                        temp.pop(0)
                    return "".join(temp)

                if not item.endswith(":\n"):
                    temp_list.append("".join(list(rem(string=item)))[:-1] + " ")
                    continue
                else:
                    temp_list.append(rem(string=item))
                new_item = ""
                for item in temp_list:
                    new_item = new_item + item
                item = new_item
                flag = False
                temp_list = []

            if "class" in item.split():
                item = remove(string=item)
                # new_list.append(item)
                file.writelines("\n")
                file.writelines(item)
            elif "def" in item.split():
                if not item.endswith(":\n"):
                    temp_list.append("".join(list(item))[:-1])
                    flag = True
                    continue
                item = remove(string=item)
                # new_list.append(item)
                file.writelines(item)
        file.writelines("\n\n")
    """with open(file=file_name, mode="a") as file:
        for item in new_list:
            file.writelines(item)
        file.writelines("\n\n")"""


def write_methodes() -> None:
    file_list = get_py_files()

    for item in file_list:
        with open(file=item, mode="r") as file:
            lines = file.readlines()
        with open(file=file_name, mode="a") as file:
            file.writelines(f"## {item}\n\n")
        write(lines=lines)


def get_py_files() -> list:
    files = []
    for item in Path(current_path).glob("*"):
        if str(item).__contains__(".py") and not str(item).__contains__("test"):
            files.append(str(item).split("\\")[-1])
    return files


def write_files() -> None:
    files = get_py_files()

    with open(file=file_name, mode="a") as file:
        file.writelines("# Files\n")
        file.writelines("## Python Files\n")
        for item in files:
            file.writelines("    " + item + "\n")
        file.writelines("\n\n")
    files = []
    for item in Path(current_path + "\Data").glob("*"):
        files.append("    " + str(item).split("\\")[-1])
    with open(file=file_name, mode="a") as file:
        file.writelines("## Data Files\n")
        for item in files:
            file.writelines(item + "\n")
        file.writelines("\n\n")
        file.writelines("\n# Class and Functions\n")


if __name__ == "__blueprint__":
    create_file()
    write_files()
    write_methodes()
