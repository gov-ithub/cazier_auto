require 'test_helper'

class WebsiteControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get website_index_url
    assert_response :success
  end

end
