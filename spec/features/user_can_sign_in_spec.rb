require 'rails_helper'

RSpec.feature "Sign in", type: :feature do
  scenario "Can sign in" do
    visit "/"
    click_link "Sign up"
    fill_in "Email", with: "test@test.com"
    fill_in "Password", with: "test_pass"
    fill_in "Password confirmation", with: "test_pass"
    click_button "Sign up"
    click_link "Sign out"
    click_link "Sign in"
    fill_in "Email", with: "test@test.com"
    fill_in "Password", with: "test_pass"
    click_button "Sign in"
    expect(page).to have_content("Signed in successfully.")
  end

end
