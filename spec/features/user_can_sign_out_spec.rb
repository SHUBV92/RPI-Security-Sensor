require 'rails_helper'

RSpec.feature "Sign out", type: :feature do
  scenario "Can sign out" do
    visit "/"
    click_link "Sign up"
    fill_in "Email", with: "test@test.com"
    fill_in "Password", with: "test_pass"
    fill_in "Password confirmation", with: "test_pass"
    click_button "Sign up"
    click_link "Sign out"
    expect(page).to have_content("Signed out successfully.")
  end

end
