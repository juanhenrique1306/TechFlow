from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db
from .models import Task
from .services import validate_task_data

main = Blueprint("main", __name__)


@main.get("/")
def dashboard():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    counters = {
        "total": len(tasks),
        "todo": sum(task.status == "A Fazer" for task in tasks),
        "progress": sum(task.status == "Em Progresso" for task in tasks),
        "done": sum(task.status == "Concluído" for task in tasks),
        "critical": sum(task.priority == "Crítica" for task in tasks),
    }
    return render_template("dashboard.html", tasks=tasks, counters=counters)


@main.route("/tasks/new", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        form_data = request.form.to_dict()
        errors = validate_task_data(form_data)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("task_form.html", task=None, form_data=form_data), 400

        due_date = None
        if form_data.get("due_date"):
            due_date = datetime.strptime(form_data["due_date"], "%Y-%m-%d").date()

        task = Task(
            title=form_data["title"].strip(),
            description=form_data.get("description", "").strip(),
            priority=form_data["priority"],
            status=form_data["status"],
            responsible=form_data.get("responsible", "").strip(),
            due_date=due_date,
        )
        db.session.add(task)
        db.session.commit()
        flash("Tarefa criada com sucesso.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("task_form.html", task=None, form_data={})


@main.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        form_data = request.form.to_dict()
        errors = validate_task_data(form_data)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("task_form.html", task=task, form_data=form_data), 400

        task.title = form_data["title"].strip()
        task.description = form_data.get("description", "").strip()
        task.priority = form_data["priority"]
        task.status = form_data["status"]
        task.responsible = form_data.get("responsible", "").strip()
        task.due_date = (
            datetime.strptime(form_data["due_date"], "%Y-%m-%d").date()
            if form_data.get("due_date")
            else None
        )
        db.session.commit()
        flash("Tarefa atualizada com sucesso.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("task_form.html", task=task, form_data={})


@main.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Tarefa excluída com sucesso.", "success")
    return redirect(url_for("main.dashboard"))


@main.post("/tasks/<int:task_id>/status")
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get("status")

    if new_status not in {"A Fazer", "Em Progresso", "Concluído"}:
        flash("Status inválido.", "error")
        return redirect(url_for("main.dashboard"))

    task.status = new_status
    db.session.commit()
    flash("Status alterado com sucesso.", "success")
    return redirect(url_for("main.dashboard"))
