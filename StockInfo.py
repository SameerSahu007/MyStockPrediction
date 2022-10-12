from ast import main
import json
from webbrowser import get
import yfinance as yf
import pandas as pd


def getStockInfo(name):
    ticker = yf.Ticker(name)

    return ticker.info
