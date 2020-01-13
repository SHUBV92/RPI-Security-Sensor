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
    Feed.create(image_string: params[:image])
  end

  def show
    @images = Feed.all
    decode
    render "feed/images"
  end

  def decode
    @images_array = []
    @images.each do |image|
      @images_array << image.image_string
    end
  end
end



# File.open('./app/assets/images/image1.png', 'wb+') do |f|
#   f.write(Base64.decode64(params[:image]))
# end
