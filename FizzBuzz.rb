#!/usr/bin/ruby
# Fizz Buzz program that prints each number from 1 to 100 on a new line
# Iterate through numbers 1 to 100
for num in 1..100
# Check if the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number
 if num%3==0 and num%5==0
  puts "FizzBuzz"
# Check if the number is divisible by 3 and print "Fizz" instead of the number
 elsif num%3==0
  puts "Fizz"
# Check if the number is divisible by 5 and print "Buzz" instead of the number
 elsif num%5==0
  puts "Buzz"
# If the number is not divisible by both 3 and 5, print the number
 else
  puts "#{num}"
 end
end