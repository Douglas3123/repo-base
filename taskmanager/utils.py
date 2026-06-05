# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    """Formata uma tarefa de forma legível para exibição na CLI."""
    # Status com emoji
    if task.get("done", False):
        status = "✅"
    else:
        status = "⬜"
    
    # Prioridade com cor/simbolo
    priority = task.get("priority", "M")
    
    # Data de prazo (se existir)
    due = f" | 📅 {task['due_date']}" if task.get("due_date") else ""
    
    return f"{status} [{priority}] #{task['id']:03d} - {task['title']}{due}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
