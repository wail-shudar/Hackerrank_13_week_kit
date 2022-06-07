class textEditor:
   
    def __init__(self, s=None):
        self.s = s if s else ''
        self.s_prev = []
        
    def edit(self, args):
        return getattr(self, 'case_' + str(args[0]))(args)

    def case_1(self, args):
        self.s_prev.append(self.s)
        self.s += args[1]

    def case_2(self, args):
        self.s_prev.append(self.s)
        self.s = self.s[:-int(args[1])]
        
    def case_3(self, args):
        print(self.s[int(args[1])-1])
        
    def case_4(self, args=None):
        self.s = self.s_prev[-1]
        self.s_prev.pop()
          
        
if __name__ == '__main__':
    txt = textEditor()    
    ops = int(input())

    for op in range(ops):
        op = input().split()
        txt.edit(op)