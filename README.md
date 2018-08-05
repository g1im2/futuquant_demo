# 富途量化 API Demo 展示

根据富途量化 API 的官方文档编写相对应的 demo，用来学习和辨认 api的使用方式

## 富途官方地址链接
- [官方 API 下载](https://www.futunn.com/download/openAPI)
- [官方在线文档](https://futunnopen.github.io/futuquant/intro/intro.html)
- [官方代码地址](https://github.com/FutunnOpen/futuquant)

## QuoteDemo.py
- 主要用来说明获取行情的使用
- 另外说明一些行情更新过程中的回调类的范例

## TradeDemo.py
- 主要用来说明交易操作的使用示例
- 另外说明一些交易操作过程中的回调类范例

## 说明
- 主要的使用学习说明来自官方文档
- 一些参数类型来自官方文档中的枚举常量

## 学习顺序（使用顺序说明）
1. 先安装[Open API](https://www.futunn.com/download/openAPI)， 这个工具是用来跟富途的服务器进行连接的一个工具，要使用量化工具必须先登录，这个工具就是用来干这事的。
2. OpenApi装完之后，就要安装API调用工具包，透过Api调用包连接到OpenApi上进行功能调用。
3. 这些都做完之后，就能看API帮助文档，里面有告诉我们API如何使用
4. 最后就是做我们自己的策略来使用这个工具。