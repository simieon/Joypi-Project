def sevenSegmentDisplay(segment, value):
  
  # to catch errors 
  if value is None:
    segment[0] = "0"     
    segment[1] = "0" 
    segment[2] = "0"    
    segment[3] = "0"
    return    

  # Loop through the list "value" and get:
  # - index: the position of the current item (0, 1, 2, ...)
  for index, singleNumber in enumerate(value):
    # Store the text version of the number
    # in the same position inside the list "segment"

    segment[index] = str(singleNumber)
  
 # set the ":" in the segment Display
  segment.colon = True
  segment.show()
  return
