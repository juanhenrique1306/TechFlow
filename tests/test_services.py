from src.services import validate_task_data


def test_valid_task_data_returns_no_errors():
    data = {
        "title": "Separar pedidos",
        "priority": "Alta",
        "status": "A Fazer",
    }
    assert validate_task_data(data) == []


def test_short_title_returns_error():
    data = {
        "title": "Oi",
        "priority": "Média",
        "status": "A Fazer",
    }
    errors = validate_task_data(data)
    assert "pelo menos 3 caracteres" in errors[0]


def test_invalid_priority_returns_error():
    data = {
        "title": "Conferir rota",
        "priority": "Urgentíssima",
        "status": "A Fazer",
    }
    assert "Prioridade inválida." in validate_task_data(data)
