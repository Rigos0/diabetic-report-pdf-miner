from diabetic_report_pdf_miner.readers.medtronic import MedtronicFull, MedtronicMissingComparison
from diabetic_report_pdf_miner.readers.dexcom import Dexcom


from typing import Dict, List
from pdfminer.high_level import extract_text


def first_page_text(path_to_pdf: str) -> str:
    """
    Extracts the text from the first page of a PDF file.

    Parameters:
    path_to_pdf (str): The path to the PDF file.

    Returns:
    str: The extracted text.
    """
    # Extract text from the first page of the PDF
    text = extract_text(path_to_pdf, page_numbers=[0])

    return text


def analyze_pdf(path_to_pdf: str) -> Dict:
    """
    :param path_to_pdf: Path to pdf to analyze
    :return: Dict of results
    """

    text = first_page_text(path_to_pdf)
    if "AGP report" in text:
        report_type = "LibreView"
        raise NotImplementedError("Pipeline for LibreView reports not implemented.")

    elif "Glooko" in text:
        report_type = "Glooko"
        raise NotImplementedError("Pipeline for Glooko reports not implemented.")

    elif "Dexcom" in text:
        report_type = "Dexcom"
        raise NotImplementedError("Pipeline for Dexcom reports not implemented.")

    elif "Porovnání percentilů" in text:
        report_type = "Medtronic"
        reader = MedtronicFull(path_to_pdf)

    else:
        raise ValueError("Record type not recognised.")

    reader.load_all_data()

    return reader.data


if __name__ == "__main__":
    path_to_reports = "C:/Users/z004vpye/Documents/Projects/hackathon_data/sorted/glooko/"
    report_filename = "0a3e6b77-8636-4026-a18e-ddb0dcdb9938.pdf"

    gustav = "Gustav-Křivinka-16.11.2023.pdf"

    path = path_to_reports + report_filename

    analyze_pdf(path_to_pdf=path)
    medtronic = MedtronicFull(path)

    for e in medtronic.extract_elements_from_nth_page(0):
        print(e)

    # """Finished"""
    # medtronic.load_sensor_insulin_data()
    # medtronic.load_sp_ci_data()
    #
    # """TODO"""
    # # medtronic.load_sensor_range_data()
    #
    # medtronic.display_data()

