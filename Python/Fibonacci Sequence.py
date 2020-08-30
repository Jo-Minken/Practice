def Fibonacci(n):
    fibonacci = []
    for i in range(n):
        if i == 0 or i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    print("the {}th element of {} is {}".format(n, fibonacci, fibonacci[-1]))

Fibonacci(2)
Fibonacci(3)
Fibonacci(10)


"""
Try to write a iterable class which can print out a Fibonacci sequence.

[1, 1, 2, 3, 5, 8, 13, 21, 44, 55...]

Remember your class must have a dunder iter method which returns itself,

and a dunder next method which returns the next value.

It would be nicer to have a dunder repr method to discribe your class
"""

class fibon_iterator:
    def __init__(self, *args):
        self.fibon = []
        self.runs = args[0]
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.runs > 0:
            self.runs -= 1
        else:
            raise StopIteration
            
        if len(self.fibon) < 2:
            self.fibon.append(1)
        else:
            self.fibon.append(self.fibon[0] + self.fibon[1])
            self.fibon.pop(0)
            
            
        return self.fibon[-1]
            
    
    def __repr__(self):
        return "A iterator of fibon for {} runs".format(self.runs)
    
    

fi = fibon_iterator(10)
print(fi)

for fibon in fi:
    print(fibon)
    