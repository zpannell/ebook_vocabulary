import tkinter.filedialog
import sys
from pathlib import Path
from read import extract_text
from word_frequency import convert_text
from translate import translate


def main():
    fileIn = tkinter.filedialog.askopenfilename()
    if not fileIn:
        sys.exit("No file selected")
    title = Path(fileIn).stem
    bookDir = f"{Path(fileIn).parents[0]}"

    extract_text(fileIn)
    convert_text(f"{bookDir}/text_files")
    translate(f"{bookDir}/word_frequency")


if __name__ == "__main__":
    main()
