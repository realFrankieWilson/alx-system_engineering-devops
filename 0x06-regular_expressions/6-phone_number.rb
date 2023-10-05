#!/usr/bin/env ruby
# The regular expression must match a 10 digit phone number.

puts ARGS[0].scan(/^[0-9]{10}$/).join
