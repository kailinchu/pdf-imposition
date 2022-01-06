from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
import math
import sys

# note to self: use pyenv version 3.9.7

# define page size for letter (landscape)
# based on postscript units here: https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/page_sizes
page_width = 792
page_height = 612

def pdf_generator(file_in, file_out):
    reader = PdfFileReader(file_in)
    writer = PdfFileWriter()
    num_pages = reader.getNumPages()
    num_groups_of_4 = math.ceil(num_pages / 4)

    # loop through groups of 4 pages
    for i in range(num_groups_of_4):
        # create list of pages and then call four_in_one to merge the 4 pages together
        if (num_pages >= 4):
            list_size = 4
            num_pages -= 4
        else:
            list_size = num_pages
            num_pages = 0
        pages = []

        for j in range(list_size):
            pages.append(reader.getPage(i*4 + j))
        
        writer.addPage(four_in_one(pages))
    with open(file_out, "wb") as file:
        writer.write(file)
    print(f"Success! The new file is located at {file_out}")
    return

def four_in_one(pages):
    # given a list of 1 to 4 pages, returns a page on which the four input pages have been imposed
    # make new page
    page = PageObject.createBlankPage(width=page_width, height=page_height)

    for i in range(len(pages)):
        x = ((i % 2) == 1) * page_width / 2 # index 0 & 2 should have value 0, 1 & 3 should be w/2
        y = (i <= 1) * page_height / 2 # index 0 & 1 should have value h/2, 2 & 3 should be 0
        page.mergeScaledTranslatedPage(pages[i], 0.5, x, y)
    return page

if __name__ == '__main__':
    # input format: imposition.py <input file> <output file, optional>
    if len(sys.argv) == 3:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
    elif len(sys.argv) == 2:
        file_in = sys.argv[1]
        file_out = sys.argv[1]
    else:
        sys.exit("Usage: python imposition.py <input.pdf> <output.pdf, optional>")
    pdf_generator(file_in, file_out)