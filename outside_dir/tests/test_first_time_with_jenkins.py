
from assertpy import assert_that


class TestFirstTimeWithJenkins:

    def test_with_jenkins(self):
        greeting = "Hello, Jenkins!"

        assert_that(greeting).starts_with("Hello")
        assert_that(greeting).ends_with("Jenkins!")
        assert len(greeting) == 15

