# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    # Status dinâmico
    status = "[x]" if task.get("done", False) else "[ ]"
    
    # Adiciona data de criação se existir
    due_date = ""
    if task.get("due_date"):
        due_date = f" (prazo: {task['due_date']})"
    
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']}{due_date}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
