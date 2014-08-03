import unittest
import lib.ast.traverse
from lib.ast.parser import Parser
from lib.ast.node_type import get_node_type_name



class TestTraverse(unittest.TestCase):
    def setUp(self):
        parser = Parser()
        self.ast = parser.parse_file('test/fixture/fixture_to_traverse.vim')

    def test_traverse(self):
        expected_order_of_visit = [
            'TOPLEVEL',
            'LET',
            'IDENTIFIER',
            'NUMBER',
            'WHILE',
            'ECHO',
            'STRING',
            'IDENTIFIER',
            'LET',
            'IDENTIFIER',
            'NUMBER',
            'SMALLER',
            'IDENTIFIER',
            'NUMBER',
            'ENDWHILE',
        ]

        actual_order_of_visit = []

        # Records visited node type name in order
        record_node_type_in_order = lambda node: actual_order_of_visit.append(
            get_node_type_name(node['type']))

        lib.ast.traverse.traverse(record_node_type_in_order, self.ast)

        self.assertEqual(actual_order_of_visit, expected_order_of_visit)


if __name__ == '__main__':
    unittest.main()
