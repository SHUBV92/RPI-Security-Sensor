Rails.application.routes.draw do

  authenticated :user do
    root to: 'feed#show'
  end

  get 'feed/images', to: 'feed#show'

  post "/", to: 'feed#create' # Method in controller

  root :to => redirect("/users/sign_in")

  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
