require 'base64'

class FeedController < ApplicationController
  def images
    if params[:image] == nil
      @image = "Not Found"
    else
      @image = Base64.decode64(params[:image])
    end
  end
end
