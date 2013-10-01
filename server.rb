require 'sinatra'

get '/downstairs' do
  system("/home/hasi/dope/open_door_downstairs.sh")
end

get '/upstairs' do
  system("/home/hasi/dope/open_door_upstairs.sh")
end
