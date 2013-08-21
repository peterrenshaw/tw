from datetime import datetime
from apscheduler.scheduler import Scheduler



def job_function():
    count = c + 1
    print "%s" % count

#count = 0
#@print 'shedule ', count
#sched = Scheduler()
#print 'start ', count
#sched.add_cron_job(job_function,  second=30)
#sched.start()
#print 'end ', count

#If you need to unschedule the decorated functions, you can do it this way:
#if count >= 5:
#    scheduler.unschedule_job(job_function.job)


    
    
