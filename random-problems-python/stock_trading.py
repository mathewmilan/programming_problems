#!/usr/bin/env python3

import unittest

#Calculate Maximum Profit and Maximum Loss possible from a time series list of stock prices
def calculate_profit(price_list):
    i = 0
    max_profit = None
    min_price = None
    while (i < len(price_list) - 1):
        if (min_price is None or price_list[i] < min_price):
            min_price = price_list[i]
        profit = price_list[i+1] - min_price
        if (max_profit is None or profit > max_profit):
            max_profit = profit
        i += 1
    return max_profit


def calculate_loss(price_list):
    i = 0
    max_loss = None
    max_price = None
    while (i < len(price_list)):
        if (max_price is None or price_list[i] > max_price):
            max_price = price_list[i]
        loss = max_price - price_list[i]
        if (max_loss is None or loss > max_loss):
            max_loss = loss
        i += 1
    return max_loss

class calculateProfitTest(unittest.TestCase):
    def test_case_1(self):
        a = [10, 7, 5, 8, 11, 9, 4, 6, 10, 12]
        self.assertEqual(calculate_profit(a), 8)
        a = [10, 7, 5, 0, 8, 11, 9, 4, 6, 10, 2, 3]
        self.assertEqual(calculate_profit(a), 10)
    def test_case_2(self):
        a = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(calculate_profit(a), 0)
    def test_case_3(self):
        a = [10, 9, 8 , 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(calculate_profit(a), -1)

class calculateLossTest(unittest.TestCase):
    def test_case_1(self):
        a = [10, 7, 5, 8, 11, 9, 4, 6, 10, 12]
        assert calculate_loss(a) == 7
        a = [10, 7, 5, 0, 8, 11, 9, 4, 6, 10, 2, 3]
        assert calculate_loss(a) == 10
    def test_case_2(self):
        a = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        assert calculate_loss(a) == 0
    def test_case_3(self):
        a = [10, 9, 8 , 7, 6, 5, 4, 3, 2, 1]
        assert calculate_loss(a) == 9

def main():
    unittest.main()
    sys.exit(0)

if __name__ == '__main__':
    main()

#a = [10, 7, 5, 8, 11, 9, 4, 6, 10, 12]
#assert calculate_profit(a) == 8
#assert calculate_loss(a) == 7
#a = [10, 7, 5, 0, 8, 11, 9, 4, 6, 10, 2, 3]
#assert calculate_profit(a), 11
#assert calculate_loss(a) == 10
#a = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#assert calculate_profit(a) == 0
#assert calculate_loss(a) == 0
#a = [10, 9, 8 , 7, 6, 5, 4, 3, 2, 1]
#assert calculate_profit(a) == -1
#assert calculate_loss(a) == 9
