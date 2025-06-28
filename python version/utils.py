from tiingo import TiingoClient
import math

def get_tiingo_client():
    config = {
        'session' : True,
        'api_key' : "Enter your api key"
    }
    return TiingoClient(config)

def fetch_stock_data(client , ticker , start_date , end_date):
    data = client.get_dataframe(
        ticker,
        startDate = str(start_date),
        endDate = str(end_date),
        frequency = 'daily'
    )
    return data


def calc_returns_and_cagr(df,capital):
    close_data = df['adjClose']
    init_price = close_data[0]
    final_price = close_data[-1]
    start_date = df.index[0]
    end_date = df.index[-1]
    days = (end_date - start_date).days
    n = days / 365.25
    total_return = ((final_price-init_price)/init_price)

    cagr = math.pow((final_price/init_price),(1/n)) - 1

    close_data['growth_factor'] = close_data / init_price
    close_data['portfolio_returns'] = close_data['growth_factor'] * capital

    return [total_return , cagr , close_data['portfolio_returns']]




    
