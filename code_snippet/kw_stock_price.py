# built-in module
import sys
import pdb
import os
import pandas as pd
import time
from datetime import datetime

# UI(PyQt5) module
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

from slacker import Slacker

from kiwoom.kw import Kiwoom
from kiwoom import constant
from config import config_manager
from util.tt_logger import TTlog

from database.db_manager import DBM
from pymongo import MongoClient
import pymongo
import random
from collections import defaultdict

# load main UI object
ui = uic.loadUiType(config_manager.MAIN_UI_PATH)[0]


# main class
class TopTrader(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # load app screen
        self.tt_logger = TTlog()
        self.kw = Kiwoom()
        self.test()

    def test(self):
        # Login
        err_code = self.kw.login()
        if err_code != 0:
            self.tt_logger.error("Login Fail")
            return
        self.tt_logger.info("Login success")

        ret = self.kw.stock_price_by_min('000020', tick='1', screen_no='1111',
                                         start_date=datetime(2018, 6, 18, 0, 0, 0),
                                         end_date=datetime(2018, 6, 25, 10, 0, 0))
        pdb.set_trace()
        ret = self.kw.stock_price_by_day('000020', screen_no='1112',
                                         start_date=datetime(2000, 1, 1, 0, 0, 0),
                                         end_date=datetime(2018, 6, 25, 0, 0, 0))
        pdb.set_trace()
        ret = self.kw.stock_price_by_week('000020', screen_no='1113',
                                          start_date=datetime(2000, 1, 1, 0, 0, 0),
                                          end_date=datetime(2018, 6, 25, 0, 0, 0))
        pdb.set_trace()
        ret = self.kw.stock_price_by_month('000020', screen_no='1114',
                                          start_date=datetime(2000, 1, 1, 0, 0, 0),
                                          end_date=datetime(2018, 6, 25, 0, 0, 0))
        pdb.set_trace()

        server = self.kw.get_connect_state()
        self.kw.get_server_gubun()
        code_name = self.kw.get_master_stock_name('207940')  # 삼바
        THEME_ORDER = 1
        theme_list = self.kw.get_theme_group_list(THEME_ORDER)
        code_list = self.kw.get_code_list_by_market(0)


# Print Exception Setting
sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tt = TopTrader()
    tt.show()
    sys.exit(app.exec_())
