#!/usr/bin/env ruby

device = "/dev/ttyGPIO"
pin = ARGV[0]
sleep_time = ARGV[1].to_i

begin
  file = File.open(device, "w")
  file.write(pin + "=1\r\n")
  sleep(sleep_time)
  file.write(pin + "=0\r\n")
rescue IOError => e
  # bad.
ensure
  file.close unless file == nil
end
