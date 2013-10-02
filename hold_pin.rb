#!/usr/bin/env ruby

device = "/dev/ttyGPIO"
pin = ARGV[0]
sleep_time = ARGV[1].to_i

begin
  file = File.open(device, "w")
  file.write(pin + "=1\r\n")
  file.close
  
  sleep(sleep_time)
  
  file = File.open(device, "w")
  file.write(pin + "=0\r\n")
  file.close
rescue IOError => e
  # bad.
ensure
  file.close unless file == nil
end
