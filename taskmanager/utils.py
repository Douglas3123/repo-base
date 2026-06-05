# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks
"""Filtra tarefas por status e prioridade."""
def format_task(task):
    status = "[ ]"
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']}"

def filter_tasks(tasks, show_done=True, priority=None, min_priority=None):
    filtered = tasks
    
    if not show_done:
        filtered = [t for t in filtered if not t.get("done", False)]
    
    if priority:
        filtered = [t for t in filtered if t.get("priority") == priority]
    
    if min_priority:
        filtered = [t for t in filtered if t.get("priority") >= min_priority]
    
    return filtered
