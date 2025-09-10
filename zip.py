def cropyield(weights,region):
  result=0;
  for x,w in zip(weights,region):
    result+=x*w
  return result


kantos=[73,67,43]
johto=[91,88,64]
hoen=[87,134,58]
weights=[0.3,0.2,0.5]
print("kantos:",int(cropyield(weights,kantos)))
print("johto:",cropyield(weights,johto))
print("hoen:",cropyield(weights,hoen))
