import unittest
from demographic_data_analyzer import demographic_data_analyzer

class TestDemographicDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.results = demographic_data_analyzer()

    def test_race_count(self):
        self.assertIsInstance(self.results['race_count'], pd.Series)

    def test_average_age_men(self):
        self.assertIsInstance(self.results['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertIsInstance(self.results['percentage_bachelors'], float)

    def test_percentage_advanced_education_rich(self):
        self.assertIsInstance(self.results['percentage_advanced_education_rich'], float)

    def test_percentage_non_advanced_education_rich(self):
        self.assertIsInstance(self.results['percentage_non_advanced_education_rich'], float)

    def test_min_work_hours(self):
        self.assertIsInstance(self.results['min_work_hours'], int)

    def test_percentage_rich_min_workers(self):
        self.assertIsInstance(self.results['percentage_rich_min_workers'], float)

    def test_highest_earning_country(self):
        self.assertIsInstance(self.results['highest_earning_country'], str)

    def test_highest_earning_country_percentage(self):
        self.assertIsInstance(self.results['highest_earning_country_percentage'], float)

    def test_top_IN_occupation(self):
        self.assertIsInstance(self.results['top_IN_occupation'], str)

if __name__ == "__main__":
    unittest.main()
