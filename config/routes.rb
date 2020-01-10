Rails.application.routes.draw do
  get 'feed/images', to: 'feed#images'

  post "/", to: 'feed#images'

  root to: "feed#images"
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
