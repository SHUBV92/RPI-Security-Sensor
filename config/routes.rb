Rails.application.routes.draw do
  get 'feed/images', to: 'feed#show'

  post "/", to: 'feed#create' # Method in controller

  root to: "feed#show"
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
