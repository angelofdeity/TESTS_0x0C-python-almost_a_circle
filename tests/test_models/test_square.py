import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import json


class TestSquareClassInstantiation(unittest.TestCase):

    def test_is_an_instance_of_Square(self):
        est_ = Square(2, 3, 4)
        self.assertIsInstance(est_, Square)

    def test_is_a_subclass_of_base(self):
        test_1 = Square(2, 3, 4)
        self.assertIsInstance(test_1, Base)
    def test_is_a_subclass_of_rectangle(self):
        test_1 = Square(2, 3, 4)
        self.assertIsInstance(test_1, Rectangle)


    def test_for_incorrect_no_of_parameters(self):
        self.assertRaises(TypeError, Square, ())


class TestSquareId(unittest.TestCase):
    def testa(self):
        remo = Square(2)
        rect = Square(3, 4)
        rect_2 = Square(3, 4, 5)
        rect_3 = Square(3, 4, 5, 6)
        self.assertEqual(remo.id, 6)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect_2.id, rect.id + 1)
        self.assertEqual(rect_3.id, 6)

class TestSquareSize(unittest.TestCase):
    def test_raise_value_error_for_wrong_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Square("9")

    def test_raise_value_error_for_wrong_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Square([5])

    def test_raise_value_error_for_wrong_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Square(4.5)

    def test_raise_value_error_for_wrong_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Square({"4": 5})

    def test_raise_value_error_for_wrong_size_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes = Square(-5)

    def test_raise_value_error_for_wrong_size_is_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes = Square(0)

    def test_size_setter(self):
        tes = Square(1)
        tes.size = 5
        self.assertEqual(5, tes.size)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes.size = "4"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes.size = [4]
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes.size = -5

    def test_size_getter(self):
        tes = Square(4)
        self.assertEqual(4, tes.size)
        tes.size = 7
        a = tes.size
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.size)


class TestSquareX(unittest.TestCase):
    def test_raise_value_error_for_wrong_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Square(3, "4")

    def test_raise_value_error_for_wrong_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Square(3, ["4"])

    def test_raise_value_error_for_wrong_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Square(3, 4.5)

    def test_raise_value_error_for_wrong_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Square(3, {"4": 6})

    def test_raise_value_error_for_wrong_x_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            tess = Square(3, -5)

    def test_x_setter(self):
        tes = Square(1, 1)
        tes.x = 5
        self.assertEqual(5, tes.x)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes.x = "4"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes.x = [4]
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            tes.x = -5

    def test_x_getter(self):
        tes = Square(3, 4)
        self.assertEqual(4, tes.x)
        tes.x = 7
        a = tes.x
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.x)


class TestSquareY(unittest.TestCase):
    def test_raise_value_error_for_wrong_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Square(3, 3, "4")

    def test_raise_value_error_for_wrong_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Square(3, 3, ["4"])

    def test_raise_value_error_for_wrong_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Square(3, 3, 4.5)

    def test_raise_value_error_for_wrong_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Square(3, 3, {"4": 5})

    def test_raise_value_error_for_wrong_y_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tess = Square(3, 3, -5)

    def test_y_setter(self):
        tes = Square(1, 1, 1)
        tes.y = 5
        self.assertEqual(5, tes.y)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tes.y = "4"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tes.y = [4]
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tes.y = -5

    def test_y_getter(self):
        tes = Square(3, 3, 4)
        self.assertEqual(4, tes.y)
        tes.y = 7
        a = tes.y
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.y)

class TestSquareArea(unittest.TestCase):

    def test_small_area(self):
        test = Square(13, 2)
        self.assertEqual(test.area(), 169)

    def test_large_area(self):
        tes = Square(12233344546556576768556)
        self.assertEqual(tes.area(), 149654718794765536868399471490448239190325136)

class TestSquareUpdateArgs(unittest.TestCase):

    def test_update_args_1(self):
        tes = Square(1, 1)
        tes.update(5)
        self.assertEqual(tes.id, 5)

    def test_update_args_2(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)

    def test_update_args_3(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 6)
        self.assertEqual(tes.x, 5)

    def test_update_args_4(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5, 8)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 6)
        self.assertEqual(tes.x, 5)
        self.assertEqual(tes.y, 8)

    def test_update_args_error_in_1(self):
        tes = Square(1, 2)
        self.assertEqual(tes.size, 1)
        tes.update(4, "4", 5, 1, 2)
        self.assertEqual(tes.size, 1)

    def test_update_args_error_in_2_and_above(self):
        tes = Square(1, 2)
        self.assertEqual(tes.size, 1)
        tes.update(4, "4,", [5], {3:0})
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 1)
        self.assertEqual(tes.x, 2)
        self.assertEqual(tes.y, 0)

class TestSquareUpdateArgsAndKwargs(unittest.TestCase):

    def test_update_args_1_with_kwargs(self):
        tes = Square(1, 1)
        tes.update(5, id=3)
        self.assertEqual(tes.id, 5)

    def test_update_kwargs_with_args_is_none(self):
        tes = Square(1, 2, 3, 4)
        self.assertEqual(tes.size, 1)
        tes.update(None, id=6, size=6)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 1)

    def test_kwargs_with_errors(self):
        tes = Square(2, 3, 11, 12)
        self.assertEqual(tes.size, 2)
        tes.update(x=6, size=10, id=4)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.x, 6)
        self.assertEqual(tes.size, 10)

    def test_update_args_is_not_none_with_kwargs(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5, y=7, id=2, size=10)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.x, 5)

    def test_update_kwargs_with_wrong_key(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(size=6, id=4, y=5, x=8, mes=2)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 6)
        self.assertEqual(tes.y, 5)
        self.assertEqual(tes.x, 8)

    def test_update_kwargs_with_wrong_value(self):
        tes = Square(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(id=4, size='5', x=8, mes=2, y=9)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.size, 1)
        self.assertEqual(tes.x, 8)
        self.assertEqual(tes.y, 9)

class TestToDictionary(unittest.TestCase):
    def test_dict_repr(self):
        tes = Square(4, 5, 0, 5)
        ess = tes.to_dictionary()
        self.assertEqual(ess, tes.to_dictionary())
        self.assertDictContainsSubset({"size": 4}, tes.to_dictionary())
        self.assertEqual(ess["id"], tes.id)

class TestToJsonStringDict(unittest.TestCase):
    def test_to_json_string_valid_input(self):
        dic = [{1: 3, 2: 4}, {5: 6}]
        self.assertIsInstance(Square.to_json_string(dic), str)
        self.assertEqual(Square.to_json_string(dic), json.dumps(dic))
        self.assertEqual(Square.to_json_string(dic), '[{"1": 3, "2": 4}, {"5": 6}]')

    def test_to_json_string_invalid_input(self):
        dic_2 = None
        self.assertEqual(Square.to_json_string(dic_2), "[]")

    def test_to_json_string_empty_input(self):
        dic = []
        self.assertEqual(Square.to_json_string(dic), "[]")


class TestSaveToJson(unittest.TestCase):
    def test_valid_input(self):
        test_list = [Square(7, 2, 8, 1), Square(2, 3, 4, 5)]
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(),
                             '[{"id": 1, "size": 7, "x": 2, "y": 8}, '
                            '{"id": 5, "size": 2, "x": 3, "y": 4}]'
                             )

    def test_the_dict_result(self):
        test_list = [Square(7, 2, 8, 1), Square(2, 3, 4, 5)]
        Square.save_to_file(test_list)
        outcome = []
        with open("Square.json", 'r') as ft:
            outcome = json.load(ft)
        self.assertEqual(test_list[0].to_dictionary(), outcome[0])

    def test_empty_list(self):
        test_list = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')

    def test_empty_list_as_object(self):
        test_list = []
        outcome = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(json.load(ft), [])

    def test_none_as_value(self):
        test_list = None
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')

    def test_none_list_result__empty_list__(self):
        test_list = None
        outcome = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(json.load(ft), [])

class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        core = [{"am": 3}]
        test_subject = json.dumps(core)
        self.assertEqual(Square.from_json_string(test_subject), [{'am': 3}])
        self.assertEqual(Square.from_json_string(test_subject), json.loads(test_subject))

    def test_empty_list(self):
        test_subject = json.dumps([])
        self.assertEqual(Square.from_json_string(test_subject), [])
        self.assertEqual(Square.from_json_string(test_subject), json.loads(test_subject))
        self.assertEqual(Square.from_json_string('[]'), [])

    def test_none_as_value(self):
        self.assertEqual(Square.from_json_string(None), [])

    def test_large_list(self):
        core = json.dumps([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}])
        expected_output = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(Square.from_json_string(core), expected_output)

# class TestClassMethods(unittest.TestCase):
#     def test_to_json_string(self):
#         dic = [{1: 3, 2: 4}, {5: 6}]
#         self.assertIsInstance(Square.to_json_string(dic), str)
#         self.assertEqual(Square.to_json_string(None), "[]")
#         self.assertEqual(Square.to_json_string(dic), '[{"1": 3, "2": 4}, {"5": 6}]')
#
#     def test_save_to_file(self):
#         ad = [Square(4, 5, 0, 5), Square(1, 2, 3, 3)]
#         Square.save_to_file(ad)
#         c = [ad[0].to_dictionary(), ad[1].to_dictionary()]
#         a = Square.to_json_string(c)
#         with open("Square.json", 'r') as s:
#             self.assertEqual(a, s.read())
#
#     def test_rewritten_file(self):
#         am = [Square(4, 5, 0, 7), Square(1, 2, 3, 3)]
#         Square.save_to_file(am)
#         ca = [am[0].to_dictionary(), am[1].to_dictionary()]
#         aa = Square.to_json_string(ca)
#         with open("Square.json", 'r') as s:
#             self.assertEqual(aa, s.read())
#
#     def test_from_json_string(self):
#         a = '[{"1": 3, "2": 4}]'
#         self.assertEqual(Base.from_json_string(a), [{'1': 3, '2': 4}])
#
#     def test_with_json_decoded(self):
#         ca = Base.to_json_string([{1: 3, 2: 4}])
#         self.assertEqual(Base.from_json_string(ca), [{'1': 3, '2': 4}])
#
#     def test_create(self):
#         a = Square.create(size=4, id=3)
#         self.assertIsInstance(a, Square)
#         self.assertEqual(a.id, 3)
#
#     def test_dummy_create(self):
#         a = Square.create()
#         self.assertEqual(a.size, 1)
#
#     def test_load_from_file(self):

if __name__ == '__main__':
    unittest.main()
