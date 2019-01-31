import os
import datetime
import random

class GreenStart(object):

  def set_sys_time(self, year, month, day):
    os.system('date -u %02d%02d0610%04d' % (month, day, year))

  def modify(self, file_name):
    file = open(file_name, 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('zero.md', 'w+')
    if flag:
      file.write('1')
    else:
      file.write('0')
      file.close()
    pass

  def commit(self):
    os.system('git add .')
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')
    pass

  def trick_commit(self, year, month, day, file_name):
    self.set_sys_time(year, month, day)
    times = random.randint(0, 35) + 2
    print("current day %04d %02d %02d", year, month, day)
    while times > 0:
      self.modify(file_name)
      self.commit()
      times -= 1
      pass

  def daily_commit(self, start_date, end_date, file_name):
    for index in range((end_date - start_date).days + 1):
      # 计算当前时间
      current_date = start_date + datetime.timedelta(days=index)
      # 触发提交
      self.trick_commit(current_date.year, current_date.month, current_date.day, file_name)
    pass

if __name__ == '__main__':
  start = GreenStart()
  start.daily_commit(datetime.date(2019, 1, 31), datetime.date(2019, 2, 25), 'zero.md')
