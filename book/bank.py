import pandas as pd


def readfromexcel():
    df=pd.read_excel("data/bank.xlsx",index_col=0)
    return df
# x=readfromexcel()
# print(x)
def getAccount(accountno):
    try:
        df=readfromexcel()
        return df.loc[accountno]
    
    except:
        print("Errpr inside GetAccount")
    