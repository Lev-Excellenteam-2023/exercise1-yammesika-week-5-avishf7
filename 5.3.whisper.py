import re


def find_all_whisper_strings(path, pattern):
    """
        This function searches for all occurrences of a given regular expression pattern in a file located at a specified path
        and yields each matched string.
        :param path: A string representing the path to a file
        :param pattern: A regular expression pattern to search for in the file
        :return: A string containing the matched substring.
        """
    with open(path, mode="rb") as logo:
        for line in logo:
            for whisper_str in re.finditer(pattern, str(line)):
                yield whisper_str.group()


iter_strings = find_all_whisper_strings("images/logo.jpg", "[a-z]{5}[a-z]*!")
for ms in iter_strings:
    print(ms)
