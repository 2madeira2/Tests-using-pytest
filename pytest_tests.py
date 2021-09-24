import pytest


class TestString:

    # параметризованный тест

    @pytest.mark.parametrize('string', ['string', '\nstring', 'string\n', '\nstring\n', ' string '])
    def test_strip(self, string):
        assert string.strip() == 'string'

    # негативный тест

    def test_string_index_out_of_range(self):
        s = "abcd"
        try:
            assert s[len(s)]
        except IndexError:
            pass

    def test_lower(self):
        string = 'StrING'
        assert string.lower() == 'string'

    def test_concat(self):
        str1 = 'first'
        str2 = 'second'
        assert str1 + str2 == 'firstsecond'

    def test_mult(self):
        string = 'word'
        assert string * 3 == 'wordwordword'


class TestFloat:

    # параметризованный тест метода float.is_integer(), который должен вернуть True, если значение является целым

    @pytest.mark.parametrize('value, result', [(2.0, True), (3.4, False), (7.453535, False)])
    def test_float_is_integer(self, value, result):
        assert float.is_integer(value) == result

    # негативный тест - float не поддерживает длинную арифметику

    def test_too_large_to_float(self):
        a = 3 ** 1000
        try:
            assert a + 0.1
        except OverflowError:
            pass

    # float.as_integer_ratio() возвращает tuple пару целых чисел, чьё отношение равно этому числу.

    def test_float_as_integer_ratio(self):
        assert 3.5.as_integer_ratio() == (7, 2)

    # round - округляет до целого

    def test_round(self):
        assert round(137.1) == 137
