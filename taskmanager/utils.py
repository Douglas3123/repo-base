def filter_tasks(tasks, show_done=True, priority=None, min_priority=None):
    """Filtra tarefas por status e prioridade."""
    filtered = tasks
    
    if not show_done:
        filtered = [t for t in filtered if not t.get("done", False)]



    if priority:
        filtered = [t for t in filtered if t.get("priority") == priority]



    if min_priority:
        filtered = [t for t in filtered if t.get("priority") >= min_priority]



    
    return filtered


def format_task(task):
    status = "✅" if task.get("done", False) else "⬜"



    return f"{status} [{task.get('priority', 'M')}] #{task['id']} - {task['title']}"


