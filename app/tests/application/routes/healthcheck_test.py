class StatusPageTest:
    def test_when_app_is_running(self, http_client):
        # When
        response = http_client.get('/status')

        # Then
        assert response.status_code == 200
