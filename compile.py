from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle

score_file = "01 - Full score - Concertino.pdf"
notes_file = "tailleferre_harp_concertino_commentary.pdf"
output_file = "Tailleferre - Harp Concertino.pdf"

def main():
    writer = PdfWriter()
    writer.append(score_file, pages=(0, 90))
    writer.append(notes_file)
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Full Score", 2)
    writer.add_outline_item("I.94 Original Notation", 87)
    writer.add_outline_item("I. Cadenza Ossia", 88)
    writer.add_outline_item("Editorial Commentary", 90)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Instrumentation")
    writer.set_page_label(2, 90, style=PageLabelStyle.DECIMAL)
    writer.write(output_file)

if __name__ == "__main__":
    main()