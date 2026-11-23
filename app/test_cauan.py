from app import app


def test_rota_inexistente_da_404():
    assert app.test_client().get("/nao-existe").status_code == 404
