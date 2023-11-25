# Diabetic Report PDF Miner

## Overview

The Diabetic Report PDF Miner is a Python library designed for extracting specific information from diabetic reports in PDF format. The library utilizes the `pdfminer` package for PDF parsing and provides a set of classes and methods to extract relevant data.

## Installation

To use the Diabetic Report PDF Miner, you need to have Python installed on your system. Additionally, you can install the required dependencies by running the following command:

```bash
pip install pdfminer
```

## Usage
```python
from diabetic_report_pdf_miner.analyze import analyze_pdf
from diabetic_report_pdf_miner.handle_result import display_data

filename = "<path_to_your_file>"

# Analyze the PDF and display the extracted data
extracted_data = analyze_pdf(filename)
display_data(extracted_data)
```


## Example of pdf miner workflow of reading a PDF
![image](https://github.com/Rigos0/diabetic-report-pdf-miner/assets/47658855/78d4c4c2-a674-4cb3-b10c-fa945ca303f7)
