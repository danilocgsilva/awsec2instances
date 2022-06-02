import unittest
from awsec2instances_includes.OsFamily import OsFamily

class test_OsFamily(unittest.TestCase):

    def setUp(self):
        self.os_family = OsFamily()

    def test_is_debian_family_true(self):
        distro = "ubuntu"
        self.assertTrue(self.os_family.is_debian_family(distro))

    def test_is_debian_family_false(self):
        distro = "abc123"
        self.assertFalse(self.os_family.is_debian_family(distro))

    def test_is_ubuntu_family_true(self):
        distro = "ubuntu"
        self.assertTrue(self.os_family.is_ubuntu_family(distro))

    def test_is_ubuntu_family_false(self):
        distro = "abc123"
        self.assertFalse(self.os_family.is_ubuntu_family(distro))

    def test_is_ubuntu_family_true_2(self):
        distro = "ubuntu-20.04"
        self.assertTrue(self.os_family.is_ubuntu_family(distro))

    def test_is_debian_family_true_2(self):
        distro = "ubuntu-20.04"
        self.assertTrue(self.os_family.is_ubuntu_family(distro))

    

