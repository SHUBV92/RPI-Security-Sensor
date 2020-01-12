require 'base64'
require 'date'

class FeedController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :authenticate_user!

  # def create
  #   @image = Base64.decode64(params[:image])
  #   redirect_to controller: 'feed', action: 'images'
  #   File.open('./public/image.png', 'wb+') do |f|
  #     f.write(Base64.decode64(params[:image]))
  #   end
  # end

  def create
    File.open('./app/assets/images/image.png', 'wb+') do |f|
      f.write(Base64.decode64(params[:image]))
    @date = Time.now.strftime('%l:%M%P %-d-%B-%Y')
    render "feed/images"
    end
  end
end

# filenames.each do |filename|
#     File.rename(image + id.to_s)
#     id += 1
