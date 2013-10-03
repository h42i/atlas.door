#!/usr/bin/env ruby

require 'socket'               # Get sockets from stdlib

server = TCPServer.new("localhost", 9337)  # Socket to listen on port 2000
loop {                         # Servers run forever
  client = server.accept       # Wait for a client to connect
  print("client connected.")
  public_key = client.read
  print("writing public key to list.")
  key_store = File.open("keystore", "w")
  key_store.write(public_key + "\n")
  key_store.close
  client.close                 # Disconnect from the client
}
