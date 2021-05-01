class Contract():
    def __init__(self,name,start,end):
        self.name = name
        self.start = start
        self.end = end

    def __gt__(self, contract):
        return self.end > contract.end

    def exceeds_week(self):
        return self.end < self.start
    
    def get_end(self):
        return self.end

    def get_start(self):
        return self.start

    def get_name(self):
        return self.name



def interval_scheduling(C):
    A = []
    if(len(C) == 0):
        return A
    C = sorted(C)
    end = C[0].get_end()
    A.append(C[0])
    for i in range (1,len(C)):
        current = C[i]
        if(current.get_start()>=end):
            A.append(current)
            end = current.get_end()
    return A


def select_contracts (C):
    # We separate the intervals into two groups, g1 and g2.
    g1 = []
    g2 = []
    
    for contract in C:
        if not contract.exceeds_week():
            g1.append(contract)
        else:
            g2.append(contract)
    
    #We generate an optimal solution for type 1 (o) with the interval scheduling algorithm
    o = interval_scheduling (g1)

    #now we will see if we can add one more contract
    if len(g2) > 0:
        max_end_time = g1[0].get_end()
        min_start_time = g1[0].get_start()
        for i in range (1,len(g1)):
            current = g1[i]
            if current.get_start() < min_start_time:
                min_start_time = current.get_start()
            if current.get_end() > max_end_time:
                max_end_time = current.get_end()
        for contract in C:
            if contract.get_start() >= max_end_time and contract.get_end() <= min_start_time:
                o.append(contract)
                break
    
    #We return the maximum subset
    return o


def read_file(path):
    contracts = []
    f = open (path,'r')
    line = f.readline()
    while line:
        line = line[:-1]
        line = line.split(",")
        contracts.append(Contract(line[0],int(line[1]),int(line[2])))
        line = f.readline()
    f.close()  
    return contracts


def main():
    contracts = read_file("contracts.txt")
   
    A = select_contracts(contracts)

    for contract in A:
        print(contract.name)

main()


