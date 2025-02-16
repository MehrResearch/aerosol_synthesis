from pico_ctrlaer import ON, OFF, mux, CtrlAer

NUM_PULSES = 100

def diazonium():
    for i in range(NUM_PULSES):
        print(i)
        yield ON, 100
        yield OFF, 200

def naphthoxide():
    for _ in range(NUM_PULSES):
       yield ON, 100
       yield OFF, 200

prog = mux([diazonium(), naphthoxide()])
ctrlaer = CtrlAer(sm_number=0, base_pin=7, n_pins=2)

ctrlaer.run(prog)
