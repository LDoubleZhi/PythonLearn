# encoding:utf-8
def DemoString():
    stra = 'hello world'
    print stra.capitalize()


def Dict():
    dicta = {'a': 1, 'b': 2}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    for key, value in dicta.items():
        print key, value


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__()
        self.group = group

    def __repr__(self):
        return 'im' + self.name + ' ' + str(self.uid) + ' ' + self.group


if __name__ == '__main__':
# Dict()
# print 'hello world !!'
