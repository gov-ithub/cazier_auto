Rails.application.routes.draw do
  devise_for :users

  root to: 'website#index'

  get 'website/index'
  get '/about', to: 'website#about'
  get '/team', to: 'website#team'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
