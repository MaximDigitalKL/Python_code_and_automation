import unittest

from unittests.alerts_test import Alerts
from unittests.context_menu_test import Context_menu
from unittests.random_unit_tests import Tests1

import HtmlTestRunner

class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Context_menu),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Tests1)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = "Test Execution Report",
            report_name = "Test Results"
        )
        runner.run(tests_to_run)