from utils.log_manager import get_logger

log = get_logger("posts_api")

class Test_Posts:
    def test_post_api_returns_201(self, api_client, api_body, configs):
        log.info("Started API Test")
        response = api_client.post_api(f"{configs['base_url']}/posts/", api_headers=configs["headers"], body_data=api_body["posts_api"])
        assert response.status_code == 201, f"Expected response code: 201; Recieved response code: {response.status_code}"
        log.info("Finished API test")
        
    def test_post_api_response_body(self, api_client, api_body, configs):
        log.info("Started API Test")
        response = api_client.post_api(f"{configs['base_url']}/posts/", api_headers=configs["headers"], body_data=api_body["posts_api"])
        data = response.json()
        assert "id" in data, f"Expected 'id' in response, Recieved '{data}' in response"
        log.info("Finished API test")