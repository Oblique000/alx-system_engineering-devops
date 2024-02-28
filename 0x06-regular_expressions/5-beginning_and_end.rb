#!/usr/bin/env ruby
input = ARGV[0]

if input =~ /\Ah.n\Z/
  puts input
else
  puts "No match found."
end
