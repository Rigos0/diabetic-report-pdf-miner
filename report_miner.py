from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams, LTTextBox, LTRect
from pdfminer.layout import LTTextContainer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import resolve1
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from io import StringIO

from diabetic_report_pdf_miner.labels import *
from diabetic_report_pdf_miner.string_utils import *


class PDFReader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.data = {} # will store the found data
        # self.pages_elements = [] # list of lists. Every page contains all elements

    def extract_elements_from_nth_page(self, page_index):
        laparams = LAParams(detect_vertical=True)  # Enable vertical text detection
        elements = []
        for i, page_layout in enumerate(extract_pages(self.pdf_path, laparams=laparams)):
            if i == page_index:  # Pages are 0-indexed
                for element in page_layout:
                    elements.append(element)
                break  # No need to process further pages
        return elements

    def number_of_pages(self) -> int:
        """
        Finds number of pages in the pdf
        :return: number of pages in the pdf
        """
        with open(self.pdf_path, 'rb') as file:
            parser = PDFParser(file)
            document = PDFDocument(parser)
            return resolve1(document.catalog['Pages'])['Count']

    def find_page_index_by_text(self, text_to_search: str) -> int:
        """
        Finds the page index of the given text in the pdf
        :param text_to_search: text to search in the pdf
        :return: page index of the found text in the pdf
        """
        for page_number, page in enumerate(extract_pages(self.pdf_path)):
            for element in page:
                if isinstance(element, LTTextContainer):
                    if text_to_search in element.get_text():
                        return page_number
        return -1  # return -1 if the text was not found

    def read_pdf(self):
        raise NotImplementedError("Subclass must implement this method")

    def display_data(self):
        print("Načtená data: ")
        for popisek, hodnota in self.data.items():
            print(f"{popisek}: {hodnota}")

    @staticmethod
    def skip_elements(elements_list: list, regex_pattern: str, n=1):
        """
        Deletes first x elements from elements list until it finds the required amount of elements
        that match the regex (it also deletes the elements that match the regex)
        :param elements_list: list of all elements
        :param regex_pattern:
        :param n: how many occurrences of the pattern to "skip"
        :return: shorter list of elements
        """
        elements_to_delete = []

        for element in elements_list:
            if n == 0:
                # Delete elements_to_delete from the original elements_list
                for elem in elements_to_delete:
                    elements_list.remove(elem)
                return

            if not isinstance(element, LTTextBox):
                continue

            text = element.get_text()
            if re.search(regex_pattern, text):
                n -= 1

            elements_to_delete.append(element)

        # return element list without elements to delete (delete them from the start)
        raise ValueError("Did not find sufficient amount of elements to skip.")

    @staticmethod
    def find_first_occurrence(elements_list: list, regex_pattern: str) -> str:
        """
        Finds and returns first occurrence of regex pattern in the element list.
        :param elements_list: list of all elements
        :param regex_pattern:
        :return: tuple containing the text of the element and the rest of the elements
        """
        for i, element in enumerate(elements_list):
            if not isinstance(element, LTTextBox):
                continue

            text = element.get_text()
            if re.search(regex_pattern, text):
                elements_list[:] = elements_list[i + 1:]
                return text

        raise ValueError(f"No such element found on the page: {regex_pattern}")

    @staticmethod
    def find_element_based_on_previous(elements_list: list, regex_pattern: str) -> str:
        """
        Finds and returns first text from element based on previously occurring element.
        :param elements_list: list of all elements
        :param regex_pattern:
        :return: tuple containing the text of the element and the rest of the elements
        """
        for i, element in enumerate(elements_list):
            if not isinstance(element, LTTextBox):
                continue

            text = element.get_text()
            if re.search(regex_pattern, text): # we found the correct baseline element
                text_of_next = elements_list[i+1].get_text()
                elements_list[:] = elements_list[i + 2:] # we need to skip two elems from here
                return text_of_next

        raise ValueError("No such baseline element found on the page.")

    def first_occurrence_float(self, elements_list, regex_pattern) -> str:
        """
        Helper function that combines text extraction from element and float extraction from the string.
        :param elements_list:
        :param regex_pattern:
        :return:
        """
        extracted_text = self.find_first_occurrence(elements_list, regex_pattern=regex_pattern)
        float_as_str = extract_float_as_str(extracted_text)

        return float_as_str

    def based_on_previous_float(self, elements_list, regex_pattern) -> str:
        """
         Helper function that combines text extraction from next element from given element
          and float extraction from the string.
         :param elements_list:
         :param regex_pattern:
         :return:
         """
        extracted_text = self.find_element_based_on_previous(elements_list, regex_pattern=regex_pattern)
        float_as_str = extract_float_as_str(extracted_text)

        return float_as_str
