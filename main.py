from datetime import datetime
import os
import time

if __name__ == '__main__':
    datetime_obj = datetime.now()
    print(f"datetime_obj = {datetime_obj}")
    print(f"datetime_obj type = {type(datetime_obj)}")

    folder_name = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    # ':' is not allowed in folder naming in Windows, so change it to '_'
    folder_name = folder_name.replace(':', '_')
    print(f"Folder name will be: {folder_name}")
    print(f"folder_name type = {type(folder_name)}")

    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    folder_directory = cwd + "\\" + folder_name
    print(f"Will try to create new folder: {folder_directory}")

    try:
        if not os.path.exists(folder_directory):
            os.mkdir(folder_directory)
            print(f"Successfully created directory: {folder_directory}")
    except Exception as e:
        print(f"Failed to create directory! {e}")

    print("Finish!")
    time.sleep(5)

