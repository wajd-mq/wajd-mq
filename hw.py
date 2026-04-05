w=103
T=5
n=w//T
if n%2==0:
 n-=1
 gap=(w-(n*T))/2
 print ("number of tiles: ",n)
 print ("Gap at each end: ",gap)
else:   
 print (" No Gap ") 