from utils.log_manager import get_logger

log = get_logger("Comments_API")

class Test_Comments:
    def test_get_comments_api_response_to_have_200(self, api_client, configs):
        log.info("Started fetching all comments")
        response = api_client.get_api(f"{configs['base_url']}/comments",  api_headers=configs["headers"])
        assert response.status_code == 200, f"Expected response code: 200, Actual response code: {response.status_code}"
        log.info("API Test for comments api is completed")

    def test_get_single_comment(self, api_client, configs):
        pass