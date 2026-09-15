import math 
def ball_collide(ball1,ball2):
   #ball format:(x,y,radius)
   x1,y1,r1=ball1
   x2,y2,r2=ball2
   distance =math.sqrt((x2-x1)** 2 +(y2-y1)**2)
   return distance <=(r1+r2)
ballA=(0,0,3)
ballB=(4,0,2)
print(ball_collide(ballA, ballB))