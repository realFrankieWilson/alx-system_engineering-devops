#!/usr/bin/env ruby
# Accepts one argument and pass it to a regular expression mathching method

puts ARGV[0].scan(/hbt*n/).join
