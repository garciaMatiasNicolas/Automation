from pages.ConsultRiskData import ConsultPage


class TestScenarioReadData:

    def test_login(self, driver):
        consult_open_case = ConsultPage(case_type="open", opt_reason="FRDNI", driver=driver)
        consult_open_case.search_risk_data()
