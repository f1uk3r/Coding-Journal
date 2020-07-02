from datetime import datetime
import os
import sys

def main():
  date_today = datetime.now()
  year_today = date_today.strftime("%Y")
  month_today = date_today.strftime("%m")
  month = date_today.strftime("%B")
  day_today = date_today.strftime("%d")
  directory_name = f'{year_today}-{month_today}-{month}'
  if not os.path.exists(directory_name):
    os.makedirs(directory_name)
  os.chdir(f'./{directory_name}')
  with open(f'{year_today}-{month_today}-{day_today}-coding-journal.md', 'w') as fp:
    pass

if __name__ =='__main__':
  main()