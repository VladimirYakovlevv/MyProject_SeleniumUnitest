from pages.AllData import AllData
import time


class PassedInsurance(AllData):

    def passed_insurance(self):
        self.click_button_comprehensive_mandatory_insurance_claims_last3_years_no()
        time.sleep(1)
        self.click_button_had_negatives_last3_years_no()
        time.sleep(1)
        self.click_button_comprehensive_insurance_row_past_3years_no()
        time.sleep(1)
        self.click_button_for_offer()
        self.message(self)
