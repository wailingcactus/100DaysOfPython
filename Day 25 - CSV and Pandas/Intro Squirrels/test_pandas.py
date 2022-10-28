# # with open("weather_data.csv") as weather_file:
# #     weather_data = weather_file.readlines()
# #     print(weather_data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures=[]
# #     print(data)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
# import numpy as np
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# #
# # avg_temp = data["temp"].mean()
# # print(avg_temp)
# #
# # max_temp = data["temp"].max()
# # print(max_temp)
# # #
# # # print(data.condition)
# #
# # #Get data in row
# # print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# temp = monday.temp
# temp_f = (temp*9/5)+32
# print(temp_f)
#
# #Create a data frame