from enum import Enum

class log:

    def __init__(self, logFile):
        self.linesRead = 0
        self.logFile = logFile

    def __str__(self):
        return f'log file: {self.logFile} lines read: {self.linesRead}'

    def __repr__(self):
        return f'log file: {self.logFile} lines read: {self.linesRead}'

    def read(self):
        try:
            with open(self.logFile, "rt") as file:
                logLines = file.read().splitlines()

            newLogLines=()
            logTotalLines=len(logLines)
            if logTotalLines > self.linesRead:
                newLogLines = logLines[self.linesRead:]
                self.linesRead = logTotalLines

        except IOError as error:
            print(f"An IOError occurred while reading log file {self.logFile}: {error}")
            raise
        except Exception as error:
            print(f"An exception occurred: {error}")
            raise
        return newLogLines



