require 'base64'
require 'date'

class FeedController < ApplicationController
  skip_before_action :verify_authenticity_token
  # before_action :authenticate_user!

  # def create
  #   @image = Base64.decode64(params[:image])
  #   redirect_to controller: 'feed', action: 'images'
  #   File.open('./public/image.png', 'wb+') do |f|
  #     f.write(Base64.decode64(params[:image]))
  #   end
  # end

  def create
    @p_image = Feed.create(image_string: params[:image])
    render "feed/images"
  end

  def show
    @image = Base64.decode64(@p_image)
  end
end



# File.open('./app/assets/images/image1.png', 'wb+') do |f|
#   f.write(Base64.decode64(params[:image]))
# end
