require 'rails_helper'

RSpec.feature "Sign up", type: :feature do
  scenario "Can sign up" do
    visit "/"
    click_link "Sign up"
    fill_in "Email", with: "test@test.com"
    fill_in "Password", with: "test_pass"
    fill_in "Password confirmation", with: "test_pass"
    click_button "Sign up"
    expect(page).to have_content("Security Feed")
  end
end
