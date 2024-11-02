import allure
import logging
from assertpy import assert_that
from Lesson_30.employee import TeamLead

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestEmployee:
    qa_automation_team_lead: TeamLead = TeamLead('Serhii', 4200, 'Test', 5)

    expected_mark_attrs: dict[str, object] = {
        'name': 'Serhii',
        'salary': 4200,
        'department': 'Test',
        'team_size': 5
    }

    failed_mark_attrs: dict[str, object] = {
        'name': 'Serhii',
        'salary': 4200,
        'department': 'Test',
        'team_size': 7
    }

    @allure.story('Test Allure')
    @allure.title('Positive Test for Employee Attributes')
    def test_employee_attrs_positive(self):
        with allure.step("Starting positive test for employee attributes"):
            logger.info("Starting positive test for employee attributes")
            logger.info(f"Expected attributes: {self.expected_mark_attrs}")
            logger.info(f"Actual attributes: {self.qa_automation_team_lead.__dict__}")

            logger.info("Comparing actual attributes with expected attributes")
            assert_that(self.qa_automation_team_lead.__dict__,
                        "Desired user's attrs aren't equal to desired dict of attrs").is_equal_to(
                self.expected_mark_attrs)
            logger.info("Positive test completed successfully")

    @allure.story('Test Allure')
    @allure.title('Negative Test for Employee Attributes')
    def test_employee_attrs_negative(self):
        with allure.step("Starting negative test for employee attributes"):
            logger.info("Starting negative test for employee attributes")
            logger.info(f"Expected attributes: {self.failed_mark_attrs}")
            logger.info(f"Actual attributes: {self.qa_automation_team_lead.__dict__}")

            logger.info("Comparing actual attributes with expected attributes")
            assert_that(self.qa_automation_team_lead.__dict__,
                        "Desired user's attrs are equal to desired dict of attrs").is_equal_to(self.failed_mark_attrs)
            logger.info("Negative test completed. This test should fail if attributes are equal.")
