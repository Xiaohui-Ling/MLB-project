# @author: Wade Strain
# MSBA Database Project
# November 29, 2019

# http://www.espn.com/mlb/attendance/_/year/2019

import requests
from bs4 import BeautifulSoup as bsoup

################ ATTENDANCE ##########################
# mlb_attendance_data = []
# for year in range(2001,2020):
#     search_url = 'http://www.espn.com/mlb/attendance/_/year/%s' % (year)
#     response = requests.get(search_url,
#                             headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
#     response = response.content
#
#     parsed_html = bsoup(response, 'lxml')
#     data_rows = parsed_html.find_all('tr')
#
#     # go through each row of data and put it in a 2D list
#     mlb_attendance_data.append([[col.text for col in row.find_all('td')] for row in data_rows[2:]])
#
# numOfYrs = len(mlb_attendance_data)
# # print(numOfYrs)
# # print(mlb_attendance_data)
#
# # write to csv file
# import csv
#
# table_headers = ['RK', 'TEAM', 'HOME GMS', 'HOME TOTAL', 'HOME AVG', 'HOME PCT',
#                 'ROAD GMS', 'ROAD AVG', 'ROAD PCT',
#                 'OVERALL GMS', 'OVERALL AVG', 'OVERALL PCT']
# with open('MLB_Attendance.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(table_headers)
#     for yr in range(0, numOfYrs):
#         writer.writerows(mlb_attendance_data[yr])

################ HITTING STATS ########################
mlb_hitting_stats = []
for year in range(2001, 2020):
    search_url = "http://www.espn.com/mlb/stats/team/_/stat/batting/year/%s" % (year)
    response = requests.get(search_url,
                            headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    response = response.content

    parsed_html = bsoup(response, 'lxml')
    data_rows = parsed_html.find_all('tr')

    # go through each row of data and put it in a 2D list
    mlb_hitting_stats.append([[col.text for col in row.find_all('td')] for row in data_rows[2:-4]])

numOfYrs = len(mlb_hitting_stats)

import csv

table_headers = ['RK', 'TEAM', 'GP', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI', 'AVG', 'OBP', 'SLG', 'OPS']
with open('MLB_Hitting_Stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(table_headers)
    for yr in range(0, numOfYrs):
        writer.writerows(mlb_hitting_stats[yr])
