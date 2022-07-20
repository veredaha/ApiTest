
import statistics
def split_male_female(data_set:dict) -> dict:
 """
    function gets a dictionary like - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    and create and returns a dictionary for each gender male = male_part and  female = female_part
    :param data_set_check: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :return:  male_dict , female_dict
    """
 male ={}
 female ={}
 for p_id, p_info in data_set.items():
  if data_set[p_id]['sex'] == "male" :
       male[p_id] = p_info
  else:
      female[p_id] = p_info
 
 return "The male dictionary is " + str(male) + " and the female dictionary is " + str(female)

def find_median_average(data_set:dict) -> float or int:
 """function gets a dictionary like - > {3322117: {"name": "Tal", "sex": "male", "age": 22} and ect 
    and returns the average age ,and the median of all ages in dictionary
    :param check_dict: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :return: mean = the average age , med =  median of all ages
    """
 ages = []
 for dict in data_set:
    ages.append(data_set[dict]["age"])
 mean = statistics.mean(ages)
 med = statistics.median(ages)
 return "The mean of the ages is : " + f"{mean:.2f}" + " and the median is: " + str(med)

def print_values_above(data_set:dict ,num = 0) :
 """
    function gets two parameters ,1 a dictionary,2 age (optional).
    if got number (age_check)- prints all values above age_check, else prints check_dict_above_age
    :param date set: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :param num: int but can be anything
    :return:None
    """
 aboveage = {}
 if num == 0:
    print(" Number is not inserted so here are all the values: : " + str(data_set))
 else:
  for p_id, p_info in data_set.items():
   if data_set[p_id]['age'] > num :
       aboveage[p_id] = p_info
 print("Values above the age of " + str(num) + " is  " + str(aboveage))


def main():
    data_set = {
    #קטיה אמרה שניתן להשתמש בת"ז בתור מפתח
    17686401 : {"sex": "male", "age": 57, "ID": 17686401, "name": "Lior"},
    27686361 : {"sex": "female", "age": 26, "ID": 27686361, "name": "Vered"},
    58146401 : {"sex": "female", "age": 60, "ID": 58146401, "name": "Dina"}}
    print(split_male_female(data_set))
    print(find_median_average(data_set))
    print_values_above(data_set,5)
if __name__ == "__main__":
    main()   
