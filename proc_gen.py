from scale_gen import scale_gen

f = open("gen.abc", "w")
meta_data = "<score lang=\"ABC\">\nX:1\nT:First Song\nC:Servo\nM:4/4\nL:1/4\nK:C\n"
f.write(meta_data)

scale = scale_gen("g", "major")
# gen bar
cnt = 0
while cnt < 6:
    for i in range(4):
        if cnt < len(scale):
            f.write(scale[cnt])
            cnt = cnt + 1
    
    f.write(" | ")


# end
f.write("]\n\n</score>")
f.close()


