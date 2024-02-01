import tkinter.filedialog
import sys
import os
from pathlib import Path
from deep_translator import GoogleTranslator
import csv
import itertools


def main():
    # set directory of word frequency csv files
    csvDir = tkinter.filedialog.askdirectory()
    if not csvDir:
        sys.exit("No path selected")


def translate(csvDir):
    for filename in os.listdir(csvDir):
        infilepath = os.path.join(csvDir, filename)
        translate_file(infilepath)


def translate_file(fileIn):
    title = Path(fileIn).stem

    # create dict with translations
    dict = {}
    with open(fileIn, "r") as file:
        for row in itertools.islice(file, 20):
            value = GoogleTranslator(source="es", target="en").translate(
                row.split(",")[0]
            )
            dict[row.split(",")[0]] = value.lower()

    # create output directory
    directory = f"{Path(fileIn).parents[1]}/translated"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # create csv file
    with open(f"{directory}/{title}.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dict.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    main()
