import pytest
from PyPDF2 import PdfWriter
import tempfile
import os
from pdfeditor import name_valid, compressing, rotating

# create a temporary PDF file for testing
def create_temp_pdf(filename, num_pages=1):
    writer = PdfWriter()
    for _ in range(num_pages):
        writer.add_blank_page(width=595, height=842)
    with open(filename, "wb") as f:
        writer.write(f)

# Fixture to set the ground to use temporary files for testing
@pytest.fixture
def temp_pdf_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_filename = temp_file.name
        create_temp_pdf(temp_filename)
    yield temp_filename
    try:
        os.remove(temp_filename)
    except OSError:
        pass

# tests for name_valid function, including special chars, extension correctness
def test_name_valid_extension():
    with pytest.raises(ValueError):
        name_valid("Sample.jpg")

def test_name_valid_invalid_chars():
    with pytest.raises(ValueError):
        name_valid("Sample## again.pdf")

# finally check on whether the PDF file actually exists
def test_name_valid_file_not_found():
    with pytest.raises(SystemExit):
        name_valid("invalid_demo.pdf")

# tests for compressing function
def test_compressing(temp_pdf_file):
    compressing(temp_pdf_file)
    compressed_filename = f"{temp_pdf_file.rstrip('.pdf')}_compressed.pdf"
    assert os.path.exists(compressed_filename)
    os.remove(compressed_filename)

# test for invalid input of page number or numbers
def test_rotating_invalid_page_number(temp_pdf_file):
    invalid_page_num = [0, 100]
    for page_num in invalid_page_num:
        with pytest.raises(ValueError):
            rotating(temp_pdf_file, page_num="page_numbers", rt_angle="90")

# test for invalid input of the rotating angle
def test_rotating_invalid_angle(temp_pdf_file):
    with pytest.raises(ValueError):
        rotating(temp_pdf_file, page_num="1", rt_angle="d")
