# -6 -5 -4,-3 -2,-1 -> -Ve Index
#  A  B  C  D  E  F
#  0, 1, 2, 3, 4, 5 -> +Ve Index

# -Ve Slicing :
# [X:Y]
# Here X: This is Start Index
# Here Y is End Index which returns the value [Y-1]th
# Also X<Y

myEdtech=('A','B','C','D','E','F')
print(myEdtech[-3:-1]) # ('D', 'E')
print(myEdtech[-6:-1]) # ('A', 'B', 'C', 'D', 'E')


