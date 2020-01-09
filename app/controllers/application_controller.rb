class ApplicationController < ActionController::Base
  def index
    render plain: "Hello World!"
  end
  protect_from_forgery with: :exception
end
