import unittest
import diskspace
import os
import subprocess
import re
import sys
import StringIO

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

    def testPrintTree(self):
        path = '/home/Documentos'
        total_size = 2
        file_tree_node = {'print_size': '100.00Kb',
                               'children': [], 'size': total_size}
        file_tree = {path: file_tree_node}
        largest_size = 4
        captured = StringIO.StringIO()
        sys.stdout = captured

        diskspace.print_tree(file_tree, file_tree_node, path,
                             largest_size, total_size)

        result = "100.00Kb  100%  {}\n".format(path)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, captured.getvalue())


if __name__ == '__main__':
    unittest.main()
