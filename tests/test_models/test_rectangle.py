import unittest
from models.rectangle import Rectangle
from models.base import Base
import json


class TestRectangleClassInstantiation(unittest.TestCase):

    def test_is_an_instance_of_Rectangle(self):
        est_ = Rectangle(2, 3, 4)
        self.assertIsInstance(est_, Rectangle)

    def test_is_a_subclass_of_base(self):
        test_1 = Rectangle(2, 3, 4)
        self.assertIsInstance(test_1, Base)


    def test_for_incorrect_no_of_parameters(self):
        self.assertRaises(TypeError, Rectangle, (4))
        self.assertRaises(TypeError, Rectangle, ())


class TestRectangleId(unittest.TestCase):
    def testa(self):
        rect = Rectangle(3, 4)
        rect_2 = Rectangle(3, 4, 5, 6)
        rect_3 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(rect.id, 13)
        self.assertEqual(rect_2.id, rect.id + 1)
        self.assertEqual(rect_3.id, 7)


class TestRectangleHeight(unittest.TestCase):
    def test_raise_value_error_for_wrong_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes = Rectangle(3, "9")

    def test_raise_value_error_for_wrong_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes = Rectangle(3, [5])

    def test_raise_value_error_for_wrong_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes = Rectangle(3, 4.5)

    def test_raise_value_error_for_wrong_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes = Rectangle(3, {"4": 5})

    def test_raise_value_error_for_wrong_height_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            tes = Rectangle(3, -5)

    def test_raise_value_error_for_wrong_height_is_0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            tes = Rectangle(3, 0)

    def test_height_setter(self):
        tes = Rectangle(1, 1)
        tes.height = 5
        self.assertEqual(5, tes.height)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes.height = "4"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tes.height = [4]
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            tes.height = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            tes.height = -5

    def test_height_getter(self):
        tes = Rectangle(3, 4)
        self.assertEqual(4, tes.height)
        tes.height = 7
        a = tes.height
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.height)

class TestRectangleWidth(unittest.TestCase):
    def test_raise_value_error_for_wrong_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Rectangle("4", 5)

    def test_raise_value_error_for_wrong_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Rectangle(["4"], 5)

    def test_raise_value_error_for_wrong_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Rectangle(4.5, 5)

    def test_raise_value_error_for_wrong_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes = Rectangle({"4": 5}, 5)

    def test_raise_value_error_for_wrong_width_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes = Rectangle(-5, 3)

    def test_raise_value_error_for_wrong_width_is_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes = Rectangle(0, 3)

    def test_width_setter(self):
        tes = Rectangle(1, 1)
        tes.width = 5
        self.assertEqual(5, tes.width)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes.width = "4"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tes.width = [4]
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tes.width = -5

    def test_width_getter(self):
        tes = Rectangle(3, 4)
        self.assertEqual(3, tes.width)
        tes.width = 7
        a = tes.width
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.width)


class TestRectangleX(unittest.TestCase):
    def test_raise_value_error_for_wrong_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Rectangle(3, 3, "4")

    def test_raise_value_error_for_wrong_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Rectangle(3, 3, ["4"])

    def test_raise_value_error_for_wrong_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Rectangle(3, 3, 4.5)

    def test_raise_value_error_for_wrong_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes = Rectangle(3, 3, {"4": 6})

    def test_raise_value_error_for_wrong_x_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            tess = Rectangle(3, 3, -5)

    def test_x_setter(self):
        tes = Rectangle(1, 1, 1)
        tes.x = 5
        self.assertEqual(5, tes.x)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes.x = "4"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tes.x = [4]
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            tes.x = -5

    def test_x_getter(self):
        tes = Rectangle(3, 3, 4)
        self.assertEqual(4, tes.x)
        tes.x = 7
        a = tes.x
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.x)


class TestRectangleY(unittest.TestCase):
    def test_raise_value_error_for_wrong_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Rectangle(3, 3, 3, "4")

    def test_raise_value_error_for_wrong_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Rectangle(3, 3, 3, ["4"])

    def test_raise_value_error_for_wrong_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Rectangle(3, 3, 3, 4.5)

    def test_raise_value_error_for_wrong_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tess = Rectangle(3, 3, 3, {"4": 5})

    def test_raise_value_error_for_wrong_y_less_than_0(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tess = Rectangle(3, 3, 3, -5)

    def test_y_setter(self):
        tes = Rectangle(1, 1, 1, 1)
        tes.y = 5
        self.assertEqual(5, tes.y)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tes.y = "4"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tes.y = [4]
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tes.y = -5

    def test_y_getter(self):
        tes = Rectangle(3, 3, 3, 4)
        self.assertEqual(4, tes.y)
        tes.y = 7
        a = tes.y
        self.assertEqual(a, 7)
        self.assertEqual(7, tes.y)


class TestRectangleArea(unittest.TestCase):

    def test_small_area(self):
        test = Rectangle(23, 2)
        self.assertEqual(test.area(), 46)

    def test_large_area(self):
        tes = Rectangle(12233344546556576768, 132904945639474937475975945)
        self.assertEqual(tes.area(), 1625871991949069013770655986710326739113845760)


class TestRectangleUpdateArgs(unittest.TestCase):

    def test_update_args_1(self):
        tes = Rectangle(1, 1)
        tes.update(5)
        self.assertEqual(tes.id, 5)

    def test_update_args_2(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)

    def test_update_args_3(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 5)

    def test_update_args_4(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5, 8)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 5)
        self.assertEqual(tes.x, 8)

    def test_update_args_5(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5, 8, 9)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 5)
        self.assertEqual(tes.x, 8)
        self.assertEqual(tes.y, 9)

    def test_update_args_error_in_1(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, "4", 5, 1, 2)
        self.assertEqual(tes.width, 1)

    def test_update_args_error_in_2_and_above(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, "4,", [5], {3:0}, 2)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 1)
        self.assertEqual(tes.height, 2)
        self.assertEqual(tes.x, 0)
        self.assertEqual(tes.y, 2)


class TestRectangleUpdateArgsAndKwargs(unittest.TestCase):

    def test_update_args_1_with_kwargs(self):
        tes = Rectangle(1, 1)
        tes.update(5, id=3)
        self.assertEqual(tes.id, 5)

    def test_update_kwargs_with_args_is_none(self):
        tes = Rectangle(1, 2, 3, 4, 6)
        self.assertEqual(tes.width, 1)
        tes.update(None, id=4, width=6)
        self.assertEqual(tes.id, 6)
        self.assertEqual(tes.width, 1)

    def test_kwargs_with_errors(self):
        tes = Rectangle(2, 3, 11, 12, 9)
        self.assertEqual(tes.width, 2)
        tes.update(width=6, height=10, id=4)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 10)

    def test_update_args_is_not_none_with_kwargs(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, 6, 5, width=7, id=2, height=10)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 5)

    def test_update_kwargs_with_wrong_key(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(width=6, id=4, height=5, x=8, mes=2)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 6)
        self.assertEqual(tes.height, 5)
        self.assertEqual(tes.x, 8)

    def test_update_kwargs_with_wrong_value(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(width="6", id=4, height=5, x=8, mes=2, y=9)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 1)
        self.assertEqual(tes.height, 5)
        self.assertEqual(tes.x, 8)
        self.assertEqual(tes.y, 9)

    def update_args_error_in_1(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, "4", 5, 1, 2)
        self.assertEqual(tes.width, 2)

    def update_args_error_in_2_and_above(self):
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        tes.update(4, "4,", [5], {3:0}, 2)
        self.assertEqual(tes.id, 4)
        self.assertEqual(tes.width, 2)
        self.assertEqual(tes.height, 2)
        self.assertEqual(tes.x, 0)
        self.assertEqual(tes.y, 2)


class TestToDictionary(unittest.TestCase):

    def test_dict_repr(self):
        tes = Rectangle(4, 5, 0, 0, 4)
        ess = tes.to_dictionary()
        self.assertEqual(ess, tes.to_dictionary())
        self.assertDictContainsSubset({"width": 4}, tes.to_dictionary())
        self.assertEqual(ess["id"], tes.id)


class TestToJsonStringDict(unittest.TestCase):
    def test_to_json_string_valid_input(self):
        dic = [{1: 3, 2: 4}, {5: 6}]
        self.assertIsInstance(Rectangle.to_json_string(dic), str)
        self.assertEqual(Rectangle.to_json_string(dic), json.dumps(dic))
        self.assertEqual(Rectangle.to_json_string(dic), '[{"1": 3, "2": 4}, {"5": 6}]')

    def test_to_json_string_invalid_input(self):
        dic_2 = None
        self.assertEqual(Rectangle.to_json_string(dic_2), "[]")

    def test_to_json_string_empty_input(self):
        dic = []
        self.assertEqual(Rectangle.to_json_string(dic), "[]")


class TestSaveToJson(unittest.TestCase):
    def test_valid_input(self):
        test_list = [Rectangle(10, 7, 2, 8, 1), Rectangle(1, 2, 3, 4, 5)]
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(),
                             '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                            '{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
                             )

    def test_the_dict_result(self):
        test_list = [Rectangle(10, 7, 2, 8, 1), Rectangle(1, 2, 3, 4, 5)]
        Rectangle.save_to_file(test_list)
        outcome = []
        with open("Rectangle.json", 'r') as ft:
            outcome = json.load(ft)
        self.assertEqual(test_list[0].to_dictionary(), outcome[0])

    def test_empty_list(self):
        test_list = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')

    def test_empty_list_as_object(self):
        test_list = []
        outcome = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(json.load(ft), [])

    def test_none_as_value(self):
        test_list = None
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')

    def test_none_list_result__empty_list__(self):
        test_list = None
        outcome = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(json.load(ft), [])

class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        core = [{"am": 3}]
        test_subject = json.dumps(core)
        self.assertEqual(Rectangle.from_json_string(test_subject), [{'am': 3}])
        self.assertEqual(Rectangle.from_json_string(test_subject), json.loads(test_subject))

    def test_empty_list(self):
        test_subject = json.dumps([])
        self.assertEqual(Rectangle.from_json_string(test_subject), [])
        self.assertEqual(Rectangle.from_json_string(test_subject), json.loads(test_subject))
        self.assertEqual(Rectangle.from_json_string('[]'), [])

    def test_none_as_value(self):
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_large_list(self):
        core = json.dumps([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}])
        expected_output = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                            {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(Rectangle.from_json_string(core), expected_output)

if __name__ == '__main__':
    unittest.main()
