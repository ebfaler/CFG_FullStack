from unittest import TestCase, main, mock
from shop import luxury_shop, item_price, BalanceError

# I've researched mocking in the python docs https://docs.python.org/3/library/unittest.mock.html

class TestLuxuryShop(TestCase):

    @mock.patch('shop.get_input')
    def test_luxury_shop_raises_error_on_invalid_entry_prompt(self, mock_get_input):
        mock_get_input.return_value = 'bla'
        with self.assertRaises(ValueError):  # when luxury_shop() is called, a value error is raised
            luxury_shop()

    def test_luxury_shop_proceeds_on_y_entry_prompt(self):
        input_mock = mock.MagicMock()
        item_price_mock = mock.MagicMock()
        with (mock.patch('shop.get_input', input_mock), mock.patch('shop.item_price', item_price_mock)):
            input_mock.return_value = 'y'
            luxury_shop()       # when get_input() returns y in luxury_shop(), item_price() is called
            item_price_mock.assert_called_once()

    def test_luxury_shop_exits_on_n_entry_prompt(self):
        input_mock = mock.MagicMock()
        item_price_mock = mock.MagicMock()
        with (mock.patch('shop.get_input', input_mock), mock.patch('shop.item_price', item_price_mock)):
            input_mock.return_value = 'n'  # when get_input() returns n in luxury_shop(), item_price() is NOT called
            luxury_shop()
            item_price_mock.assert_not_called()


    def test_cant_buy_bag_with_insufficient_funds(self):
        input_mock = mock.MagicMock()
        get_money_mock = mock.MagicMock()
        with (mock.patch('shop.get_input', input_mock), mock.patch('shop.get_more_money', get_money_mock)):
            input_mock.return_value = 'bag'
            get_money_mock.return_value = 100
            with self.assertRaises(BalanceError):  # when item_price() is called, a balance error is raised
                item_price()
            self.assertEqual(get_money_mock.call_count, 3) # get_money() is called 3 times

    def test_can_buy_bag_after_topup(self):
        input_mock = mock.MagicMock()
        get_money_mock = mock.MagicMock()
        with (mock.patch('shop.get_input', input_mock), mock.patch('shop.get_more_money', get_money_mock)):
            input_mock.return_value = 'bag'
            get_money_mock.return_value = 1000
            price = item_price()
            self.assertEqual(price, 1020)  # when item_price() is called,it returns 1020
            self.assertEqual(get_money_mock.call_count, 1) # get_money() is called once

    @mock.patch('shop.get_input')
    def test_can_buy_scarf(self, input_mock):
        input_mock.return_value = 'scarf'
        price = item_price()
        self.assertEqual(price, 99) # item_price() returns 99

    @mock.patch('shop.get_input')
    def test_key_error_when_out_of_stock(self, input_mock):
        input_mock.return_value = 'somethingelse'
        with self.assertRaises(KeyError):  # when item_price() is called, a key error is raised
         item_price()

if __name__ == "__main__":
    main()
