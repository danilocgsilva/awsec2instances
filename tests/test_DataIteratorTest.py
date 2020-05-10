from testsAssets.get_mocked_raw_data import get_mocked_raw_data
from awsec2instances_includes.fn import getRawDataFromCli
from awsec2instances_includes.DataIterator import DataIterator
import unittest


class DataIteratorTest(unittest.TestCase):

    def test_getting_all_instanes(self):
        instances = get_mocked_raw_data()

        di = DataIterator()
        instanceInfos = di.getInstancesInfos(instances)

        self.assertEqual(2, len(instanceInfos))


    def test_filter_stopped_instances(self):
        instances = get_mocked_raw_data()

        di = DataIterator()
        di.set_allow_stopped(False)
        instanceInfos = di.getInstancesInfos(instances)

        self.assertEqual(1, len(instanceInfos))


if __name__ == '__main__':
    unittest.main()
