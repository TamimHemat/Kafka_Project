from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base
import datetime

class Stats(Base):
    # TODO declare table name
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    
    # TODO create the necessary columns following the id example above
    max_buy_price = Column(Float, nullable=False)
    num_buys = Column(Integer, nullable=False)
    max_sell_price = Column(Float, nullable=False)
    num_sells = Column(Integer, nullable=False)
    last_updated = Column(String(250), nullable=False)

    def __init__(self, max_buy_price, num_buys, max_sell_price, num_sells, last_updated):
        # TODO assign the parameter values to the object's properties
        self.max_buy_price = max_buy_price
        self.num_buys = num_buys
        self.max_sell_price = max_sell_price
        self.num_sells = num_sells
        self.last_updated = last_updated

    def to_dict(self):
        # TODO create a dict, and assign object properties to your dict
        dict = {}
        dict['max_buy_price'] = self.max_buy_price
        dict['num_buys'] = self.num_buys
        dict['max_sell_price'] = self.max_sell_price
        dict['num_sells'] = self.num_sells
        dict['last_updated'] = self.last_updated

        # TODO return dict
        return dict
