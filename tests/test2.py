from ..src.trading.connections.binance import BinanceConnection

bc = BinanceConnection()
print(bc.connection.response.status_code)
