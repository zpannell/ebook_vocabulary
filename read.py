import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os
import tkinter.filedialog
from pathlib import Path
import sys


def main():
    # input file
    fileIn = tkinter.filedialog.askopenfilename()
    if not fileIn:
        sys.exit("No file selected")
    extract_text(fileIn)

def extract_text(fileIn):
    # create directories to store outputs
    title = Path(fileIn).stem
    directory = f"{Path(fileIn).parents[0]}/text_files"
    if not os.path.exists(directory):
        os.makedirs(directory)
    fullbook = f"{directory}/{title}.txt"

    # set chapter start keywords
    keywords = ["Chapter", "Letter", "CAPÍTULO", "CAPITULO"]

    # read ebook file and store as book
    book = epub.read_epub(fileIn, {"ignore_ncx": True})
    full_book(book, fullbook)
    each_chapter(book, directory, keywords)


# extract text from paragraph tags
def para_extract(soup):
    content = ""
    data = soup.find_all("p")
    content = " ".join([p1.text for p1 in data])
    # enable the below line and disable above to put each <p> on a new line
    # content = "\n".join([p1.text for p1 in data])
    return content


# create file with book text
def full_book(book, output):
    content = ""
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), "html.parser")
            content += para_extract(soup)
            with open(output, "w") as fout:
                fout.write(content)


# create one file for each chapter that includes that chapter's text
def each_chapter(book, directory, keywords):
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), "html.parser")
            for header in soup.find_all(["h1", "h2", "h3", "h4", "h5"]):
                content = ""
                headers = header.get_text().strip()
                for keyword in keywords:
                    if keyword in headers:
                        content += para_extract(soup)
                        with open(f"{directory}/{headers}.txt", "w") as file:
                            file.write(content)


if __name__ == "__main__":
    main()
