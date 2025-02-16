from ctrlaer import ON, OFF, CtrlAer, mux

NUM_PULSES = 6

# "Acid" solution (Bromothymol blue)
def acid():
    for _ in range(NUM_PULSES):
        yield ON, 500
        yield OFF, 10000

# Base solution (NaOH + phenolphthalein)
def base():
    for _ in range(NUM_PULSES):
        yield ON, 500
        yield OFF, 10000

prog = mux([acid(), base()])

ctrlaer = CtrlAer(sm_number=0, base_pin=7, n_pins=2)
ctrlaer.run(prog)