# This is a demo file. 
def func_1(count):
    count += 1
    func_2(count)

def func_2(count):
    count += 1
    func_3(count)

def func_3(count):
    count += 1
    func_4(count)

def func_4(count):
    count += 1
    print ("DONE")

count = 0
func_1(count)
