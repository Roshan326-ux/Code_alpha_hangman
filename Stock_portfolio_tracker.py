import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        stock = yf.Ticker(ticker)
        self.portfolio[ticker] = {'quantity': quantity, 'price': stock.info['previousClose']}

    def update_prices(self):
        for ticker, data in self.portfolio.items():
            stock = yf.Ticker(ticker)
            data['price'] = stock.info['previousClose']

    def calculate_total_value(self):
        total_value = 0
        for ticker, data in self.portfolio.items():
            total_value += data['quantity'] * data['price']
        return total_value

# Example usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 100)
portfolio.add_stock('GOOGL', 50)
portfolio.update_prices()
print(portfolio.calculate_total_value())

