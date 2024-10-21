from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("Test.pdf")
writer = PdfWriter()
writer.add_page(reader.pages[0])
writer.pages[0].rotate(180)

with open("rotated.pdf", "wb") as fp:
    writer.write(fp)