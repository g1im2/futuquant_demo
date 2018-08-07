# -*- coding:utf-8 -*-

import futuquant as ft
import AnalysisThread


class QuantTrader(object):

    def __init__(self):
        self.quote_ctx = ft.OpenQuoteContext(host='127.0.0.1', port=11111)

    def close(self):
        self.quote_ctx.stop()
        self.quote_ctx.close()

    def print_sz_info(self):
        var_sz_quote = self.quote_ctx.get_stock_basicinfo(ft.Market.SZ)
        num = 0
        for var in var_sz_quote[1].index:
            stock_dict = var_sz_quote[1].loc[var]
            stock_name = stock_dict['name']
            stock_date = stock_dict['listing_date']
            stock_code = stock_dict['code']
            if stock_date == '1970-01-01':
                continue
            var_price_history = self.quote_ctx.get_history_kline(code=stock_code, start=stock_date, end='2018-08-06')
            self.print_state(stock_name, self.analysis(var_price_history[1]['close'].values))

    def print_sh_info(self):
        var_sh_quote = self.quote_ctx.get_stock_basicinfo(ft.Market.SH)
        print(var_sh_quote)

    def run(self, thread_index=10):
        var_sz_quote = self.quote_ctx.get_stock_basicinfo(ft.Market.SZ)
        stock_sz_count = var_sz_quote[1]['code'].count()
        array_count = stock_sz_count / thread_index
        thread_array = []
        for var in range(stock_sz_count):
            # 定位到具体的股票信息
            stock_dict = var_sz_quote[1].loc[var]
            # 查看具体的股票上市时间
            stock_date = stock_dict['listing_date']
            if stock_date != '1970-01-01':

        for th in thread_array:
            th.join()

if __name__ == '__main__':
    trader = QuantTrader()
    trader.run()
    trader.close()
