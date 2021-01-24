from scale_gen import scale_gen

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


scale = scale_gen("g", "major")
print(scale)
