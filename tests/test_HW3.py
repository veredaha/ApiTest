from asyncio.log import logger
import pytest
import logging
import Tar3 as t3

#logging.basicConfig(level=logging.INFO)


@pytest.fixture
def dataset() -> dict:
 """
   This function is a fixtrue that holds the dateset of people information
    :return:  data_set
 """
 data_set ={
    17686401 : {"sex": "male", "age": 57, "ID": 17686401, "name": "Lior"},
    27686361 : {"sex": "female", "age": 26, "ID": 27686361, "name": "Vered"},
    58146401 : {"sex": "female", "age": 60, "ID": 58146401, "name": "Dina"}}
 return data_set

def test_split_male_female(dataset,caplog) -> None:
 """
 Tests that function splits male and female corectly
 :param date set: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
 :param caplog -> sets the log level
 :return:None
 """
 splittest = t3.split_male_female(dataset) 
 caplog.set_level(logging.INFO)
 logging.getLogger().info('Sentence is wrong')
 assert splittest == "The male dictionary is {17686401: {'sex': 'male', 'age': 57, 'ID': 17686401, 'name': 'Lior'}} and the female dictionary is {27686361: {'sex': 'female', 'age': 26, 'ID': 27686361, 'name': 'Vered'}, 58146401: {'sex': 'female', 'age': 60, 'ID': 58146401, 'name': 'Dina'}}"


def test_find_median_average(dataset,caplog) -> None:
 """
 Tests that function finds correct mid and med
 :param date set: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
 :param caplog -> sets the log level
 :return:None
 """
 medmidtest = t3.find_median_average(dataset) 
 caplog.set_level(logging.INFO)
 logging.getLogger().info('Sentence is wrong')
 assert medmidtest == "The mean of the ages is : 47.67 and the median is: 57"

def test_print_values_above(dataset,caplog) -> None:
 """
 Tests that function prints above age correctly
 :param date set: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
 :param caplog -> sets the log level
 :return:None
 """
 printtest = t3.print_values_above(dataset,5)
 caplog.set_level(logging.INFO)
 logging.getLogger().info('Sentence is wrong')
 assert printtest == "Values above the age of 5 is  {17686401: {'sex': 'male', 'age': 57, 'ID': 17686401, 'name': 'Lior'}, 27686361: {'sex': 'female', 'age': 26, 'ID': 27686361, 'name': 'Vered'}, 58146401: {'sex': 'female', 'age': 60, 'ID': 58146401, 'name': 'Dina'}}"





