import random
import math     
import numpy as np
import matplotlib.pyplot as plt

#L=2.7 * (10**16)
L = math.sqrt(3)
#m=5.97#initializing our constants
m=0.5
#E=-2.6486*10**(9)
E=-1

#r0 = 150*10**(-15)
r0 = 0.5

def keppler_integrate(L,m,E,V,r):
  return(L/((r**2)*math.sqrt(2*m*(E-V(r))-L**2/r**2)))

def V(r):
  #return (-7.9 * 10**(20)/r)
  return(-3/(r*r)-5-r)

def F(r):
  return (E - V(r) - L*L/(2*m*r*r))

def tp(r):
  return keppler_integrate(L,m,E,V,r)

def bisection(a,b,func):
  exite=False
  while (exite== False):
    #print(a,b)
    if (func(a)*func((a+b)/2)>0):
      a=(a+b)/2
    else:
      b = (a + b)/2
    if ((b-a)/(b+a))<0.00000000000001:
      exite = True
  return (((b+a)/2)//0.00001)*0.00001
      


def rootfinder(r0,func):
  #print("Hi")
  x = np.random.uniform(math.log(r0)-2.00,math.log(r0)+3.00,1000)
  y=np.exp(x)
  y=np.sort(y)
  z=[]
  roots=[]
  for i in range(0,1000):
    z.append(func(y[i]))
  w=np.sign(z)
  for i in range(1,1000):
    if (abs(w[i-1]+w[i])!=2):
      roots.append(bisection(y[i-1],y[i],func))
  return roots
    
def nearbyrootfinder(r0,F):
  if(F(r0)<0):
    return (0,[])
  roots = rootfinder(r0,F)
  if (len(roots)!=0):
    for i in range(1,len(roots)):
      #print("Hi")
      if(roots[i-1]<=r0<=roots[i]):
        #print("Hi")
        return(1,[roots[i-1],roots[i]])
    if (r0>roots[-1]):
      return(2,[roots[-1]])
    elif (r0<roots[0]):
      return(3,[roots[0]])
  else:
    return(4,[])

def golden_min(a,b,func):
  xl=a
  xu=b                      
  R = (math.sqrt(5) - 1)/2
  d = R*(xu-xl)
  x1 = xl + d 
  x2 = xu - d
  exite=0
  
  while exite == 0:
    
    if(func(x1) < func(x2)):
      
      xopt=x1
      error = (1 - R)*abs((xu-xl)/xopt)
      xl=x2        
      x2=x1
      d=R*(xu-xl)
      x1 = xl + d
    else:
     
      xopt = x2
      error = (1 - R)*abs((xu-xl)/xopt)
      xu=x1
      x1 = x2
      d=R*(xu-xl)
      x2 = xu - d
    if (error<0.0001):
      exite=1
  return xopt
def golden_max(a,b,func):
  
  xl=a
  xu=b                      
  R = (math.sqrt(5) - 1)/2
  d = R*(xu-xl)
  x1 = xl + d 
  x2 = xu - d
  exite=0
  
  while exite == 0:
    #print(x1,x2)    
    if(func(x1) > func(x2)):
      
      xopt=x1
      error = (1 - R)*abs((xu-xl)/xopt)
      xl=x2        
      x2=x1
      d=R*(xu-xl)
      x1 = xl + d
    else:
     
      xopt = x2
      error = (1 - R)*abs((xu-xl)/xopt)
      xu=x1
      x1 = x2
      d=R*(xu-xl)
      x2 = xu - d
    if (error<0.0001):
      exite=1
  return xopt
  

def find(a,b,n,theta,m,P):
    h = (b-a)/n
    max = tp(golden_max(a,b,tp)) + 1
    min = tp(golden_min(a,b,tp)) - 1
    X = []
    Y = []
    C=0
    B=a + h
    A=a
    for iter in range(n):
      res = 0
      
        
      for _ in range(10000):
          max = tp(golden_max(A,B,tp)) + 1
          min = tp(golden_min(A,B,tp)) - 1
          y = (max-min)*random.random()
          x = A + h*random.random()
          #print(x)
          if y < tp(x) - min:
            res += 1
     
      integral = (res/10000)*(max-min)*(h)
      
      integral += (h)*(min)
      if(P==0): 
        X.append(B*math.cos((((-1)**m)*C+theta)))
        Y.append(B*math.sin((((-1)**m)*C+theta)))
      else:
        X.append(B*math.cos(2*math.pi-(((-1)**m)*C+theta)))
        Y.append(B*math.sin(2*math.pi-(((-1)**m)*C+theta)))
      A=B
      B+=h
      C+=integral
      
    plt.scatter(X,Y)
    print(C)
    return C
    
  


case,rboots = nearbyrootfinder(r0, F)

if (case==1):
  rboots[0]*=(1.01)
  rboots[1]*=1
  rboots.append(rboots[0])
  for j in range(0,2):
    t=0
    s=0
    for i in range (1,len(rboots)):
      #find(rboots[i-1],rboots[i],25,t,i+j+1)    
      t = find(rboots[i-1],rboots[i],25,t,i++1,j)
      s+=(-(-1)**(i))*t
    #t=find(rboots[0],rboots[1],25,0,i)
    if (s>=5.23):
      break
elif (case==2):
  t=0
  for i in range(0,2):
    t=find(rboots[0]*1.02,10*rboots[0],25,0,i,0)
elif(case==3):
  rboots[0]*=0.98
  t = find(0.01*rboots[0],rboots[0],25,0,0,0)
elif(case == 4):
 
  #t=find(0.01*r0,10*r0,25,0,0,0)
  print("Trajectory sensitively dependent on direction of intial velocity")
elif(case==0):
  print("motion impossible")
plt.show()

        


"""def not_Newton_Raphson_Method(L,m,E,guess):
    def V(r):
        return r
    flag = 0
    error = 100
    while(error >= 0.000001):
        value = E - V(guess) - L**2/(2*m*guess**2)
        value_with_perturbance = E - V(guess+0.00001) - L**2/(2*m*(guess+0.00001)**2)
        derivative = (value_with_perturbance - value)/0.00001
        if(math.fabs(derivative) < 0.0000000001):
            print("\nFirst order derivative vanished at a particular point, so the Newton-Raphson method failed. Sorry :(")
            flag = 1
            break
        prev_guess = guess
        guess = prev_guess - (value/derivative)
        if(math.fabs(prev_guess) < 0.0000000001):
            print("Division by 0. Hence, we cannot find the root by this method.")
            flag = 1
            break
        error = math.fabs(guess - prev_guess) * 100/math.fabs(prev_guess)
    if(flag == 0):
        print("\nThe root found is", guess)

not_Newton_Raphson_Method(1,4,0,2)"""
