from ctrlaer import ON, OFF, CtrlAer, mux

NUM_PULSES = 10

# Oxidant solution (Cerium(IV) ammonium nitrate)
def ox():
    for _ in range(NUM_PULSES):
        yield ON, 1000
        yield OFF, 10000

# Reducing agent solution (Ferroin)
def red():
    for _ in range(NUM_PULSES):
        yield ON, 1000
        yield OFF, 10000

prog = mux([ox(), red()])

ctrlaer = CtrlAer(sm_number=0, base_pin=7, n_pins=2)
ctrlaer.run(prog)