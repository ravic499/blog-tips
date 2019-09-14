"""Module to explain NSE API in Python

   Used Jupyter Notebooks to visualized the plotted graph
   Hence requesting the followers to use the same
   Please do note that I have just shared the nsepy module minimal support
   Will explore more and update you all for further support

   @author : Ravichandran K (ravic499@gmail.com)
"""
from datetime import date

# External Libraries used
# matplotlib to plot the graph
import matplotlib.pyplot as plt
# nsepy to get the historical data
from nsepy import get_history

stock = get_history(symbol="HAVELLS",
                    start=date(2018,9,14),
                    end=date(2019,9,14))

# figsize is configurable as per our need
stock.Close.plot(figsize=(15, 5))
plt.title("HAVELLS")
plt.show()

# get_history help will show us list of parameters and its expected data type
help(get_history)

# Options Data and Graph
stock = get_history(symbol="ITC",
                    start=date(2018,9,1),
                    end=date(2018,9,14),
                    option_type="CE",
                    strike_price=300,
                    expiry_date=date(2018,9,27))
stock.Close.plot()
plt.title("ITC")
plt.show()

# Futures Data and Graph
import matplotlib.pyplot as plt
from datetime import date
from nsepy import get_history
stock = get_history(symbol="ITC",
                    start=date(2018,9,1),
                    end=date(2018,9,14),
                    futures=True,
                    expiry_date=date(2018,9,27))
stock.Close.plot()
plt.title("ITC")
plt.show()
