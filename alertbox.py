from box import alert
from timer import timer
from log import log_in, log_out

log_in()
timer(9, 0, 0)
log_out()
alert('Work Timer', 'Your time has exhausted!')
