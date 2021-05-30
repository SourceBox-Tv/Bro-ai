from zipfile import ZipFile
import os
import time
filename = "app.zip"
def filres():
    with ZipFile(filename, 'r') as zip:
        zip.printdir()
        zip.extractall("./app/")
def upadated():
            import requests
            from clint.textui import progress
            print("After downloading file; it would be in zip file, please replace this file with the downloaded one")
            url = ["https://github.com/SourceBox-Tv/Bro-aiwithpython/releases/download/Bro1.0/app.zip"]
            files = ["app.zip"]
            for url, files in zip(url,files):
                r = requests.get(url, stream=True)
                with open(files, "wb") as Pypdf:
                    total_length = int(r.headers.get('content-length'))
                 
                    for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)
def main():
        if __name__ == '__main__':
            upadated()
            filres()
            os.remove(filename)
