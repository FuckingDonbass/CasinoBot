from enum import Enum
from loader import listBD
import sqlite3


class State(Enum):
    Profile = 0
    Settings = 1
    Play = 2
    Wallet = 3
    ChangeBet = 4
    Main = 5
    Spin = 6
    Slot = 7


class User:
    def __init__(self, user_id, balance=0, bet=100, qiwi="", btc="", ban=False):
        self.user_id = user_id
        self.state = State.Main
        self.balance = balance
        self.bet = bet
        self.qiwi = qiwi
        self.btc = btc
        self.ban = ban

    def __str__(self):
        return f"user_id: {self.user_id}, state: {self.state}, balance: {self.balance}, " \
               f"bet: {self.bet}, qiwi: {self.qiwi}, btc: {self.btc}, ban: {self.ban}"


class Func:
    @staticmethod
    def get_object(user_id):
        for el in listBD:
            if el.user_id == user_id:
                return el
        return None

    @staticmethod
    def get_id(user_id):
        for el in listBD:
            if el.user_id == user_id:
                return user_id
        return None

    @staticmethod
    def select_all_to_bd():
        bd = sqlite3.connect("D:\\MyWorks\\CasinoBot\\CasinoBaseData\\CasinoBD.db")
        cursor = bd.cursor()
        command = """SELECT * FROM CasinoTable"""
        cursor.execute(command)
        listen = cursor.fetchall()
        bd.commit()
        cursor.close()
        for el in listen:
            listBD.append(User(el[0], el[1], el[2], el[3], el[4], el[5]))

    @staticmethod
    def save_to_bd(user_id, objects=None, balance=None, bet=None, qiwi=None, btc=None, ban=None):
        if balance is None:
            balance = objects.balance
        if bet is None:
            bet = objects.bet
        if qiwi is None:
            qiwi = objects.qiwi
        if btc is None:
            btc = objects.btc
        if ban is None:
            ban = objects.ban
        param = (user_id, balance, bet, qiwi, btc, ban)
        bd = sqlite3.connect("D:\\MyWorks\\CasinoBot\\CasinoBaseData\\CasinoBD.db")
        cursor = bd.cursor()
        ins = """INSERT INTO CasinoTable
        (ID, BALANCE, BET, QIWI_WALLET, BTC_WALLET, BAN) 
        VALUES 
        (?, ?, ?, ?, ?, ?)"""
        cursor.execute(ins, param)
        bd.commit()
        cursor.close()
