from copy import deepcopy


class Node(object):
    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class BigInteger:
    def __init__(self, initValue):
        self.initValue = initValue.lstrip('0')
        if len(self.initValue) == 0:
            self.initValue = '0'
        if initValue.startswith('-'):
            self.sign = False
            self.initValue = initValue[1:].lstrip(
                '0') if initValue != '0' else initValue[1:]
        else:
            self.sign = True

        self.head = TwoWayNode(self.initValue[0])
        self.tail = self.head
        for i in range(len(self.initValue) - 1):
            self.tail.next = TwoWayNode(self.initValue[i + 1], self.tail)
            self.tail = self.tail.next

    def _remove_zeros(self):
        pass

    def __str__(self):
        self_head = self.head
        line = '' if self.sign is True else '-'
        for i in range(len(self)):
            line += self_head.data
            self_head = self_head.next
        return line

    def __int__(self):
        return int(str(self))

    def __len__(self):
        length = 0
        head = self.head
        while head is not None:
            length += 1
            head = head.next
        return length

    def __lt__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is False and other.sign is True:
            return True
        elif other.sign is False and self.sign is True:
            return False
        else:
            if len(self) < len(other):
                if self.sign is True and other.sign is True:
                    return True
                else:
                    return False
            elif len(self) > len(other):
                if self.sign is True and other.sign is True:
                    return False
                else:
                    return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return True
                        else:
                            return False
                    elif int(self_head.data) > int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return False
                        else:
                            return True
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return False

    def __le__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is False and other.sign is True:
            return True
        elif other.sign is False and self.sign is True:
            return False
        else:
            if len(self) < len(other):
                if self.sign is True and other.sign is True:
                    return True
                else:
                    return False
            elif len(self) > len(other):
                if self.sign is True and other.sign is True:
                    return False
                else:
                    return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return True
                        else:
                            return False
                    elif int(self_head.data) > int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return False
                        else:
                            return True
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return True

    def __gt__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is False and other.sign is True:
            return False
        elif other.sign is False and self.sign is True:
            return True
        else:
            if len(self) < len(other):
                if self.sign is True and other.sign is True:
                    return False
                else:
                    return True
            elif len(self) > len(other):
                if self.sign is True and other.sign is True:
                    return True
                else:
                    return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return False
                        else:
                            return True
                    elif int(self_head.data) > int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return True
                        else:
                            return False
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return False

    def __ge__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is False and other.sign is True:
            return False
        elif other.sign is False and self.sign is True:
            return True
        else:
            if len(self) < len(other):
                if self.sign is True and other.sign is True:
                    return False
                else:
                    return True
            elif len(self) > len(other):
                if self.sign is True and other.sign is True:
                    return True
                else:
                    return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return False
                        else:
                            return True
                    elif int(self_head.data) > int(other_head.data):
                        if self.sign is True and other.sign is True:
                            return True
                        else:
                            return False
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return True

    def __eq__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is not other.sign:
            return False
        else:
            if len(self) != len(other):
                return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) != int(other_head.data):
                        return False
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return True

    def __ne__(self, other):
        self_head = self.head
        other_head = other.head
        if self.sign is not other.sign:
            return True
        else:
            if len(self) != len(other):
                return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) != int(other_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        other_head = other_head.next
                else:
                    return False

    def __add__(self, other):
        new_bigint_str = str()
        self._remove_zeros()
        other._remove_zeros()
        if self.sign is True and other.sign is True:
            pass
        elif self.sign is True and other.sign is False:
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            res = self_copy - other_copy
            if self_copy > other_copy:
                res.sign = True
            elif self_copy < other_copy:
                res.sign = False
            else:
                res = BigInteger('0')
            return res
        elif self.sign is False and other.sign is True:
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            res = other_copy - self_copy
            if self_copy > other_copy:
                res.sign = False
            elif self_copy < other_copy:
                res.sign = True
            else:
                res = BigInteger('0')
            return res
        else:  # self.sign is False and other.sign is False
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            res = self_copy + other_copy
            res.sign = False
            return res

        self_tail = self.tail
        other_tail = other.tail
        remainder = 0

        def digit_operation(remainder, self_tail_data=0, other_tail_data=0):
            digit = int(self_tail_data) + int(other_tail_data) + remainder
            if digit >= 10:
                remainder = digit // 10
                digit = digit % 10
            else:
                remainder = 0
            return digit, remainder

        while self_tail is not None and other_tail is not None:
            digit, remainder = digit_operation(remainder, self_tail.data,
                                               other_tail.data)
            new_bigint_str += str(digit)
            self_tail = self_tail.previous
            other_tail = other_tail.previous

        while self_tail is not None:
            digit, remainder = digit_operation(remainder,
                                               self_tail_data=self_tail.data)
            new_bigint_str += str(digit)
            self_tail = self_tail.previous

        while other_tail is not None:
            digit, remainder = digit_operation(remainder,
                                               other_tail_data=other_tail.data)
            new_bigint_str += str(digit)
            other_tail = other_tail.previous

        if remainder == 1:
            new_bigint_str += '1'
        res = BigInteger(new_bigint_str[::-1])
        res._remove_zeros()
        return res

    def __sub__(self, other):
        new_bigint_str = str()
        self._remove_zeros()
        other._remove_zeros()
        if self.sign is True and other.sign is True:
            if self > other:
                self_tail = self.tail
                other_tail = other.tail
                sign = True
            elif self < other:
                self_tail = other.tail
                other_tail = self.tail
                sign = False
            else:
                return BigInteger('0')
        elif self.sign is True and other.sign is False:
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            res = self_copy + other_copy
            res.sign = True
            return res
        elif self.sign is False and other.sign is True:
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            res = other_copy + self_copy
            res.sign = False
            return res
        else:  # self.sign is False and other.sign is False
            self_copy, other_copy = deepcopy(self), deepcopy(other)
            self_copy.sign, other_copy.sign = True, True
            if self_copy > other_copy:
                res = self_copy - other_copy
                res.sign = False
            elif other_copy > self_copy:
                res = other_copy - self_copy
                res.sign = True
            else:
                res = BigInteger('0')
            return res

        remainder = 0

        def digit_operation(remainder, self_tail_data=0, other_tail_data=0):
            if int(self_tail_data) < int(other_tail_data):
                self_tail_data += '1'
                self_tail_data = self_tail_data[::-1]
                digit = int(self_tail_data) - int(other_tail_data) - remainder
                remainder = 1
            else:
                digit = int(self_tail_data) - int(other_tail_data) - remainder
                remainder = 0
            if digit < 0:
                digit = 10 + digit
                remainder = 1
            return digit, remainder

        while self_tail is not None and other_tail is not None:
            digit, remainder = digit_operation(remainder, self_tail.data,
                                               other_tail.data)
            new_bigint_str += str(digit)
            self_tail = self_tail.previous
            other_tail = other_tail.previous

        while self_tail is not None:
            digit, remainder = digit_operation(remainder,
                                               self_tail_data=self_tail.data)
            new_bigint_str += str(digit)
            self_tail = self_tail.previous

        while other_tail is not None:
            digit, remainder = digit_operation(remainder,
                                               other_tail_data=other_tail.data)
            new_bigint_str += str(digit)
            other_tail = other_tail.previous

        res = BigInteger(new_bigint_str[::-1])
        res.sign = sign
        return res

    def __mul__(self, other):
        new_bigint = BigInteger('0')
        multiplied = list()
        second_degree = 0
        self_tail = self.tail
        while self_tail is not None:
            other_tail = other.tail
            first_degree = 0
            while other_tail is not None:
                mult = int(self_tail.data) * int(other_tail.data)
                mult = str(mult) + '0' * first_degree + '0' * second_degree
                multiplied.append(BigInteger(mult))
                first_degree += 1
                other_tail = other_tail.previous
            second_degree += 1
            self_tail = self_tail.previous
        for integer in multiplied:
            new_bigint = new_bigint + integer
        if self.sign is other.sign:
            new_bigint.sign = True
        else:
            new_bigint.sign = False
        return new_bigint

    def __floordiv__(self, other):
        if str(other) == '0':
            raise ZeroDivisionError
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        self_copy.sign, other_copy.sign = True, True
        times = BigInteger('0')
        if self_copy > other_copy:
            while self_copy >= other_copy:
                self_copy -= other_copy
                times += BigInteger('1')
            if other.sign != self.sign:
                times += BigInteger('1')
                times.sign = False
            return times
        elif other_copy > self_copy:
            if self.sign != other.sign:
                return BigInteger('-1')
            else:
                return BigInteger('0')
        else:
            if self.sign != other.sign:
                return BigInteger('-1')
            else:
                return BigInteger('1')

    def __mod__(self, other):
        res = self - self // other * other
        return res

    def __pow__(self, power, modulo=None):
        assert int(str(power)) >= 0, 'Not working with negative powers'
        res = BigInteger('1')
        for i in range(int(str(power))):
            res *= self
        return res

    def __or__(self, other):
        res = str()
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        self_tail = self_bin.tail
        other_tail = other_bin.tail
        while self_tail is not None and other_tail is not None:
            digit = int(self_tail.data) | int(other_tail.data)
            res += str(digit)
            self_tail = self_tail.previous
            other_tail = other_tail.previous
        while self_tail is not None:
            digit = int(self_tail.data) | 0
            res += str(digit)
            self_tail = self_tail.previous
        while other_tail is not None:
            digit = int(other_tail.data) | 0
            res += str(digit)
            other_tail = other_tail.previous
        return BigInteger(res[::-1])._from_bin()

    def __and__(self, other):
        res = str()
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        self_tail = self_bin.tail
        other_tail = other_bin.tail
        while self_tail is not None and other_tail is not None:
            digit = int(self_tail.data) & int(other_tail.data)
            res += str(digit)
            self_tail = self_tail.previous
            other_tail = other_tail.previous
        while self_tail is not None:
            digit = int(self_tail.data) & 0
            res += str(digit)
            self_tail = self_tail.previous
        while other_tail is not None:
            digit = int(other_tail.data) & 0
            res += str(digit)
            other_tail = other_tail.previous
        return BigInteger(res[::-1])._from_bin()

    def __xor__(self, other):
        res = str()
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        self_tail = self_bin.tail
        other_tail = other_bin.tail
        while self_tail is not None and other_tail is not None:
            digit = int(self_tail.data) ^ int(other_tail.data)
            res += str(digit)
            self_tail = self_tail.previous
            other_tail = other_tail.previous
        while self_tail is not None:
            digit = int(self_tail.data) ^ 0
            res += str(digit)
            self_tail = self_tail.previous
        while other_tail is not None:
            digit = int(other_tail.data) ^ 0
            res += str(digit)
            other_tail = other_tail.previous
        return BigInteger(res[::-1])._from_bin()

    def __rshift__(self, other):
        self_bin = self._to_bin()
        for i in range(int(str(other))):
            self_bin.tail = self_bin.tail.previous
            if self_bin.tail is None:
                self_bin.head = TwoWayNode('0')
                break
            self_bin.tail.next = None
        return self_bin._from_bin()

    def __lshift__(self, other):
        self_bin = self._to_bin()
        for i in range(int(str(other))):
            self_bin.tail.next = TwoWayNode('0', self_bin.tail, None)
            self_bin.tail = self_bin.tail.next
        return self_bin._from_bin()

    def toString(self):
        return self.initValue

    def comparable(self):
        pass

    def arithmetic(self, rhsInt, operand):
        pass

    def bitwiseOps(self, rhsInt, operand):
        pass

    def _to_bin(self):
        res = "{0:b}".format(int(str(self)))
        return BigInteger(res)

    def _from_bin(self):
        res = str(int(str(self), 2))
        return BigInteger(res)

# зсув: __ne__ + xor
