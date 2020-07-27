#Given a column title as appears in an Excel sheet, return its corresponding column number.
#Examples:
#
#A -> 1
#    
#B -> 2
#    
#C -> 3
#    
#    ...
#    
#Z -> 26
#    
#AA -> 27
#    
#AB -> 28 
def excel_column_to_number(column):
  val = 0
  val2 = 0
  val3 = 0
  for n in range (0,len(column)):
    if n==0:
      val = ord(column[n]) - 64
    #val2 = val2 + 26**val
    if n==1:
      val = 26*val
      val2 = (ord(column[n]) -64)
    if n==2:
      val = val*26
      val2 = val2*26
      val3 = ord(column[n]) - 64
  return val + val2 + val3
  
print(excel_column_to_number("BA"))