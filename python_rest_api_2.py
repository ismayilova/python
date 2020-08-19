#!/bin/python3

import requests

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
def getWinnerTotalGoals(competition, year):
    # Write your code here
  
  uri ='https://jsonmock.hackerrank.com/api/football_competitions?'   
  print('======')
  resp = requests.get(uri+f'name={competition}&year={year}')
  
  team = resp.json()['data'][0]['winner']

  res = getTotalGoals(team,year,competition)
  print(team)
  return res


def getTotalGoals(team, year,competition):
  totalGoal = 0
  totalGoal1 = 0
  totalGoal2 =0
  uri = 'https://jsonmock.hackerrank.com/api/football_matches?'
  
  
  resp1 =requests.get(uri+f'competition={competition}&year={year}&team1={team}&page=1') 
  resp2 =requests.get(uri+f'competition={competition}&year={year}&team2={team}&page=1') 

  # print(resp1.json()['total_pages'])
  print('========')
  for i in range(1,(int(resp1.json()['total_pages'])+1)):
   
    resp = requests.get(uri+f'competition={competition}&year={year}&team1={team}&page={i}')
    for js in resp.json()['data']:
      totalGoal1+=int(js['team1goals'])
    #  print(js)
      
  print(totalGoal1)
    
  for i in range(1,int(resp2.json()['total_pages'])+1):
    resp = requests.get(uri+f'competition={competition}&year={year}&team2={team}&page={i}')
    for js in resp.json()['data']:
      totalGoal2+=int(js['team2goals'])
      # print(js)
  
  print(totalGoal2)  
  totalGoal = totalGoal1+totalGoal2

  print(totalGoal)  

  return totalGoal

    # Write your code here
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)
    print('RESULT ========================')
    print(result)
    # result = getTotalGoals(team, year)

    # fptr.write(str(result) + '\n')

    # fptr.close()
