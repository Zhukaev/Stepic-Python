#2.3.4

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности

        for iter in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(iter):
                    pos = pos + 1
                else:
                    neg = neg + 1
            if self.judge(pos, neg):
                yield iter
				
#2.3.5

import itertools

def primes():
    num = 2
    while True:
        for i in range(2, num - 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1