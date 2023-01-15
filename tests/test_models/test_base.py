import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_is_an_instance_of_base(self):
        test_n = Base()
        self.assertIsInstance(test_n, Base)

    def test_base_id(self):
        test_n = Base(2)
        self.assertEqual(test_n.id, 2)
        temp = Base()
        another = Base()
        self.assertEqual(another.id, 2)

    def test_wrong_id(self):
        test_n = Base("3")
        self.assertRaises(ValueError)

    def test_wrong_id_2(self):
        test_n = Base([3])
        self.assertRaises(ValueError)

class TestToJsonStringDict(unittest.TestCase):
    def test_to_json_string_valid_input(self):
        dic = [{1: 3, 2: 4}, {5: 6}]
        self.assertIsInstance(Base.to_json_string(dic), str)
        self.assertEqual(Base.to_json_string(dic), json.dumps(dic))
        self.assertEqual(Base.to_json_string(dic), '[{"1": 3, "2": 4}, {"5": 6}]')

    def test_to_json_string_invalid_input(self):
        dic_2 = None
        self.assertEqual(Base.to_json_string(dic_2), "[]")

    def test_to_json_string_empty_input(self):
        dic = []
        self.assertEqual(Base.to_json_string(dic), "[]")



class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        core = [{"am": 3}]
        test_subject = json.dumps(core)
        self.assertEqual(Base.from_json_string(test_subject), [{'am': 3}])
        self.assertEqual(Base.from_json_string(test_subject), json.loads(test_subject))

    def test_empty_list(self):
        test_subject = json.dumps([])
        self.assertEqual(Base.from_json_string(test_subject), [])
        self.assertEqual(Base.from_json_string(test_subject), json.loads(test_subject))
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_none_as_value(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_large_list(self):
        core = json.dumps([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}])
        expected_output = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(Base.from_json_string(core), expected_output)


class TestCreate(unittest.TestCase):
    def test_create_with_rectangle(self):
        a = Rectangle.create(id=0, width=3)
        self.assertIsInstance(a, Rectangle)
        self.assertEqual(a.id, 0)

    def test_create_with_square(self):
        test_value = Square(1, 2, 3, 4)
        dict_test = test_value.to_dictionary()
        new_value = Square.create(**dict_test)
        self.assertIsInstance(new_value, Square)
        self.assertEqual(new_value.to_dictionary(), test_value.to_dictionary())

if __name__ == '__main__':
    unittest.main()
