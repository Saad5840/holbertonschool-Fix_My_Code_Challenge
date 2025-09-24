#!/usr/bin/env ruby
# Prints all numeric arguments sorted from smallest to largest.

nums = ARGV.select { |arg| arg.match?(/^[-+]?\d+$/) }  # keep only integers
           .map(&:to_i)                                # convert to integers
           .sort                                       # numeric sort

nums.each { |n| puts n }
