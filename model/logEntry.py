class nginxLog(Enum):
    remoteAddr = 0
    dash1 = 1
    remoteUser = 2
    timestamp = 3
    timezone = 4
    requestMethod = 5
    requestPath = 6
    requestProtocol = 7
    requestStatus = 8
    bytesSent = 9
    httpsReferer = 10
    httpUserAgent = 11
    dash2 = 12

class logEntry:
    def __init__(self, line):

        words = line.replace('"','').split()
        self.method = words[nginxLog.requestMethod.value]
        self.path = words[nginxLog.requestPath.value]
        self.code = words[nginxLog.requestStatus.value]

    def __str__(self):
        return ' '.join([self.method, self.path, self.code])

    def __repr__(self):
        return f'Log entry(method={self.method}, path={self.path}, return code={self.code})'
