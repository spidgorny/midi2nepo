import mido

inport = mido.open_input()
msg = inport.receive()
