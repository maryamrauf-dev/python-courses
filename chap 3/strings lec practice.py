name="maryam"
shortname=name[0:2]#included all character from 0 to 1
print(shortname)
print(name[0:3])#included all character from 0 to 2
print(name[0:4])#included all character from 0 to 3
print(name[-1:-4])#negative index start from right to left and start with -1 not 0 
#this will be likw maryam (m=-1,a=-2,y=-3,r=-4,a=-5,m=-6) so it will print nothing also we can convert this into positive index
#as it will be 5:2 so will print nothing
print(name[-3:-1])
#also it is convinent to convert this into positive index as in positive it will be converted as 3:5
print(name[3:7])
print(name[:3])#1st mai kuch ni likha to 0 se start hoga
print(name[3:])#last mai kuch ni likha to end tak jayega
print(name[:])#start se end tak

