import os
import time
path = "C:\\Users\\absh_\\Downloads\\"

files = os.listdir(path)
print("Files pdf files older than a year:")
for file in files:
    if file.endswith(".pdf"):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_age = os.path.getmtime(file_path)
            if (time.time() - file_age) > (365 * 24 * 60 * 60):  # older than a year
                print(file)
print("Save this list in a text file")
with open("old_pdfs.txt", "w") as f:
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                file_age = os.path.getmtime(file_path)
                if (time.time() - file_age) > (365 * 24 * 60 * 60):
                    f.write(file + "\n")