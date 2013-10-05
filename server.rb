require 'sinatra'

get '/:argument' do
  begin
    open_time = params[:argument].to_i
    if open_time <= 20
      system("/home/hasi/atlas.door/open_door_downstairs.sh" + params[:argument])
    end
  rescue
    "You're doing it wrong."
  end
end

