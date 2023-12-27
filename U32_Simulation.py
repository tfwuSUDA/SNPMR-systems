Process = {
    # OpeNum:Operation,OpeNum, NextOp=(TrueNum,FalseNum) if Opetration is T, else NextOp=NextOpeNum
    # T:Test, S:Subroutine, A:Add
    0:"Finshed",
    1:"T,1,2,6",
    2:"S,1,3",
    3:"A,7,1",
    4:"T,5,5,7",
    5:"S,5,6",
    6:"A,6,4",
    7:"T,6,8,4",
    8:"S,6,9",
    9:"A,5,10",
    10:"T,7,11,13",
    11:"S,7,12",
    12:"A,1,7",
    13:"T,6,14,1",
    14:"T,4,15,16",
    15:"S,4,1",
    16:"T,5,17,23",
    17:"S,5,18",
    18:"T,5,19,27",
    19:"S,5,20",
    20:"T,5,21,30",
    21:"S,5,22",
    22:"A,4,16",
    23:"T,2,24,25",
    24:"S,2,32",
    25:"T,0,26,32",
    26:"S,0,1",
    27:"T,3,28,29",
    28:"S,3,32",
    29:"A,0,1",
    30:"A,2,31",
    31:"A,3,32",
    32:"T,4,15,0",
}

Register = [0,1,1,0,0,0,0,0]

i = 0
Pnumber = 1
while True and i < 10000:
    P = Process[Pnumber]
    print(i,(Pnumber,Register))
    Ope = P.split(",")[0]
    if Ope == "Finshed": # Finshed
        print("Finshed")
        break
    elif Ope == "T": # Test
        T = int(P.split(",")[1])
        if Register[T] == 0:
            Pnumber = int(P.split(",")[3])
        else:
            Pnumber = int(P.split(",")[2])
    elif Ope == "S": # Subtract
        T = int(P.split(",")[1])
        Pnumber = int(P.split(",")[2])
        Register[T] -= 1
    elif Ope == "A": # Add
        T = int(P.split(",")[1])
        Pnumber = int(P.split(",")[2])
        Register[T] += 1
    i += 1
        