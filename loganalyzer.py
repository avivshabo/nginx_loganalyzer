from model.stats import stats
from model.log import log
from model.logEntry import logEntry
import sys
import time

logFile=sys.argv[1]
monitorInterval=sys.argv[2] if sys.argv[2] else 5
mylog = log(logFile)
logStats = stats()
while True:
    logLines = mylog.read()
    if logLines:
        for line in logLines:
            currentLogEntry = logEntry(line)
            logStats.addID(currentLogEntry)

        logStats.printStats()
    time.sleep(monitorInterval)
