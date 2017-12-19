def median(med):
  med.sort()
  print (med)
  size = len(med)
  print ("size %d" % size)
  ind = int(size/2)
  print ("ind %d" % ind)
  if size%2!=0:
    return med[ind]
  else:
    return (med[ind]+med[ind-1])/2


print( median([4,5,5,4]))

