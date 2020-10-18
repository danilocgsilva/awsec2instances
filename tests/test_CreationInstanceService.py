import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.CreationInstanceService import CreationInstanceService

class test_CreationInstanceService(unittest.TestCase):

    def setUp(self):
        self.creationalService = CreationInstanceService()

    def test_ensureMinutesData_arbitrary(self):
        self.creationalService.ensureMinutesData("234")
        self.assertEqual(
            234,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_arbitrary_2(self):
        self.creationalService.ensureMinutesData("66")
        self.assertEqual(
            66,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_tenminutes(self):
        self.creationalService.ensureMinutesData("for-ten-minutes")
        self.assertEqual(
            10,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_onehour(self):
        self.creationalService.ensureMinutesData("for-an-hour")
        self.assertEqual(
            60,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_day(self):
        self.creationalService.ensureMinutesData("for-a-day")
        self.assertEqual(
            1440,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_week(self):
        self.creationalService.ensureMinutesData("for-an-week")
        self.assertEqual(
            10080,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_month(self):
        self.creationalService.ensureMinutesData("for-a-month")
        self.assertEqual(
            43200,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_year(self):
        self.creationalService.ensureMinutesData("for-an-year")
        self.assertEqual(
            525600,
            self.creationalService.die_time
        )
    
    def test_ensureMinutesData_forever(self):
        self.creationalService.ensureMinutesData("forever")
        self.assertEqual(
            2102424,
            self.creationalService.die_time
        )

    def test_ensureMinutesData_wrongvalue(self):
        with self.assertRaises(Exception):
            self.creationalService.ensureMinutesData("not_existing")        

