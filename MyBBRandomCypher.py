import random

#import random
#xc is a list that gets a random value assigned to it between -13 and 12
#create 26 of the random values in the list xc
#random.sample does not repeat a value

xc = random.sample(range(-13, 13), 26)

#show the key

print(xc)

#display pretty help text

print("___________________________________")

print("a = ", xc[0], "    ", "b = ", xc[1], "    ", "c = ", xc[2] )
print("   ")
print("d = ", xc[3], "    ", "e = ", xc[4], "    ", "f = ", xc[5] )
print("   ")
print("g = ", xc[6], "    ", "h = ", xc[7], "    ", "i = ", xc[8] )
print("   ")
print("j = ", xc[9], "    ", "k = ", xc[10], "    ", "l = ", xc[11] )
print("   ")
print("m = ", xc[12], "    ", "n = ", xc[13], "    ", "o = ", xc[14] )
print("   ")
print("p = ", xc[15], "    ", "q = ", xc[16], "    ", "r = ", xc[17] )
print("   ")
print("s = ", xc[18], "    ", "t = ", xc[19], "    ", "u = ", xc[20] )
print("   ")
print("v = ", xc[21], "    ", "w = ", xc[22], "    ", "x = ", xc[23] )
print("   ")
print("y = ", xc[24], "    ", "z = ", xc[25])

