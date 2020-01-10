Rails.application.routes.draw do
  get 'feed/images/:image', to: 'feed#images'

  root to: "application#index"
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
