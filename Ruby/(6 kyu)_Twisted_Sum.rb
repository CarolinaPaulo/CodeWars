#Find the sum of the digits of all the numbers from 1 to N (both ends included).

#Examples
# N = 4
#1 + 2 + 3 + 4 = 10

# N = 10
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51


def solution(n)
  # Code here...
  str = []
  (1..n).each { |a| str << a }  
  
  a = str.join("")
  
  b = a.split("")
  
  int_array = b.map(&:to_i)
  
  return  int_array.sum 
end
