require 'sinatra'

get '/downstairs' do
  system("/home/hasi/atlas.door/open_door_downstairs.sh")
end

get '/upstairs' do
  system("/home/hasi/atlas.door/open_door_upstairs.sh")
end
