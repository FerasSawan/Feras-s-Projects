import yfinance as yf
#import GrowthEstimateScraper
#import SentimentAnalysis
import pandas as pd
import os
import datetime

basicMaterials = ["CSNA3","KLBN11","SUZB3","VALE3","500820","500027","509480","500440","500470","532538","500295","OR","2600","00914","51910","003670","BHP","CAR","GLEN","JMAT","MNDI","RIO","CHNR","IOSP","KALU","NTIC","RGLD","USLM","APD","ASH","CLW","CTVA","EMN","FMC","FCX","NTR","PKX","KWR","X","CRH","DOW","LAC","AEM"]
consumerDiscretionary = ["LREN3","MGLU3","532848","532977","500043","500530","500182","533155","500520","532500","500570","500114","VOW","03690","CCL","CPG","DOM","HSW","IHG","LOOK","NXT","OTB","WTB","AMZN","CZR","CAKE","CAAS","DLTR","ETSY","GRPN","HAS","HIBB","LE","LULU","MAR","MAT","ORLY","PZZA","PTON","SWBI","SBUX","SFIX","TSLA","TXRH","WEN","ULTA","URBN","VRA","ANF","BABA","AEO","APTV","AZO","BNED","BBY","BWA","BBW","BURL","KMX","CMG","DG","FL","F","GPS","GRMN","GM","HRB","HOG","HD","HMC","H","LVS","LCII","LOW","M","MCD","MOV","EDU","NKE","NCLH","PLNT","SONY","TAL","TGT","TCS","TJX","TM","UAA","VFC","WSM","WH","YUM","601888","000333","GOOS","DOL","QSR"]
consumerStaples = ["ABEV3","CRFB3","BRFS3","JBSS3","MDIA3","NTCO3","RADL3","FEMSAUBD","BIMBOA","540743","532424","500696","500875","500790","RKT","SBRY","ULVR","WYN","CASY","COST","JJSF","KDP","MNST","FIZZ","PEP","SFM","WBA","WDFC","CPB","KO","CL","DEO","GIS","K","MKC","TAP","PG","RAD","SYY","EL","HSY","TR","THS","TSN","UL","UNFI","WMT","BUD","600519","000858","NESN","ATD"]
energy = ["CSAN3","PETR3","UGPA3","533278","500312","500325","SHEL","TLW","AMTX","BP","CCJ","CVX","ENB","ET","XOM","HES","KMI","NGS","NOV","OKE","PSX","SUN","TRP","WHD","CNQ","SU"]
financials = ["B3SA3","BPAC11","BBAS3","SANB11","BBDC3","BBSE3","IRBR3","PSSA3","532810","532215","532978","500180","532174","500247","500271","500302","532955","500112","532648","BN","MC","00939","02318","AV","CLIG","HSBA","LLOY","NWG","SDR","STAN","OZK","GBCI","ONB","PACW","TROW","SEIC","AFL","ALL","AXP","APAM","BAC","BCS","BLK","BX","BAM","C","DB","DFS","BEN","GS","ICE","JPM","KEY","KKR","LAZ","L","MTB","MET","MCO","MS","OPY","PNC","PRU","RF","UBS","WFC","SCHW","002142","BNS","CWB","FFH","GWO","RY"]
healthCare = ["HYPE3","524804","500087","500124","532482","524715","UCB","AZN","SN","ACHC","AMGN","CPRX","ENDP","GMAB","GILD","GEG","HBIO","ILMN","LQDA","MYGN","REGN","VYNT","ABT","ABBV","AMN","BAX","BMY","CNC","CVS","GSK","GMED","IQV","JNJ","MCK","MRK","NVS","PFE","PBH","TEVA","UNH","VEEV","NVO","600276","300760","ROG","ACB"]
industrials = ["CCRO3","EMBR3","RENT3","RAIL3","WEGE3","GAPB","500103","500510","03311","00267","009540","BNZL","DSCV","EZJ","EXPN","FERG","SMIN","RR","AAL","ARCB","BECN","CHPT","ROCK","HTLD","JBLU","LYFT","PCAR","ROLL","SKYW","MIDD","VRSK","ASGN","BA","CNI","CP","CAT","CYD","DE","DAL","PLOW","FCN","GD","GE","LMT","NOC","RTX","RBA","SNA","LUV","SAVE","TWI","TREX","UBER","WNC","ZTO","TXT","UPS","600009","AC","BBD.B","BYD","CJT"]
realEstate = ["MULT3","INS","DLR","EXR","IRM","DOC","PSA","GEO","600007","000002"]
technology = ["CIEL3","532493","532927","532281","500209","540005","500304","532540","532755","507685","ASML","005930","SGE","AWE","ADBE","AMD","AEHR","AAPL","RTC","AVGO","CSCO","CTSH","DBX","FTNT","INTC","MANH","MMAT","MSFT","NVDA","NXPI","PYPL","QCOM","SEDG","TXN","UTSI","ANET","BILL","DXC","FICO","MA","ORCL","CRM","SAP","SNOW","TSM","V","XRX","601138","002415","CSU","ENGH","OTEX","SHOP"]
telecommunications = ["532454","535648","00941","00700","BT.A","PSON","RMV","VOD","ATVI","GOOG","BIDU","CMCSA","DJCO","GOGO","MTCH","META","NTES","NFLX","SIRI","SOHU","NCTY","VEON","AMC","T","EDR","IMAX","RCI","SPOT","TU","DIS","VZ","BCE"]
utilities = ["ELET3","SBSP3","CPFE3","EGIE3","EQTL3","532155","517300","532555","532898","533206","500400","00384","0902","SVT","SSE","UU","AEP","MSEX","YORW","AWK","D","FE","FTS","NFG","PCG","SRE","SJW","SO","UGI","600900","CU"]


sectorIndices = {0: "basicMaterials",
             1: "consumerDiscretionary",
             2: "consumerStaples",
             3: "energy",
             4: "financials",
             5: "healthCare",
             6: "industrials",
             7: "realEstate",
             8: "technology",
             9: "telecommunications",
             10: "utilities"}

allStocks = [basicMaterials,
             consumerDiscretionary,
             consumerStaples,
             energy,
             financials,
             healthCare,
             industrials,
             realEstate,
             technology,
             telecommunications,
             utilities]

#def calcScoreRisk(ticker):


def calcScoreValue(ticker):
    print('Calculating value score...')

    score = 0
    passCriteria = 2

    #GETS TICKER INFO
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        print('info', info)
        assert(len(info) > 10)
    except:
        print('error with retrieving ticker')
        return -1

    #CALCULATES SCORES FOR EACH METRIC

    #forwardPE
    try:
        if info['forwardPE'] > 25 or info['forwardPE'] < 0:
            passCriteria -= 2
            forwardPE = 0
        elif info['forwardPE'] > 20 or info['forwardPE'] < 0:
            forwardPE = 1
        else:
            forwardPE = 2
        print('forwardPE', info['forwardPE'])
    except:
        print('error with forward p/e... will try supplementing with trailing p/e')
        try:
            if info['trailingPE'] > 25 or info['trailingPE'] < 0:
                passCriteria -= 2
                forwardPE = 0
            elif info['trailingPE'] > 20 or info['trailingPE'] < 0:
                forwardPE = 1
            else:
                forwardPE = 2
            print('trailingPE', info['trailingPE'])

        except:
            print('error with trailing p/e')
            forwardPE = -1


    #currentRatio
    try:
        if info['currentRatio'] < 1:
            passCriteria -= 1
            currentRatio = 0
        elif info['currentRatio'] < 2:
            currentRatio = 1
        else:
            currentRatio = 2
        print('current ratio', info['currentRatio'])
    except:
        print('error with current ratio')
        currentRatio = -1

    #profit margins
    try:
        if info['profitMargins'] < 0.12:
            passCriteria -= 1
            profitMargin = 0
        elif info['profitMargins'] < 0.2:
            profitMargin = 1
        else:
            profitMargin = 2
        print('profit margin', info['profitMargins'])
    except:
        print('error with profit margin')
        profitMargin = -1

    #debt to Equity
    try:
        if info['debtToEquity'] > 200 or info['debtToEquity'] < 0:
            passCriteria -= 1
            debtToEquity = 0
        elif info['debtToEquity']  > 100 or info['debtToEquity'] < 0:
            debtToEquity = 1
        else:
            debtToEquity = 2
        print('debt to equity', info['debtToEquity'])
    except:
        print('error with debt to equity')
        debtToEquity = -1

    #return on Equity
    try:
        if info['returnOnEquity'] < 0.12:
            passCriteria -= 1
            returnOnEquity = 0
        elif info['returnOnEquity']  <0.20:
            returnOnEquity = 1
        else:
            returnOnEquity = 2
        print('return on equity', info['returnOnEquity'])
    except:
        print('error with return on equity')
        returnOnEquity = -1



    #CALCULATES FINAL SCORE
    score = max(forwardPE, 0) + max(currentRatio, 0) + max(profitMargin, 0) + max(debtToEquity, 0) + max(returnOnEquity, 0)
    if passCriteria <= 0:
        print('failed criteria')
        score = -1


    return [info['beta'], score, forwardPE, currentRatio, profitMargin, debtToEquity, returnOnEquity, info['longBusinessSummary']]

def calcScoreGrowth(ticker):
    return -1
   

def calcTechnicalScore(ticker):

    return -1

if __name__ == "__main__":

    PATH = f"D:\\investing club"#"C:\\Users\\Aarav\\KWHSStockScores\\"#path csv file of stock scores should be exported to

    stockScores = {}

    #calculates all stock scores
    sectorIndex = 0
    stockScoresAll = {}
    for sector in allStocks:
        sectorName = sectorIndices[sectorIndex]
        stockScores[sectorIndices[sectorIndex]] = {}

        print('\n\n\n' + sectorIndices[sectorIndex].upper())
        for stock in sector:
            try:
                print(2 * '\n', '***' + stock + '***', '\n----------')
                stockScoreValue = calcScoreValue(stock)
                print()
                stockScoreGrowth = calcScoreGrowth(stock)
                print()
                stockScoreTechnical = calcTechnicalScore(stock)
                print(stock + ' scores: ', 'value-' + str(stockScoreValue[1]) + ', growth-' + str(stockScoreGrowth) + ', technical-' + str(stockScoreTechnical))
                stockScoresAll[stock] = [sectorName ,stockScoreValue[1], stockScoreGrowth, stockScoreTechnical]
                stockScores[sectorIndices[sectorIndex]][stock] = stockScoreValue
            except Exception as e:
                print('there was an ERROR', e)
                stockScoresAll[stock] = [-1, -1, -1, -1]
                stockScores[sectorIndices[sectorIndex]][stock] = [-1, -1, -1, -1, -1, -1, -1, -1]
        sectorIndex += 1

    print('stockScores', stockScores)
    stockScoresAllDf = pd.DataFrame.from_dict(stockScoresAll, orient ='index', columns = ["sector", "value", "growth", "technical"])#pd.DataFrame(stockScoresAll, columns = ["value", "growth", "technical"])
    stockScoresAllDf.to_csv(PATH + "//stockscoresall.csv")

    #filters out the top 20% of stocks per sector
    sectorIndex = 0
    for sector in stockScores.values():

        sectorName = sectorIndices[sectorIndex]
        print('\n' + sectorName)
        sectorIndex += 1

        topValue = {}
        topGrowth = {}
        valueMinScore = 0
        valueItems = max(int(len(sector)/3), 7)

      
        #    return [info['beta'], score, forwardPE, currentRatio, profitMargin, debtToEquity, returnOnEquity, info['longBusinessSummary']]
        dfValue = pd.DataFrame.from_dict(sector, orient ='index', columns = ["beta", "score", "forwardPE", "currentRatio", "profitMargin", "debtToEquity", "returnOnEquity", "longBusinessSummary"])
        dfValue = dfValue.sort_values(by=['score'], ascending=False)
        print(dfValue)

        #adds as a file
        tempPATH = PATH + '\\' + sectorName
        try:
            os.makedirs(tempPATH)
        except:
            pass

        dfValue.to_csv(tempPATH + "\\whartonstockscores.csv")