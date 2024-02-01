import tkinter.filedialog
from pathlib import Path
import re
import csv


# import file as string
def main():
    # input file
    fileIn = tkinter.filedialog.askopenfilename()
    if not fileIn:
        sys.exit("No file selected")
    title = Path(fileIn).stem

    # create dictionary that contains each word and its corresponding number of appearances
    dict = {}
    with open(fileIn, "r") as file:
        text = file.read().lower()
        text = re.sub(r"[^\wñáéíóú\-']+", " ", text)
        # print(text)
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

    with open("mycsvfile.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in sortedDict.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    main()
