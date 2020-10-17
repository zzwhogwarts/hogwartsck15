import pytest

from pythoncode.calculator import Calculator


def test_a():
    print("test case a")


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1], [500, 1, 501]
                                 , [2, 800, 802], [0.2, 1, 1.2], [2, 0.3, 2.3], [-2, 1, -1], [2, -3, -1]
                                 , [-1.2, 1, -0.2], [2, -4.2, -2.2], [1.2, 0, 1.2], [0, 2.7, 2.7], [-2, 0, -2]
                                 , [0, -3, -3]],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case', 'bignum_int_case'
                                 , 'int_bignum_case', 'float_int_case', 'int_float_case', 'minus_int_case',
                                  'int_minus_case'
                                 , 'minusfloat_int_case', 'int_minusfloat_case', 'float_zero_case', 'zero_float_case',
                                  'minus_zero_case', 'zero_minus_case'
                                  ]
                             )
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2

    @pytest.mark.parametrize('a,b,expect', [[4, 2, 2], [0, 2, 0], [1, 0, 0], [6, 8, 0]
        , [-2, -1, 2], [-3, 1, -3], [6, -2, -3], [6.4, 8, 0], [8, 6.4, 1],
                                            [-7.4, 2, -3], [3, -2.4, -1], [1.4, 2.4, 0], [-2.3, -3.4, 0]],
                             ids=['整除', '被除数为0', '除数为0', '非整除', '两个负数相除', '被除数为负数_除数为正整数',
                                  '被除数为正整数_除数为负数', '被除数为小数_除数为正整数', '被除数为正整数_除数为小数',
                                  '被除数为负小数_除数为正整数', '被除数为正整数_除数为负小数', '两个小数相除',
                                  '两个负小数相除'])
    def test_div(self, a, b, expect):
        # calc = Calculator()
        if b == 0:

            with pytest.raises(ZeroDivisionError) as e:
                self.calc.div(a, b)
                # 断言异常 type
                assert e.type == ZeroDivisionError
                # 断言异常 value，value 是 tuple 类型
                assert "division by zero" in str(e.value)
        else:
            result = self.calc.div(a, b)
            assert int(result) == expect
