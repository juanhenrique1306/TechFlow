VALID_PRIORITIES = {"Baixa", "Média", "Alta", "Crítica"}
VALID_STATUSES = {"A Fazer", "Em Progresso", "Concluído"}


def validate_task_data(data):
    errors = []

    title = (data.get("title") or "").strip()
    if len(title) < 3:
        errors.append("O título deve possuir pelo menos 3 caracteres.")

    if data.get("priority") not in VALID_PRIORITIES:
        errors.append("Prioridade inválida.")

    if data.get("status") not in VALID_STATUSES:
        errors.append("Status inválido.")

    return errors
