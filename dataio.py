import os
import re

def there_are_new_data():
    # Define the regular expressions for matching the file names
    txt_pattern = r".*_updated\.txt$"
    csv_pattern = r".*_updated\.csv$"

    txt_files = [file for file in os.listdir(os.getcwd()) if re.match(txt_pattern, file)]

    csv_files = [file for file in os.listdir(os.getcwd()) if re.match(csv_pattern, file)]
    
    if(len(txt_files) > 0 or len(csv_files) > 0):
        return True, txt_files, csv_files
    return False, None, None


def update_vectorstore():
    pass