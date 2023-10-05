#!/usr/bin/env ruby
# Scripts Output: [SENDER],[RECEIVER],[FLAGS]
#       The sender phone number of name (including country code if present)
#       The receiver phone number of name (including country code if present)
#       The flags that was used.

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
