from apscheduler.scheduler import Scheduler
from marketscrape import *
from items_map import *

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from rosterrun import q, db, MappedMarketResult

import sys

from rq import Queue, get_current_job
from rq.job import Job
from worker import conn
from datetime import datetime

sched = Scheduler()
m = MarketScraper()
if len(sys.argv) == 0:
  print 'need to pass credentials'
  return

user = sys.argv[1]
pw = sys.argv[2]

print user
print pw
m.login(user, pw)

scrapejob = None

@sched.interval_schedule(minutes=3)
def interval_market_scrape():
  #send this to redis queue
  
  scrapejob = q.enqueue_call(func=m.get_scrape_results, args=(search_items,), result_ttl=3000)
  print 'running calc %s ' % scrapejob.id
  print 'This job runs every 12 hours.'

@sched.interval_schedule(minutes=1)
def retrieve_market_scrape():
  #retrieve results from redis queue
  if scrapejob is None:
    print 'No scrape job found'
    return
  
  try:
    job_id = scrapejob.id
    currentjob = Job(connection=conn)
    currentjob = currentjob.fetch(job_id, connection=conn)
    print 'scrape job found'
  
    print 'found job %s ' % currentjob
      
    if currentjob is not None:
      if currentjob.result is not None:
        marketresults = currentjob.result
        print marketresults
  
        #delete existing market results
           
        #cur = MappedMarketResult.query.filter_by(g_spreadsheet_id=str(session['g_spreadsheet_id']), g_worksheet_id=str(session['g_worksheet_id'])) 
      
        #[db.session.delete(c) for c in cur]  
        #db.session.commit()
        #mapped market result havs [itemid, name, cards, price, amount, title, vendor, coords, date]
        for i in range(0, len(marketresults) - 1):
          [db.session.add(MappedMarketResult(str(mr.itemid), str(mr.name), str(mr.cards), str(mr.price), str(mr.amount), str(mr.title), str(mr.vendor), str(mr.coords), str(datetime.now()))) for mr in marketresults[i]]
       
        db.session.commit()
    else: 
      print 'current job is not ready %s' % job_id
  except:
    print 'issue finding scrape job'


#@sched.cron_schedule(day_of_week='mon-fri', hour=17)
#def scheduled_job():
#    print 'This job is run every weekday at 5pm.'

sched.start()

while True:
    pass