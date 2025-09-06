%%time
def printname():
  print("heloo jawad")
printname()
def printselname(name):
  print("heloo ",name)
printselname("ali")
numblist=[1,2,3,4,5,6,7,8]
list=[]
oddlist=[]
def filter(nolist):
  for numb in nolist:
    if numb%2==0:
      list.append(numb)
    else :
      oddlist.append(numb)
  return list
evenlist=filter(numblist)
print("even",evenlist)
print("odd",oddlist)
odd_list=[]
def filter_odd(list):
   for number in list:
  	  if number % 2!=0:
		     odd_list.append(number)
    	
filter_odd([1,2,3,4,5,6,7,8,9])
odd_list
