import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class MonthlyBill(Base):
    __tablename__ = 'monthlyBills'
    id = Column(Integer, primary_key = True)
    bill = Column(String(80), nullable = False)
    cost = Column(Float)
    date = Column(String(2))
    UserID = Column(String(128))
    
class WeeklyBill(Base):
    __tablename__ = 'weeklyBills'
    id = Column(Integer, primary_key = True)
    bill = Column(String(80), nullable = False)
    cost = Column(Float)    
    dayOfWeek = Column(String(250))
    UserID = Column(String(128), nullable = False)

class BringHome(Base):
    __tablename__ = 'bringHomePay'
    id =Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    amount = Column(Float) 
    dayOfWeek =  Column(String(9))
    Frequency = Column(String(25))
    UserID = Column(String(128), nullable = False)

class BankBalance(Base):
    __tablename__ = 'keybalance'
    id =Column(Integer, primary_key = True)
    KeyBalance = Column(Float, nullable = False)
    DateTime = Column(DateTime, nullable = True)
    UserID = Column(String(128), nullable = False)
    AvailableBalance = Column(Float, nullable = True)

# engine = create_engine('sqlite:///TRBills.db')
# Base.metadata.create_all(engine)