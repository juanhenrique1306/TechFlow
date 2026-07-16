def test_dashboard_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Painel de tarefas" in response.get_data(as_text=True)


def test_create_task(client):
    response = client.post(
        "/tasks/new",
        data={
            "title": "Planejar rota de entrega",
            "description": "Definir melhor sequência de paradas.",
            "priority": "Crítica",
            "status": "A Fazer",
            "responsible": "Equipe de logística",
            "due_date": "2026-08-01",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Tarefa criada com sucesso" in response.get_data(as_text=True)
    assert "Planejar rota de entrega" in response.get_data(as_text=True)


def test_rejects_invalid_task(client):
    response = client.post(
        "/tasks/new",
        data={
            "title": "X",
            "priority": "Média",
            "status": "A Fazer",
        },
    )
    assert response.status_code == 400
