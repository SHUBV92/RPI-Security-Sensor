Rails.application.routes.draw do
  get 'feed/images', to: 'feed#images'

  get "/pages/:page" => "pages#show"

  post "/", to: 'feed#create'

  root to: "feed#show"
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
