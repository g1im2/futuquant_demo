# -*-coding:utf-8 -*-

import threading


class AnalysisThread(threading.Thread):

    _upward = 1001
    _natural_upward = 1002
    _secondary_upward = 1003
    _downward = 1004
    _natural_downward = 1005
    _secondary_downward = 1006

    def __init__(self, quote_ctx):
        threading.Thread.__init__(self)
        self.array = []
        self.quote_ctx = quote_ctx

    def append_stocks(self, stock_dict):
        self.array.append(stock_dict)

    def clear_stocks(self):
        self.array.clear()

    def run(self):
        for dict in self.array:
            var_price_history = self.quote_ctx.get_history_kline(code=dict['code'], start=dict['listing_date'],
                                                                 end='2018-08-06')
            self.state_info_display(dict['name'], dict['code'], self.analysis(var_price_history[1]['close'].values))

    def state_info_display(self, name, code, state):
        if state == AnalysisThread._natural_upward:
            print('code: ', code, 'name: ', name, ' state: 自然回升')
        elif state == AnalysisThread._natural_downward:
            print('code: ', code, 'name: ', name, ' state: 自然回调')
        elif state == AnalysisThread._upward:
            print('code: ', code, 'name: ', name, ' state: 上升趋势')
        elif state == AnalysisThread._downward:
            print('code: ', code, 'name: ', name, ' state: 下降趋势')
        elif state == AnalysisThread._secondary_downward:
            print('code: ', code, 'name: ', name, ' state: 次级回调')
        elif state == AnalysisThread._secondary_upward:
            print('code: ', code, 'name: ', name, ' state: 次级回升')

    def analysis(self, data):
        state = AnalysisThread._natural_upward
        data_len = len(data)
        for index in range(data_len):
            if index + 1 < data_len:
                state = self.price_compare(data[index], data[index + 1])
        return state

    def price_compare(self, price_first, price_second):
        var_percent = abs(price_first - price_second) / price_first
        var_state = 0
        if var_percent > 0.06:
            if price_first < price_second:
                var_state = AnalysisThread._upward
            else:
                var_state = AnalysisThread._downward
        elif var_percent > 0.03:
            if price_first < price_second:
                if var_state == AnalysisThread._natural_upward:
                    var_state = AnalysisThread._upward
                else:
                    var_state = AnalysisThread._natural_upward
            else:
                if var_state == AnalysisThread._natural_downward:
                    var_state = AnalysisThread._downward
                else:
                    var_state = AnalysisThread._natural_downward
        return var_state