#while
i=0
while i<=100:
  i+=1
  if i%2==0:
    print("even {}".format(i))
    continue
  print("odd  {}".format(i))
