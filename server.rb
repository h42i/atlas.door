require 'sinatra'

get '/:argument' do
  begin
    open_time = params[:argument].to_i
    if open_time <= 20
      system("/home/hasi/atlas.door/open_door_downstairs.sh" + open_time.to_s)
    end
    "Door downstairs is openinig for " + open_time.to_s + " seconds now."
  rescue
    "You're doing it wrong."
  end
end

