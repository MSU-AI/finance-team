import yfinance
import pandas

ceoData = pandas.read_csv("ceo_data_pay_sp500.csv")

quantity = 2

for x,y in ceoData.iterrows():
    if quantity == 0:
        break

    quantity -= 1

    ticker = str(y[0])
    ceo = str(y[2]).replace(" ","_")

    print("0: ",ticker)
    print("2: ",ceo)

    finalData = pandas.DataFrame()
    openList = []
    closeList = []
    dateList = []

    newTick = yfinance.Ticker(y[0])
    hist = newTick.history(period="2y",interval="1h")

    for x,y in hist.iterrows():
        date = x.strftime('%Y-%b-%d %H:%M:00')
        opn = round(y[0],2)
        high = round(y[1],2)
        low = round(y[2],2)
        close = round(y[3],2)
        volume = round(y[4],2)

        dateList.append(date)
        openList.append(opn)
        closeList.append(close)

    filename = ticker+"-"+ceo+"-"+"data"+".csv"
    fp = open(filename, "x")

    finalData["Date"] = dateList
    finalData["Open"] = openList
    finalData["Close"] = closeList
    finalData.to_csv(filename,index=False)
