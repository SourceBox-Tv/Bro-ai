from zipfile import ZipFile
import os
import platform
import requests
from clint.textui import progress
filename = "windows.zip"
def filres():
    with ZipFile(filename, 'r') as zip:
        zip.printdir()
        zip.extractall("./app")
def upadated():
            print("After downloading file please replace this file with the downloaded one")
            url = ["https://github.com/SourceBox-Tv/Bro-aiwithpython/releases/latest/download/windows.zip"]
            files = ["windows.zip"]
            for url, files in zip(url,files):
                r = requests.get(url, stream=True)
                with open(files, "wb") as Pypdf:
                    total_length = int(r.headers.get('content-length'))
                 
                    for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)
def otherupdates():

            url = ["https://raw.githubusercontent.com/SourceBox-Tv/Bro-aiwithpython/master/ai.py",
             "https://raw.githubusercontent.com/SourceBox-Tv/Bro-aiwithpython/master/media.py",
              "https://raw.githubusercontent.com/SourceBox-Tv/Bro-aiwithpython/master/screenshots.py",
               "https://raw.githubusercontent.com/SourceBox-Tv/Bro-aiwithpython/master/goals.py"]
            
            files = ["ai.py","screenshot.py","media.py","goals.py"]
            for url, files in zip(url,files):
                rg = requests.get(url, stream=True)
                with open(files, "wb") as Pypdf:
                    total_length = int(rg.headers.get('content-length'))
                 
                    for ch in progress.bar(rg.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)
def main():
    if platform.system() == "Windows":
            upadated()
            filres()
            os.remove(filename)
    else:
        otherupdates()
