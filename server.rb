require 'sinatra'

get '/downstairs' do
  system("/home/hasi/atlas.door/open_door_downstairs.sh 3")
end

