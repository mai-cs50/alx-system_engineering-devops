#!/usr/bin/env ruby
puts ARGV.scan(/(?<=from|to|flags):(\+?w+|[-?[0-1]:?]+)/).join
