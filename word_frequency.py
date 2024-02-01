import tkinter.filedialog
from pathlib import Path
import re
import csv
import sys
import os


def main():
    # set directory of text files
    textDir = tkinter.filedialog.askdirectory()
    if not textDir:
        sys.exit("No path selected")
    convert_text(textDir)


# iterate over each file in the folder and convert it to word frequency csv
def convert_text(textDir):
    for filename in os.listdir(textDir):
        infilepath = os.path.join(textDir, filename)
        convert_to_csv(infilepath)


def convert_to_csv(fileIn):
    title = Path(fileIn).stem

    # create dictionary that contains each word and its corresponding number of appearances
    dict = {}
    with open(fileIn, "r") as file:
        text = file.read().lower()
        text = re.sub(r"[^\wñáéíóú\-']+", " ", text)
        text = text.split()
        for word in text:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

    # sort dictionary by order of appearances
    sortedDict = {
        k: v for k, v in sorted(dict.items(), key=lambda v: v[1], reverse=True)
    }

    # create output directory
    directory = f"{Path(fileIn).parents[1]}/word_frequency"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # create csv file
    with open(f"{directory}/{title}.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in sortedDict.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    main()
