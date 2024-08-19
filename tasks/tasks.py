from tasks.worker import Tasks, worker


@worker.task(name=Tasks.example_task)
def example_task():
    print("This is an example task")
