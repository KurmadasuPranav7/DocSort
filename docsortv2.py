import os
import shutil
import sys
import mysql.connector

user = os.getlogin()
executable_location = sys.executable
executable_directory = os.path.dirname(os.path.realpath(executable_location))

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kp#7@msd",
        database="docsortlog"
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE log("
                     "S_no INT NOT NULL auto_increment PRIMARY KEY,"
                     "date DATE,"
                     "time TIME,"
                     "initial_directory VARCHAR(50),"
                     "final_directory VARCHAR(50));")

except mysql.connector.errors.ProgrammingError:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kp#7@msd"
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE docsortlog;")

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kp#7@msd",
            database="docsortlog"
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE log("
                         "S_no INT NOT NULL auto_increment PRIMARY KEY,"
                         "date DATE,"
                         "time TIME,"
                         "initial_directory VARCHAR(50),"
                         "final_directory VARCHAR(50));")

    except mysql.connector.errors.DatabaseError:
        pass


def mover(user, file_name, each_folder, executable_directory):
    newdb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kp#7@msd",
        database="docsortlog"
    )

    newcursor = newdb.cursor()

    if os.path.exists(f"C:\\Users\\{user}\\Downloads\\{file_name}"):
        try:
            shutil.move(each_folder, f"C:\\Users\\{user}\\Downloads\\{file_name}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_folder}", f"C:\\Users\\{user}\\Downloads\\{file_name}")
            mycursor.execute(sql, val)

            mydb.commit()

        except FileExistsError:
            for objects in os.listdir(f"C:\\Users\\{user}\\Downloads\\{each_folder}"):
                shutil.move(objects, f"C:\\Users\\{user}\\Downloads\\{file_name}\\{each_folder}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_folder}", f"C:\\Users\\{user}\\Downloads\\{file_name}")
            mycursor.execute(sql, val)

            mydb.commit()

        except Exception as e:
            pass
    else:
        path2 = f'./{file_name}'
        os.mkdir(path2)
        try:
            shutil.move(each_folder, f"C:\\Users\\{user}\\Downloads\\{file_name}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_folder}", f"C:\\Users\\{user}\\Downloads\\{file_name}")
            mycursor.execute(sql, val)

            mydb.commit()

        except FileExistsError:
            for objects in os.listdir(f"C:\\Users\\{user}\\Downloads\\{each_folder}"):
                shutil.move(objects, f"C:\\Users\\{user}\\Downloads\\{file_name}\\{each_folder}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_folder}", f"C:\\Users\\{user}\\Downloads\\{file_name}")
            mycursor.execute(sql, val)

            mydb.commit()

        except Exception as e:
            pass


os.chdir(f"C:\\Users\\{user}\\Downloads")
files = list(os.listdir(os.getcwd()))

for each_file in files:
    split = os.path.splitext(each_file)
    extension = str(split[1])
    if os.path.exists(f"C:\\Users\\{user}\\Downloads\\{extension.lower()}"):
        try:
            shutil.move(each_file, f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_file}", f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")
            mycursor.execute(sql, val)

            mydb.commit()

        except Exception as e:
            pass
    else:
        try:
            path = f'C:\\Users\\{user}\\Downloads\\{extension.lower()}'
            os.mkdir(path)
            shutil.move(each_file, f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")

            sql = ("INSERT INTO log (date, time, initial_directory, final_directory) VALUES (CURRENT_DATE(), "
                   "CURRENT_TIME(),%s,%s)")
            val = (f"{each_file}", f"C:\\Users\\{user}\\Downloads\\{extension.lower()}")
            mycursor.execute(sql, val)

            mydb.commit()

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
