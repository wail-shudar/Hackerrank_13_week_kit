# Completed by: Wa'il Shudar
class qeue:

    def __init__(self):
        self.l = [] 

    def arg(self, args):        
        return getattr(self, 'case_' + str(args[0]))(args)

    def case_1(self, args):
        self.l.append(args[1])

    def case_2(self, args=None):
        self.l.pop(0)
    
    def case_3(self, args=None):
        print(self.l[0])


if __name__ == '__main__':
    q = qeue()    
    t_iter = int(input())

    for i in range(t_iter):
        t = input().split()
        q.arg(t)