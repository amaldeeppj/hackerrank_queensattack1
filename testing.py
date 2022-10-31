# row = y-axis
# colomn = x-axis
# e,w,n,s,ne,se,nw,sw
x = [1,-1,0,0,1,1,-1,-1]
y = [0,0,1,-1,1,-1,1,-1]


for i, j in zip(x, y):
    print(f"X, Y: {i}, {j}")
    print("========")


