from PyPDF2 import PdfReader, PdfWriter
import re

def main():
    # an intro message after activating the program
    intro = """ Welcome to Gemini's command line PDF editor
        it's fun Fun FUN!!!  What do you expect?
        It's free!!!! Battery and user manuel not included...
        """
    print(intro)
    services = """ How would you like to edit your PDF file(s) today?
        press '1' for file size compression,
        press '2' for page(s) rotation,
        press '3' for page(s) trimming and
        press '4' for merging up to 5 PDF files
        """
    select = input(services)
    if int(select) in [1, 2, 3, 4]:
        filename = input("Please enter the targeted PDF file name for operation: ")
    else:
        raise ValueError("Wrong selection of PDF editor function input, please try again")

    # the file name input is examined by a validator function known as name_valid, prior to the execution
    if name_valid(filename) == True:
        match select:
            case "1":
                compressing(filename)
            case "2":
                rotating(filename)
            case "3":
                trimming(filename)
            case "4":
                merging(filename)

# a function to validate the input file name
def name_valid(filename):
    try:
        filename = filename.strip()
        # checking whether the input file type / extension to be valid
        if not filename.lower().endswith(".pdf"):
            raise ValueError("PDF file only ")

        # screen out --unwelcomed-- char and or space(s) from the file name input
        if " " in filename or "#" in filename or "@" in filename:
            raise ValueError("Invalid char for the file name input ")

        # finally verify whether the file actually exists
        with open(filename, "rb") as inputfile:
            reader = PdfReader(inputfile)

        # return True if the file name input is correct
        return True

    except FileNotFoundError:
        exit("File does not exist.")

# a function to replicate an input PDF file and compress it
def compressing(filename):

    # create a fileobj to temporarily store the data
    writer = PdfWriter()
    with open(filename, "rb") as inputfile:
        reader = PdfReader(inputfile)
        for page in reader.pages:

            # compress the file page by page
            page.compress_content_streams()
            writer.add_page(page)

    with open(f"{filename.rstrip(".pdf")}_compressed.pdf", "wb") as outputfile:
        writer.write(outputfile)

# a function to replicate an input PDF file and rotate pages as needed
def rotating(filename, page_num=None, rt_angle=None):
    # specify the PDF page or pages to be rotated
    if page_num == None:
        rt_page = input("Specify the page number(s) for rotation -- each separated by a comma: ")
        rt_page = rt_page.strip()
    else:
        rt_page = page_num

    # sort the selected pages into a list and validate the integrity of page no. input
    if re.match(r"[\d, ]+$", rt_page):
        matches = re.findall(r"(\d*\d*\d)", rt_page)
    else:
        raise ValueError("Invalid input of characters")

    # ask the user to define the angle for rotation
    if rt_angle == None:
        instruct = """Please indicate the angle for rotation:
            press 'a' for clockwise 90 degrees,
            press 'b' for page(s) upside down,
            press 'c' for anti-clockwise 90 degrees
            """
        rt_option = input(instruct)
    else:
        rt_option = rt_angle

    degree = {"a": 90, "b": 180, "c": 270}
    if rt_option not in degree:
        raise ValueError("Invalid angle selection")

    # create fileobjects for reading & storing
    writer = PdfWriter()
    with open(filename, "rb") as inputfile:
        reader = PdfReader(inputfile)
        for match in matches:
            if int(match) < 1 or int(match) > len(reader.pages):
                raise ValueError("Invalid page number input")

        # copy pages from original to new file PLUS rotating the selected pages
        for i in range(len(reader.pages)):
            if str(i + 1) in matches:
                writer.add_page(reader.pages[i]).rotate(degree[rt_option])
            else:
                writer.add_page(reader.pages[i])

    # finally, put the content from fileobject to a targeted PDF file
    with open(f"{filename.rstrip('.pdf')}_rotated.pdf", "wb") as outputfile:
        writer.write(outputfile)

# a function to replicate an input PDF file and remove the undesired pages
def trimming(filename):
    # select, validate the page or pages to be deleted, then sort them to a list
    rm_page = input("Specify the page numbers for removal -- each separated by a comma: ")
    rm_page = rm_page.strip()
    if re.match(r"[\d, ]+$", rm_page):
        matches = re.findall(r"(\d*\d*\d)", rm_page)
    else:
        raise ValueError("Invalid input of characters")

    # loop the PDF pages from original and filter out the selected page for not being recorded
    writer = PdfWriter()
    with open(filename, "rb") as inputfile:
        reader = PdfReader(inputfile)

        for match in matches:
            if int(match) < 0 or int(match) > len(reader.pages):
                raise ValueError("Invalid page number input")

        for i in range(len(reader.pages)):
            if str(i + 1) not in matches:
                writer.add_page(reader.pages[i])

    with open(f"{filename.rstrip(".pdf")}_trimmed.pdf", "wb") as outputfile:
            writer.write(outputfile)

# finally, a function to output a PDF file by merging up to 5 original PDF original files
def merging(filename):
    # Allowed 2 to 5 PDF files to be merged
    file_qty = input("How many PDF files to be merged, max at 5? ")

    # Validator for correct input of no. for merging
    if int(file_qty) > 5 or int(file_qty) < 2:
        raise ValueError("Only 2 to 5 PDF files allowed")

    writer = PdfWriter()
    with open(filename, "rb") as inputfile:
        writer.append(inputfile)
        for i in range(int(file_qty) - 1):
            add_filename = input("Please enter the next file name to be merged: ")
            with open(add_filename, "rb") as topups:
                 writer.append(topups)

    with open(f"{filename.rstrip(".pdf")}_merged.pdf", "wb") as outputfile:
            writer.write(outputfile)

if __name__ == "__main__":
    main()
