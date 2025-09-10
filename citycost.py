def calccost(paris,lonai,mudon,dubmbai):
  """used to cal cost of overall trip"""
  p=paris[0]+paris[1]*7+paris[2]
  l=london[0]+london[1]*7+london[2]
  d=dubai[0]+dubai[1]*7+dubai[2]
  m=mumbai[0]+mumbai[1]*7+mumbai[2]
  i=0
  while i<4:
    print("total cost of city: 1.paris 2.london 3.dubai 4.mumbai\nenter:")
    city=input()
    if(city=="1"):
        print("total cost is: ",p)
    elif(city=="2"):
      print("total cost is: ",l)
    elif(city=="3"):
      print("total cost is: ",d)
    elif(city=="4"):
      print("total cost is: ",m)
    else:
      print("invalid input")

    i+=1
help( calccost)
paris=[200,20,200]
london=[250,30,120]
dubai=[370,15,80]
mumbai=[450,10,70]
calccost(paris,london,dubai,mumbai)
