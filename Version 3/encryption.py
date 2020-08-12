from string import ascii_lowercase, digits, punctuation

__name__ = "__encryption__"


class encryption:
    def __init__(self) -> None:
        self.__encryption_code = self.__get_encryption_code()

    def __get_encryption_code(self) -> dict:
        """
        Get encryption code. code for each character
        """
        start_num = 10
        characters = ascii_lowercase + punctuation + digits + " "
        encryption_codes = {}
        for char in characters:
            encryption_codes[char] = start_num
            start_num += 1
        return encryption_codes

    def encode(self, data: str) -> str:
        """
        Encode the data 
        """
        data_list = list(data)
        encoded_list = []
        for char in data_list:
            encoded_list.append(str(self.__encryption_code[char]))
        encoded_data = "".join(encoded_list)
        return encoded_data

    def decode(self, data: str) -> str:
        """
        Decode the data
        """
        code_char_list = []
        for var in range(0, len(data), 2):
            code_char_list.append(data[var : var + 2])
        keys = list(self.__encryption_code.keys())
        values = [str(var) for var in self.__encryption_code.values()]
        decoded_list = []
        for item in code_char_list:
            decoded_list.append(keys[values.index(item)])
        decoded_data = "".join(decoded_list)
        return decoded_data


if __name__ == "__encryption__":
    pass
