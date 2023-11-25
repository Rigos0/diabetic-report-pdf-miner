from diabetic_report_pdf_miner.report_miner import *
from diabetic_report_pdf_miner.labels import *
from diabetic_report_pdf_miner.string_utils import *

class Medtronic(PDFReader):

    @staticmethod
    def convert_pdf_to_image(pdf_path):
        return convert_from_path(pdf_path)







    def load_sensor_range_data(self):
        page_index = 0
        elements_list = self.extract_elements_from_nth_page(page_index)

        for e in elements_list:
            if not isinstance(e, LTTextContainer):
                continue

            print(e.get_text())

    def load_sp_ci_data(self):
        """
        Loads the two required values of prumerny sacharidovy pomer and citlivost na inzulin
        :return:
        """
        # find the page index that contains the required data
        text_in_the_required_page = "Sacharidový poměr"
        page_index = self.find_page_index_by_text(text_in_the_required_page)

        elements_list = self.extract_elements_from_nth_page(page_index)

        print(self.based_on_previous_float(elements_list, regex_pattern=r'Citlivost'))

        print(self.based_on_previous_float(elements_list, regex_pattern=r'Poměr'))

        #TODO: implement the logic


class MedtronicMissingComparison(Medtronic):
    def load_sensor_insulin_data(self):
        page_number = 0
        elements_list = self.extract_elements_from_nth_page(page_number)
        # skip one element that contains ±
        self.skip_elements(elements_list, regex_pattern=CONTAINS_PLUSMINUS_SIGN, n=1)

        glukoza_a_odchylka = self.find_first_occurrence(elements_list, regex_pattern=CONTAINS_PLUSMINUS_SIGN)
        self.data[PRUMERNA_GLUKOZA], self.data[GLUKOZA_S_ODCHYLKA] = split_string_two_floats(glukoza_a_odchylka)

        self.data[GMI] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN)

        self.data[GLUKOZA_K_VARIACE] = (self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN))

        self.data[CDDI] = (self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_JEDN))

        self.data[BOLUS] = (self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN))

        self.skip_elements(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN, n=1)

        self.data[BAZAL] = (self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN))

        #TODO: doptat se na formát
        doba_aktiv_inzulinu = (
            self.find_first_occurrence(elements_list, regex_pattern=CONTAINS_LETTER_H_AND_DOUBLE_DOT))
        self.data[DOBA_AKTIV_INZULINU] = doba_aktiv_inzulinu


class MedtronicFull(Medtronic):
    def load_sensor_insulin_data(self):
        page_number = 0
        elements_list = self.extract_elements_from_nth_page(page_number)
        # skip one element that contains ±
        self.skip_elements(elements_list, regex_pattern=CONTAINS_PLUSMINUS_SIGN, n=1)

        glukoza_a_odchylka = self.find_first_occurrence(elements_list, regex_pattern=CONTAINS_PLUSMINUS_SIGN)
        self.data[PRUMERNA_GLUKOZA], self.data[GLUKOZA_S_ODCHYLKA] = split_string_two_floats(glukoza_a_odchylka)

        self.skip_elements(elements_list, regex_pattern=CONTAINS_PLUSMINUS_SIGN, n=1)
        self.data[GMI] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN)

        self.skip_elements(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN, n=1)
        self.data[GLUKOZA_K_VARIACE] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN)

        self.data[CDDI] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_JEDN)

        self.data[BOLUS] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN)

        self.skip_elements(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN, n=3)

        self.data[BAZAL] = self.first_occurrence_float(elements_list, regex_pattern=CONTAINS_PERCENTAGE_SIGN)

        #TODO: doptat se na formát
        doba_aktiv_inzulinu = (
            self.find_first_occurrence(elements_list, regex_pattern=CONTAINS_LETTER_H_AND_DOUBLE_DOT))
        self.data[DOBA_AKTIV_INZULINU] = doba_aktiv_inzulinu

    def load_sensor_in_range_params(self):
        pass