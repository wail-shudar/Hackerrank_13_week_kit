from bisect import insort

class heap:
    heap = []

    def process(self, args):
        return getattr(self, 'case_' + str(args[0]))(args)

    def case_1(self, args):
        insort(self.heap, int(args[1]))

    def case_2(self, args):       
        self.heap.remove(int(args[1]))
 
    def case_3(self, args=None):
        print(self.heap[0])

    
if __name__ == '__main__':
    heap = heap()    
    ops = int(input())

    for op in range(ops):
        op = input().split()
        heap.process(op)
    
