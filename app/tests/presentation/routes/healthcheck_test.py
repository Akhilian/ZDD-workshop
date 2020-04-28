class StatusPageTest:
    def test_when_app_is_running(self, end_to_end):
        # When
        response = end_to_end.get('/status')

        # Then
        assert response.status_code == 200
