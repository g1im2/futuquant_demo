# -*- coding:utf-8 -*-

import futuquant as ft


class TradeDemo(object):
    """
    author : smith
    date   : 2018-08-05
    desc   : trade demo with futu quant
    """

    # 初始化
    def __init__(self):
        self.trd_ctx = ft.OpenHKTradeContext(host='127.0.0.1', port=11111)

    # 关闭
    def close(self):
        self.trd_ctx.close()

    # --------------------------------- 交易操作 API ---------------------------------
    # 获取交易业务账户列表
    def print_acc_list(self):
        print(self.trd_ctx.get_acc_list())

    # 解锁交易
    def print_unlock_trade(self):
        var_unlock_trade = self.trd_ctx.unlock_trade(password="123456", password_md5=None, is_unlock=True)
        print(var_unlock_trade)

    # 获取账户资金数据
    def print_accinfo_query(self):
        var_acc_info = self.trd_ctx.accinfo_query(trd_env=ft.TrdEnv.SIMULATE, acc_id=0)
        print(var_acc_info)

    # 获取账户持仓列表
    def print_position_list_query(self):
        var_position_list = self.trd_ctx.position_list_query()
        print(var_position_list)

    # 下单
    def action_place_order(self):
        var_order = self.trd_ctx.place_order(
            price=100,                                  # 订单价格
            qty=99,                                     # 订单数量
            code='HK.00010',                            # 股票代码
            trd_side=ft.TrdSide.SELL,                   # 交易类型-sell or buy
            order_type=ft.OrderType.ABSOLUTE_LIMIT,     # 订单类型-真实账户 or 模拟账户
            adjust_limit=1,                             # 调整限制方向
            trd_env=ft.TrdEnv.SIMULATE,                 # 交易环境-真实环境 or 仿真环境
            acc_id=0                                    # 交易业务账户 ID
        )
        print(var_order)

    # 获取订单列表
    def print_order_list_query(self):
        var_order_list = self.trd_ctx.order_list_query(
            order_id='',                                # 订单号过滤
            status_filter_list='',                      # 订单状态过滤
            code='',                                    # 代码过滤
            start='2018-08-01',                         # 开始时间
            end='2018-08-05',                           # 结束时间
            trd_env=ft.TrdEnv.SIMULATE,                 # 交易环境
            acc_id=0                                    # 交易业务账户 ID
        )
        print(var_order_list)

    # 修改订单
    def action_modify_order(self):
        var_modify_order = self.trd_ctx.modify_order(
            modify_order_op=ft.ModifyOrderOp.DISABLE,   # 改单操作类型
            order_id='',                                # 订单号
            qty=100,                                    # 订单数量
            price=99,                                   # 新的订单价格
            adjust_limit=2,                             # 调整限定
            trd_env=ft.TrdEnv.SIMULATE,                 # 交易环境
            acc_id=0                                    # 交易业务账户 ID
        )
        print(var_modify_order)

    # 修改订单（老接口）
    def action_change_order(self):
        var_change_order = self.trd_ctx.change_order(
            modify_order_op=ft.ModifyOrderOp.DISABLE,  # 改单操作类型
            order_id='',  # 订单号
            qty=100,  # 订单数量
            price=99,  # 新的订单价格
            adjust_limit=2,  # 调整限定
            trd_env=ft.TrdEnv.SIMULATE,  # 交易环境
            acc_id=0  # 交易业务账户 ID
        )
        print(var_change_order)

    # 获取成交列表
    def print_deal_list_query(self):
        var_deal_list = self.trd_ctx.deal_list_query(
            code='200032',                              # 代码过滤
            trd_env=ft.TrdEnv.SIMULATE,                 # 交易环境
            acc_id=0                                    # 交易业务账户 ID
        )
        print(var_deal_list)

    # 获取历史订单列表
    def print_history_order_list_query(self):
        var_history_order_list = self.trd_ctx.history_order_list_query(
            status_filter_list=[],                      # 状态数组
            code='',                                    # 代码过滤
            start='2018-05-01',                         # 开始时间
            end='2018-05-31',                           # 结束时间
            trd_env=ft.TrdEnv.SIMULATE,                 # 交易环境
            acc_id=0                                    # 交易业务账户 ID
        )
        print(var_history_order_list)

    # 获取历史成交列表
    def print_history_deal_list_query(self):
        var_history_deal_list = self.trd_ctx.history_deal_list_query(
            code='',  # 代码过滤
            start='2018-05-01',  # 开始时间
            end='2018-05-31',  # 结束时间
            trd_env=ft.TrdEnv.SIMULATE,  # 交易环境
            acc_id=0  # 交易业务账户 ID
        )
        print(var_history_deal_list)

    # --------------------------------- 交易操作回调类 ---------------------------------
    # 响应成交推送基类
    class TTradeDealHandlerBase(ft.TradeDealHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code, data

    # 响应订单推送基类
    class TTradeOrderhandlerBase(ft.TradeOrderHandlerBase):

        def on_recv_rsp(self, rsp_pb):
            ret_code, data = super(self).on_recv_rsp(rsp_pb)
            return ret_code, data


if __name__ == '__main__':
    trader = TradeDemo()
    trader.close()