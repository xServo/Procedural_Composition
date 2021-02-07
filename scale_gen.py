def scale_gen(key, mode):
    notes = ["a", "^a", "b", "c", "^c", "d", "^d", "e", "f", "^f", "g", "^g"]
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
    return scale
