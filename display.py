import os
import sys

from pikepdf import Pdf, Name

doubleFirst = []

def set_page_display(filename: str):
    if not filename.endswith(".pdf"):
        return
    with Pdf.open(filename, allow_overwriting_input=True) as file:
        if any(instrument in filename for instrument in doubleFirst):
            print(f"Setting display of '{filename}' to TwoPageLeft")
            file.Root.PageLayout=Name("/TwoPageLeft")
        else:
            print(f"Setting display of '{filename}' to TwoPageRight")
            file.Root.PageLayout=Name("/TwoPageRight")
        file.save(filename)

def process_dir(dirname: str):
    for filename in os.listdir(dirname):
        filename = f"{dirname}/{filename}"
        set_page_display(filename)
    

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parts_dir = f"{script_dir}/parts_output"
    process_dir(parts_dir)
    set_page_display(f"{script_dir}/Tailleferre - Harp Concertino.pdf")
