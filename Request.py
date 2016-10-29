class Request:
    def __init__(self):
        self.req = {'user':'none', 'priority':0, 'request':'none'}

    def setRequest(self, cust, num, action):
        self.req['user'] = cust
        self.req['priority'] = num
        self.req['request'] = action

    def getPriority(self):
        return self.req['priority']

    def getRequest(self):
        return self.req['request']

    def getUser(self):
        return self.req['user']

    def getRequest(self):
        return self.req