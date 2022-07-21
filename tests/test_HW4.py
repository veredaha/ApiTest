from re import T
import pytest
import logging
from tar4module import Date as d

@pytest.fixture
def date() :
 date = d(1,2,2022)
 return date


def test___init__(date,caplog) -> None:
 """
 Tests init function gets Date parameter check day,month and year
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
 caplog.set_level(logging.INFO)
 logging.getLogger().info('Date is not correct')
 assert date.day == 1
 assert date.month == 2
 assert date.year == 2022

def test___str__(date,caplog) -> None:
    """
 Tests str function gets Date parameter that date print is dd/mm/yyyy
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    strdate = date.__str__()
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert strdate == "1/2/2022"

def test_isValid(date,caplog) -> None:
    """
 Tests that function checks date valid correctly 
   (-date should be 3 seperate numbers
    - in months January, March, May, June, August, October, December - the number of the day should be betweeen 1- 31
    - in months Apil, July, September, Nuvember - the number of the day should be betweeen 1- 30
    - in fabuary the the day number should be between 1 -28 and evey 4 years 1 -29)
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    isvaliddate =  d(date.day, date.month, date.year).isValid()
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert isvaliddate == True

def test_getNextDay(date,caplog) -> None:
 """
 Tests that function thay gets date and returns day after
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
 testtnextday = d(date.day, date.month, date.year).getNextDay()
 caplog.set_level(logging.INFO)
 logging.getLogger().info('Date is not correct')
 assert testtnextday == d(2,2,2022)

def test_getNextDays(date,caplog) -> None:
    """
 Tests that function thay gets date and a number of days returns date after the days number
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    testnextdays = d(date.day, date.month, date.year).getNextDays(7)
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert testnextdays == d(8,2,2022)

def test___sub__(date,caplog) -> None:
    """
 Tests that function thay gets date returns correct differnce between days
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    testsub = d(date.day, date.month, date.year).__sub__(5,8,2016)
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert testsub == 2004

def test___lt__(date,caplog) -> None:
    """
 Tests that function thay gets date is correct , checks  if date object is lager than date input
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    islt = d(date.day, date.month, date.year).__lt__(d(1,2,2023))
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert islt == True

def test___eq__(date,caplog) -> None:
    """
 Tests that function thay gets date is correct checks  if dates are the same
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    iseq = d(date.day, date.month, date.year).__eq__(d(1,2,2022))
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert iseq == True

def test___ne__(date,caplog) -> None:
    """
 Tests that function thay gets date is correct , checks  if date object and date input are not the same
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    isne = d(date.day, date.month, date.year).__ne__(d(2,2,2022))
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert isne == True

def test___gt__(date,caplog) -> None:
    """
 Tests that function thay gets date is correct , checks  if date object is smaller than date input
 :param date: int , function that holds the date example - > (2,2,2015)
 :param caplog -> sets the log level
 :return:None
 """
    isgt = d(date.day, date.month, date.year).__gt__(d(2,2,2016))
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Date is not correct')
    assert isgt == True