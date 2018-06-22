import unittest
import diskspace
import os
import subprocess
import re


class TestDiskSpaceMethods(unittest.TestCase):
    def test_subprocess_check_output(self):
        command = 'ls'
        check = subprocess.check_output(command)

        self.assertEqual(diskspace.subprocess_check_output(command), check)

    def test_bytes_to_readable(self):
        blocksB = 1
        blocksKb = 256
        blocksMb = 524288
        blocksGb = 1073741824

        self.assertEqual(diskspace.bytes_to_readable(blocksB), '512.00B')
        self.assertEqual(diskspace.bytes_to_readable(blocksKb), '128.00Kb')
        self.assertEqual(diskspace.bytes_to_readable(blocksMb), '256.00Mb')
        self.assertEqual(diskspace.bytes_to_readable(blocksGb), '512.00Gb')


if __name__ == '__main__':
    unittest.main()
