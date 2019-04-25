from unittest import TestCase
from bigInteger import *


class TestBigInteger(TestCase):
    def setUp(self):
        self.bigint_1 = BigInteger('1')
        self.bigint_123 = BigInteger('123')
        self.bigint_34 = BigInteger('34')
        self.bigint_13 = BigInteger('13')
        self.bigint_m123 = BigInteger('-123')
        self.bigint_0 = BigInteger('0')
        self.bigint_m45 = BigInteger('-45')
        self.bigint_m13 = BigInteger('-13')

    def tearDown(self):
        self.setUp()

    def test_str(self):
        self.assertEqual(str(self.bigint_0), '0')
        self.assertEqual(str(self.bigint_123), '123')
        self.assertEqual(str(self.bigint_34), '34')
        self.assertEqual(str(self.bigint_m123), '-123')
        self.assertEqual(str(self.bigint_1), '1')

    def test_lt(self):
        self.assertEqual(self.bigint_1 < self.bigint_0, False)
        self.assertEqual(self.bigint_34 < self.bigint_m123, False)
        self.assertEqual(self.bigint_m123 < self.bigint_0, True)
        self.assertEqual(self.bigint_1 < self.bigint_1, False)
        self.assertEqual(self.bigint_34 < self.bigint_123, True)
        self.assertEqual(self.bigint_34 < self.bigint_1, False)
        self.assertEqual(self.bigint_m13 < self.bigint_m123, False)
        self.assertEqual(self.bigint_m123 < self.bigint_m13, True)
        self.assertEqual(self.bigint_13 < self.bigint_34, True)
        self.assertEqual(self.bigint_34 < self.bigint_13, False)
        self.assertEqual(self.bigint_m45 < self.bigint_m13, True)
        self.assertEqual(self.bigint_m13 < self.bigint_m45, False)

    def test_le(self):
        self.assertEqual(self.bigint_1 <= self.bigint_0, False)
        self.assertEqual(self.bigint_34 <= self.bigint_m123, False)
        self.assertEqual(self.bigint_m123 <= self.bigint_0, True)
        self.assertEqual(self.bigint_1 <= self.bigint_1, True)
        self.assertEqual(self.bigint_34 <= self.bigint_123, True)
        self.assertEqual(self.bigint_34 <= self.bigint_1, False)
        self.assertEqual(self.bigint_m13 <= self.bigint_m123, False)
        self.assertEqual(self.bigint_m123 <= self.bigint_m13, True)
        self.assertEqual(self.bigint_13 <= self.bigint_34, True)
        self.assertEqual(self.bigint_34 <= self.bigint_13, False)
        self.assertEqual(self.bigint_m45 <= self.bigint_m13, True)
        self.assertEqual(self.bigint_m13 <= self.bigint_m45, False)

    def test_gt(self):
        self.assertEqual(self.bigint_1 > self.bigint_0, True)
        self.assertEqual(self.bigint_34 > self.bigint_m123, True)
        self.assertEqual(self.bigint_m123 > self.bigint_0, False)
        self.assertEqual(self.bigint_1 > self.bigint_1, False)
        self.assertEqual(self.bigint_34 > self.bigint_123, False)
        self.assertEqual(self.bigint_34 > self.bigint_1, True)
        self.assertEqual(self.bigint_m13 > self.bigint_m123, True)
        self.assertEqual(self.bigint_m123 > self.bigint_m13, False)
        self.assertEqual(self.bigint_13 > self.bigint_34, False)
        self.assertEqual(self.bigint_34 > self.bigint_13, True)
        self.assertEqual(self.bigint_m45 > self.bigint_m13, False)
        self.assertEqual(self.bigint_m13 > self.bigint_m45, True)

    def test_ge(self):
        self.assertEqual(self.bigint_1 >= self.bigint_0, True)
        self.assertEqual(self.bigint_34 >= self.bigint_m123, True)
        self.assertEqual(self.bigint_m123 >= self.bigint_0, False)
        self.assertEqual(self.bigint_1 >= self.bigint_1, True)
        self.assertEqual(self.bigint_34 >= self.bigint_123, False)
        self.assertEqual(self.bigint_34 >= self.bigint_1, True)
        self.assertEqual(self.bigint_m13 >= self.bigint_m123, True)
        self.assertEqual(self.bigint_m123 >= self.bigint_m13, False)
        self.assertEqual(self.bigint_13 >= self.bigint_34, False)
        self.assertEqual(self.bigint_34 >= self.bigint_13, True)
        self.assertEqual(self.bigint_m45 >= self.bigint_m13, False)
        self.assertEqual(self.bigint_m13 >= self.bigint_m45, True)

    def test_eq(self):
        self.assertEqual(self.bigint_1 == self.bigint_0, False)
        self.assertEqual(self.bigint_34 == self.bigint_m123, False)
        self.assertEqual(self.bigint_m123 == self.bigint_0, False)
        self.assertEqual(self.bigint_1 == self.bigint_1, True)
        self.assertEqual(self.bigint_34 == self.bigint_123, False)

    def test_ne(self):
        self.assertNotEqual(self.bigint_1 != self.bigint_0, False)
        self.assertNotEqual(self.bigint_34 != self.bigint_m123, False)
        self.assertNotEqual(self.bigint_m123 != self.bigint_0, False)
        self.assertNotEqual(self.bigint_1 != self.bigint_1, True)
        self.assertNotEqual(self.bigint_34 != self.bigint_123, False)

    def test_add(self):
        self.assertEqual(self.bigint_123 + self.bigint_1, BigInteger('124'))
        self.assertEqual(self.bigint_1 + self.bigint_0, BigInteger('1'))
        self.assertEqual(self.bigint_34 + self.bigint_123, BigInteger('157'))
        self.assertEqual(self.bigint_m123 + self.bigint_123, BigInteger('0'))
        self.assertEqual(self.bigint_34 + self.bigint_m123, BigInteger('-89'))
        self.assertEqual(self.bigint_m123 + self.bigint_m123, BigInteger('-246'))
        self.assertEqual(self.bigint_34 + self.bigint_m13, BigInteger('21'))
        self.assertEqual(self.bigint_123 + self.bigint_m123, BigInteger('0'))
        self.assertEqual(self.bigint_m123 + self.bigint_1, BigInteger('-122'))
        self.assertEqual(self.bigint_m13 + self.bigint_13, BigInteger('0'))
        self.assertEqual(self.bigint_m13 + self.bigint_123, BigInteger('110'))

    def test_sub(self):
        self.assertEqual(self.bigint_123 - self.bigint_1, BigInteger('122'))
        self.assertEqual(self.bigint_1 - self.bigint_0, BigInteger('1'))
        self.assertEqual(self.bigint_34 - self.bigint_123, BigInteger('-89'))
        self.assertEqual(self.bigint_m123 - self.bigint_123, BigInteger('-246'))
        self.assertEqual(self.bigint_34 - self.bigint_m123, BigInteger('157'))
        self.assertEqual(self.bigint_m123 - self.bigint_m123, BigInteger('0'))
        self.assertEqual(self.bigint_34 - self.bigint_m13, BigInteger('47'))
        self.assertEqual(self.bigint_123 - self.bigint_m123, BigInteger('246'))
        self.assertEqual(self.bigint_m123 - self.bigint_1, BigInteger('-124'))
        self.assertEqual(self.bigint_m13 - self.bigint_13, BigInteger('-26'))
        self.assertEqual(self.bigint_m13 - self.bigint_123, BigInteger('-136'))
        self.assertEqual(self.bigint_m13 - self.bigint_m123, BigInteger('110'))
        self.assertEqual(self.bigint_m123 - self.bigint_m13, BigInteger('-110'))

    def test_mul(self):
        self.assertEqual(self.bigint_123 * self.bigint_1, BigInteger('123'))
        self.assertEqual(self.bigint_1 * self.bigint_0, BigInteger('0'))
        self.assertEqual(self.bigint_34 * self.bigint_123, BigInteger('4182'))
        self.assertEqual(self.bigint_m123 * self.bigint_123, BigInteger('-15129'))
        self.assertEqual(self.bigint_34 * self.bigint_m123, BigInteger('-4182'))

    def test_floordiv(self):
        self.assertEqual(self.bigint_123 // self.bigint_1, BigInteger('123'))
        self.assertEqual(self.bigint_1 // self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 // self.bigint_123, BigInteger('0'))
        self.assertEqual(self.bigint_34 // self.bigint_123, BigInteger('0'))
        self.assertEqual(self.bigint_m123 // self.bigint_123, BigInteger('-1'))
        self.assertEqual(self.bigint_34 // self.bigint_m123, BigInteger('-1'))
        with self.assertRaises(ZeroDivisionError):
            self.bigint_1 // self.bigint_0

    def test_mod(self):
        self.assertEqual(self.bigint_123 % self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 % self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 % self.bigint_123, BigInteger('1'))
        self.assertEqual(self.bigint_34 % self.bigint_123, BigInteger('34'))
        self.assertEqual(self.bigint_m123 % self.bigint_123, BigInteger('0'))
        self.assertEqual(self.bigint_34 % self.bigint_m123, BigInteger('-89'))

    def test_pow(self):
        self.assertEqual(self.bigint_123 ** self.bigint_1, BigInteger('123'))
        self.assertEqual(self.bigint_1 ** self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 ** self.bigint_123, BigInteger('1'))
        self.assertEqual(self.bigint_34 ** self.bigint_34, BigInteger('11756638905368616011414050501310355554617941909569536'))
        self.assertEqual(self.bigint_m123 ** self.bigint_34, BigInteger('113965602005968684136628000184496763088921243891670079405854808234118809'))

    def test_or(self):
        self.assertEqual(self.bigint_123 | self.bigint_1, BigInteger('123'))
        self.assertEqual(self.bigint_1 | self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 | self.bigint_123, BigInteger('123'))
        self.assertEqual(self.bigint_34 | self.bigint_123, BigInteger('123'))

    def test_and(self):
        self.assertEqual(self.bigint_123 & self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 & self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 & self.bigint_123, BigInteger('1'))
        self.assertEqual(self.bigint_34 & self.bigint_123, BigInteger('34'))

    def test_xor(self):
        self.assertEqual(self.bigint_123 ^ self.bigint_1, BigInteger('122'))
        self.assertEqual(self.bigint_1 ^ self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 ^ self.bigint_123, BigInteger('122'))
        self.assertEqual(self.bigint_34 ^ self.bigint_123, BigInteger('89'))

    def test_rshift(self):
        self.assertEqual(self.bigint_123 >> self.bigint_1, BigInteger('61'))
        self.assertEqual(self.bigint_1 >> self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 >> self.bigint_123, BigInteger('0'))
        self.assertEqual(self.bigint_34 >> self.bigint_123, BigInteger('0'))

    def test_lshift(self):
        self.assertEqual(self.bigint_123 << self.bigint_1, BigInteger('246'))
        self.assertEqual(self.bigint_1 << self.bigint_1, BigInteger('2'))
        self.assertEqual(self.bigint_1 << self.bigint_123, BigInteger('10633823966279326983230456482242756608'))
        self.assertEqual(self.bigint_34 << self.bigint_123, BigInteger('361550014853497117429835520396253724672'))

    def test__remove_zeros(self):
        pass

    def test_toString(self):
        pass

    def test_comparable(self):
        pass

    def test_arithmetic(self):
        pass

    def test_bitwiseOps(self):
        pass

    def test__to_bin(self):
        self.assertEqual(self.bigint_13._to_bin(), BigInteger('1101'))
        self.assertEqual(self.bigint_1._to_bin(), BigInteger('1'))

    def test__from_bin(self):
        self.assertEqual(BigInteger('1101')._from_bin(), self.bigint_13)
        self.assertEqual(BigInteger('1')._from_bin(), self.bigint_1)
