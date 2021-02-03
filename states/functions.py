from enum import Enum
from loader import listDB
import sqlite3


class State(Enum):
    Profile = 0
    Settings = 1
    Play = 2
    Wallet = 3
    ChangeBet = 4
    Main = 5


class User:
    def __init__(self, user_id, balance=0, bet=100, qiwi=None, btc=None, ban=False):
        self.user_id = user_id
        self.state = State.Main
        self.balance = balance
        self.bet = bet
        self.qiwi = qiwi
        self.btc = btc
        self.ban = ban

    def __str__(self):
        return f"user_id: {self.user_id}, state: {self.state}, balance: {self.balance}, bet: {self.bet}, qiwi: {self.qiwi}, btc: {self.btc}, ban: {self.ban}"


def get_object(user_id):
    for el in listDB:
        if el.user_id == user_id:
            return el
    return None


class Func:
    @staticmethod
    def get_id(user_id):
        for el in listDB:
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
            listDB.append(User(el[0], el[1], el[2], el[3], el[4], el[5]))

    @staticmethod
    def save_to_bd(user_id, object, balance=None, bet=None, qiwi=None, btc=None, ban=None):
        if balance is None:
            balance = object.balance
        if bet is None:
            bet = object.bet
        if qiwi is None:
            qiwi = object.qiwi
        if btc is None:
            btc = object.btc
        if ban is None:
            ban = object.ban
