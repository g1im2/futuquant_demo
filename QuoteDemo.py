# -*- coding=utf-8 -*-

import futuquant as ft


class QuoteDemo(object):
    """
    author : smith
    date   : 2018-08-05
    desc   : demo with futuquant api using
    """

    # 初始化操作
    def __init__(self):
        # 行情上下文对象
        self.quote_ctx = ft.OpenQuoteContext(host='127.0.0.1', port=11111)
        # 设置异步回调处理对象
        # self.quote_ctx.set_handler()
        # 订阅行情信息
        # self.quote_ctx.subscribe(code_list=[], subtype_list=[], bool=True)
        # 取消订阅
        # self.quote_ctx.unsubscribe(code_list=[], subtype_list=[])
        # 查询已订阅的实时信息
        # self.quote_ctx.query_subscription(is_all_conn=True)

    def close(self):
        self.quote_ctx.stop()
        self.quote_ctx.close()

    # --------------------------------- 行情 API ---------------------------------
    # 获取全局状态
    def print_get_global_state(self):
        var_global_state = self.quote_ctx.get_global_state()
        print(var_global_state)

    # 获取订阅股票报价的实时数据，有订阅要求限制
    def print_get_stock_quote(self):
        var_stock_quote = self.quote_ctx.get_stock_quote(code_list=['SZ.002312', 'SZ.002313'])
        print(var_stock_quote)

    # 获取交易日
    def print_get_trading_days(self):
        var_trading_days = self.quote_ctx.get_trading_days(ft.Market.SZ, start_date='2018-05-01', end_date='2018-05-31')
        if var_trading_days[0] == ft.RET_OK:
            print(len(var_trading_days[1]))

    # 获取指定市场中特定类型的股票基本信息
    def print_get_stock_basic_info(self):
        var_basic_info = self.quote_ctx.get_stock_basicinfo(ft.Market.SZ)
        print(var_basic_info)

    # 获取多支股票多个时间点的指定数据列
    def print_get_multi_points_history_kline(self):
         var_multi_points_history_kline = self.quote_ctx.get_multi_points_history_kline(
             code_list=['SZ.002312', 'SZ.002313'],
             dates=['2018-05-06', '2018-05-09'],
             fields=[ft.KL_FIELD.OPEN, ft.KL_FIELD.CLOSE])
         print(var_multi_points_history_kline)

    #  获取多只股票的历史 K 线数据
    def print_get_multiple_history_kline(self):
        var_multi_history_kline = self.quote_ctx.get_multiple_history_kline(['SZ.002312', 'SZ.002313'],
                                                                            start='2018-05-01', end='2018-05-31')
        print(var_multi_history_kline)

    # 得到本地历史 K 线
    def print_get_history_kline(self):
        var_history_kline = self.quote_ctx.get_history_kline('SZ.002313', start='2018-05-01', end='2018-05-31')
        print(var_history_kline)

    # 获取给定股票列表的复权因子
    def print_get_autype_list(self):
        var_autype_list = self.quote_ctx.get_autype_list(code_list=['SZ.002313', 'SZ.002312'])
        print(var_autype_list)

    # 获取市场快照
    def print_get_market_snapshot(self):
        var_market_snapshot = self.quote_ctx.get_market_snapshot(code_list=['SZ.002313'])
        print(var_market_snapshot)

    # 获取指定股票的分时数据
    def print_get_rt_data(self):
        var_rt_data = self.quote_ctx.get_rt_data(code='SZ.002313')
        print(var_rt_data)

    # 获取指定股票的实时逐笔， 取最近 N 笔
    def print_get_rt_ticker(self):
        var_rt_ticker = self.quote_ctx.get_rt_ticker(code='SZ.002313', num=100)
        print(var_rt_ticker)

    # 获取指定板块下的股票列表
    def print_get_plate_stock(self):
        var_plate_stock = self.quote_ctx.get_plate_stock(plate_code='SH.BK0001')
        print(var_plate_stock)

    # 获取板块集合下的子版块列表
    def print_get_plate_list(self):
        var_plate_list = self.quote_ctx.get_plate_list(market=ft.Market.SZ, plate_class=ft.Plate.ALL)
        print(var_plate_list)

    # 获取股票的经纪队列
    def print_get_broker_queue(self):
        var_broker_queue = self.quote_ctx.get_broker_queue('SZ.002313')
        print(var_broker_queue)

    # 实时获取指定股票最近 num 个 K 线数据
    def print_get_cur_kline(self):
        var_cur_kline = self.quote_ctx.get_cur_kline(code='SZ.002313', num=100)
        print(var_cur_kline)

    # 获取实时摆盘数据
    def print_get_order_book(self):
        var_order_book = self.quote_ctx.get_order_book(code='SZ.002313')
        print(var_order_book)

    # --------------------------------- 行情回调类 ---------------------------------

    # 实时报价回调处理类
    class SStockQuoteHandlerBase(ft.StockQuoteHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ft.RET_OK, data

    # 实时摆盘回调处理类
    class OOrderBookHandlerBase(ft.OrderBookHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code, data

    # 实时 K 线推送回调处理类
    class CCurKlineHandlerBase(ft.OrderBookHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code, data

    # 实时逐笔推送回调处理类
    class TTickerHandlerBase(ft.TickerHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code,data

    # 实时分钟推送回调处理类
    class RRTDataHandlerBase(ft.RTDataHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp()
            return ret_code, data

    # 实时经纪推送回调处理类
    class BBrokerHandlerBase(ft.BrokerHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code, data


if __name__ == '__main__':
    demo = QuoteDemo()
    demo.print_get_multi_points_history_kline()
    demo.close()




