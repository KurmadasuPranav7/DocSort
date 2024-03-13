import os
import shutil
import sys
from datetime import datetime

user = os.getlogin()
executable_location = sys.executable
executable_directory = os.path.dirname(os.path.realpath(executable_location))


def mover(user, file_name, each_folder, executable_directory):
    if os.path.exists(f"C:\\Users\\{user}\\Downloads\\{file_name}"):
        try:
            shutil.move(each_folder, f"C:\\Users\\{user}\\Downloads\\{file_name}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_folder}  is moved to  C:\\Users\\{user}\\Downloads\\{file_name}\n")
        except FileExistsError:
            for objects in os.listdir(f"C:\\Users\\{user}\\Downloads\\{each_folder}"):
                shutil.move(objects, f"C:\\Users\\{user}\\Downloads\\{file_name}\\{each_folder}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_folder}  is moved to  C:\\Users\\{user}\\Downloads\\{file_name}\n")
        except Exception as e:
            pass
    else:
        path2 = f'./{file_name}'
        os.mkdir(path2)
        try:
            shutil.move(each_folder, f"C:\\Users\\{user}\\Downloads\\{file_name}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_folder}  is moved to  C:\\Users\\{user}\\Downloads\\{file_name}\n")
        except FileExistsError:
            for objects in os.listdir(f"C:\\Users\\{user}\\Downloads\\{each_folder}"):
                shutil.move(objects, f"C:\\Users\\{user}\\Downloads\\{file_name}\\{each_folder}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_folder}  is moved to  C:\\Users\\{user}\\Downloads\\{file_name}\n")
        except Exception as e:
            pass


if not os.path.isfile(rf"{executable_directory}\log.txt"):
    os.chdir(rf"{executable_directory}")
    f = open("log.txt", "x")
    f.close()

os.chdir(f"C:\\Users\\{user}\\Downloads")
files = list(os.listdir(os.getcwd()))

for each_file in files:
    split = os.path.splitext(each_file)
    extension = str(split[1])
    if os.path.exists(f"C:\\Users\\{user}\\Downloads\\{extension.lower()}"):
        try:
            shutil.move(each_file, f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_file}  is moved to  C:\\Users\\{user}\\Downloads\\{extension.lower()}\n")
        except Exception as e:
            pass
    else:
        try:
            path = f'C:\\Users\\{user}\\Downloads\\{extension.lower()}'
            os.mkdir(path)
            shutil.move(each_file, f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")
            with open(rf"{executable_directory}\log.txt", 'a') as file:
                file.write(
                    f"{datetime.now()}  -  {each_file}  is moved to  C:\\Users\\{user}\\Downloads\\{extension.lower()}\n")
        except Exception as e:
            pass

for each_folder in os.listdir(f"C:\\Users\\{user}\\Downloads"):
    if each_folder in {".3gp", ".aa", ".aac", ".aax", ".act", ".aiff", ".alac", ".amr", ".ape", ".au", ".awb", ".dss",
                       ".dvf", ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b", ".m4p", ".mmf", ".movpkg", ".mp3",
                       ".mpc", ".msv", ".nmf", ".ogg", ".oga", ".mogg", ".opus", ".ra", ".rm", ".raw", ".rf64", ".sln",
                       ".tta", ".voc", ".vox", ".wav", ".wma", ".wv", ".webm", ".8svx", ".cda"}:
        mover(user, "Audio", each_folder, executable_directory)
    elif each_folder in {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".3gp", ".webm", ".ogv", ".m4v", ".mpeg",
                         ".mpg", ".rm", ".swf", ".vob"}:
        mover(user, "Video", each_folder, executable_directory)
    elif each_folder in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".jfif", ".heif",
                         ".raw", ".eps", ".psd", ".ai", ".indd", ".tif", ".jfif", ".jp2", ".j2k", ".jpx", ".wdp",
                         ".hdp", ".arw", ".cr2", ".nef", ".orf", ".sr2", ".rw2"}:
        mover(user, "Image", each_folder, executable_directory)
    elif each_folder in {".doc", ".docx", ".dot", ".dotx", ".rtf"}:
        mover(user, "Document", each_folder, executable_directory)
    elif each_folder in {".xls", ".xlsx", ".xlsm", "xlsb", ".xltx", ".xltm", ".csv"}:
        mover(user, "Spreadsheet", each_folder, executable_directory)
    elif each_folder in {".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm"}:
        mover(user, "PowerPoint", each_folder, executable_directory)
    elif each_folder in {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tar.gr", ".tar.bz2"}:
        mover(user, "Compressed", each_folder, executable_directory)
    elif each_folder in {".exe", ".msi", ".dll", ".sys", ".cmd", ".lnk", ".reg", ".ini", ".inf", ".log"}:
        mover(user, "WinRelated", each_folder, executable_directory)
    else:
        pass
