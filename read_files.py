import os
from insert_data import *


# file_path = r"C:\exselentim\bootcamp\google\archive\python-3.8.4-docs-text\distutils"
# os.environ['MY_ROOT_PATH'] = file_path


def read_files_in_directory(dict_line, dict_words, path):
    """
    Read files in a specified directory defined by the MY_ROOT_PATH environment variable.
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            read_file(file_path, dict_line, dict_words)


def read_file(file_path, dict_line, dict_words, encoding='latin-1'):
    """
    Read a file, handling Unicode decoding errors, and perform additional actions.

    :param file_path: Path to the file to be read.
    :param encoding: Encoding to use when reading the file.
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            for line_number, line in enumerate(file, start=1):
                file_name = file_path.split('\\')[-1].split('.')[0]
                insert_line_dict(line, file_name, line_number, dict_line)
                insert_words_dict(line, file_name, line_number, dict_words)

    except UnicodeDecodeError:
        print(f"Error reading {file_path} with {encoding} encoding")
