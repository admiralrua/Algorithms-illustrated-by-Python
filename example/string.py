st    = input()                    # Automatically be a string
st    = "Here we; have a; string"     
st[0] = "h"                        # Error, immutable

for i, ch in enumerate(st):        # Print in a long way
    print(chr(x), ord(ch), end = " ")
	
# ASCII table:
# 0 -> 9: 48 -> 57
# A -> Z: 65 -> 90
# a -> z: 97 -> 122

st_01 = "hErE; wE hAvE; A strIng"  # Compare string
print(st >= st_01)
print(st.lower() == st_01.lower)

st_02 = st + " " + st_01

print(st.find("string"))           # Check substring

st_00 = st_02.split(";")

