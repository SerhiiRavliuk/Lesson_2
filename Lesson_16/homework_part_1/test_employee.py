from assertpy import assert_that

from Lesson_30.employee import TeamLead


class TestEmployee:
    qa_automation_team_lead : TeamLead = TeamLead('Serhii',4200,'Test',5)

    expected_mark_attrs : dict [str,object]={
        'name' : 'Serhii',
        'salary' : 4200,
        'department' : 'Test',
        'team_size' : 5
    }

    failed_mark_attrs: dict[str, object] = {
        'name': 'Serhii',
        'salary': 4200,
        'department': 'Test',
        'team_size': 7
    }

    def test_employee_attrs_positive(self):

        (assert_that(self.qa_automation_team_lead.__dict__,"Desired user's attrs aren't equal to desired dict of attrs")
         .is_equal_to(self.expected_mark_attrs))


    def test_employee_attrs_negative(self):
        (assert_that(self.qa_automation_team_lead.__dict__,
                     "Desired user's attrs are equal to desired dict of attrs")
         .is_equal_to(self.failed_mark_attrs))

