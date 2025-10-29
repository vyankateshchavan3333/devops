def test_sanity():
    assert 1 + 1 == 2

def test_health_check():
    from app import app
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
