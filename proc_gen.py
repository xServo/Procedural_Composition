f = open("gen.abc", "w")
meta_data = "<score lang=\"ABC\">\nX:1\nT:First Song\nC:Servo\nM:4/4\nL:1/4\nK:C\n"
f.write(meta_data)
# gen bar
"""
while 1:
    for i in range(4) 
    
    print(" | ")
f.close()
"""

def scale_gen(key, mode):
    notes = ["a", "a^", "b", "c", "c^", "d", "d^", "e", "f", "f^", "g", "g^"]
    # Modes
    major = "WWHWWWH"
    minor = "WHWWHWW"
    if mode == "major":
        mode = major
    elif mode == "minor":
        mode = minor

    # Build Scale
    pos = notes.index(key) # Declare as root
    scale = []
    for i in range(len(mode)):
        if i == 0:
            scale.append(notes[pos]) 
        elif mode[i - 1]  == "H":
            pos = pos + 1
            # Wrap
            if pos == len(notes):
                pos = pos - len(notes)  
            scale.append(notes[pos]) 
        elif mode[i - 1] == "W":
            pos = pos + 2
            # Wrap
            if pos == len(notes): # len doesnt start 0 so == is going over
                pos = pos - len(notes)
            elif pos == len(notes) - 1:
                pos = pos - len(notes)
            scale.append(notes[pos]) 
    print(scale)

scale_gen("g", "major")
