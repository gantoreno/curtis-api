from app.main import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_perform_diagnosis():
    """ Should correctly perform a diagnosis over the given data. """
    response = client.post('/api/diagnose', json={
        "sex": 0,
        "age": 31,
        "height": 170.0,
        "weight": 100.0,
        "HR": 82.0,
        "Pd": 106.0,
        "PQ": 138.0,
        "QRS": 88.0,
        "QT": 350.0,
        "QTcFra": 392.0
    })

    assert response.status_code == 200
    assert response.json() == 'ST elevation'
