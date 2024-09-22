

mp = {
    -2: [True, True, False],
    -1: [True, True, True],
    0: [False, False, False],
    1: [False, False, True],
    2: [False, True, False],
}

# Adder1 = [-2,-2,-2,-1,-1,-1,0,0,0,1,1,1,2,2,2]
# W20 = [-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1]
Adder1 = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]
W20 = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]

n = len(Adder1)

Adder1_bit2 = "0ns 0.9v 1ns 0.9v"
Adder1_bit1 = "0ns 0.9v 1ns 0.9v"
Adder1_bit0 = "0ns 0.9v 1ns 0.9v"
W20_bit2 = "0ns 0.9v 1ns 0.9v"
W20_bit1 = "0ns 0.9v 1ns 0.9v"
W20_bit0 = "0ns 0.9v 1ns 0.9v"
t1 = True
t2 = True
t3 = True
t4 = True
t5 = True
t6 = True
t = 1

for i in range(n):
    c1 = Adder1[i]
    c2 = W20[i]

    if mp.get(c1)[0] != t1:
        if t1:
            Adder1_bit2 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            Adder1_bit2 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t1 = not t1

    if mp.get(c1)[1] != t2:
        if t2:
            Adder1_bit1 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            Adder1_bit1 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t2 = not t2

    if mp.get(c1)[2] != t3:
        if t3:
            Adder1_bit0 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            Adder1_bit0 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t3 = not t3


    if mp.get(c2)[0] != t4:
        if t4:
            W20_bit2 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            W20_bit2 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t4 = not t4

    if mp.get(c2)[1] != t5:
        if t5:
            W20_bit1 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            W20_bit1 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t5 = not t5
    
    if mp.get(c2)[2] != t6:
        if t6:
            W20_bit0 += " " + str(t) + "ns 0.9v" + " " + str(t + 0.025) + "ns 0.0v"
        else:
            W20_bit0 += " " + str(t) + "ns 0.0v" + " " + str(t + 0.025) + "ns 0.9v"
        t6 = not t6


    t+= 5

print(Adder1_bit2)
print(Adder1_bit1)
print(Adder1_bit0)
# print(W20_bit2)
# print(W20_bit1)
# print(W20_bit0)