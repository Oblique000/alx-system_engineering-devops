#!/usr/bin/env ruby
puts (matches = ARGV[0].match(/\[from:([^\[\]]+)\].\[to:([^\[\]]+)\].\[flags:([^\[\]]+)\]/)) ? matches.captures.join(',') : "No match found."
