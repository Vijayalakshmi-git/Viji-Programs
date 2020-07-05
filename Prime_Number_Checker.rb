#!/usr/bin/ruby

# defining class primenumber
# this is optional and we could directly define function and call it
class primenumber

# function accepting an integer as argument 
# returns true if the number is a prime number and false if not
def prime_checker(num)

# setting flag is_prime to true
is_prime=true

# check if the number is 0 or 1 and print 0 or 1 is not a prime number
if num == 0 or num == 1
 puts "#{num} is neither a prime number nor a composite number"
 return
end 

# iterate through 2 to the half of the number
# and check if the number leaves a remainder 0 when divided by them
for n in 2..(num/2)
  if num % n == 0
    is_prime=false
    break
  end
end

# print true if is_prime is true else print false
 if(is_prime)
  puts "prime_checker(#{num}) => true"
 else
  puts "prime_checker(#{num}) => false"
 end  
end
end

begin                                                                                                                                                                   puts ("Enter a number:")
# getting an integer value as input
number=gets.to_i
p=primenumber.new

# calling the function with parameter
p.prime_checker(number)
end