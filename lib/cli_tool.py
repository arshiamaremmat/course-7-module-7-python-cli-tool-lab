# lib/cli_tool.py

import argparse
from .models import Task, User  # note: relative import for package 'lib'

# Global dictionary to store users and their tasks (in-memory for the session)
users: dict[str, User] = {}

def add_task(args):
    """
    Add a task for a user (create the user if they don't exist).
    """
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user

    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    """
    Complete a task for a given user; print helpful errors if not found.
    """
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return

    task = user.get_task_by_title(args.title)
    if not task:
        print("❌ Task not found.")
        return

    task.complete()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add-task
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="User name")
    add_parser.add_argument("title", help="Task title")
    add_parser.set_defaults(func=add_task)

    # complete-task
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="User name")
    complete_parser.add_argument("title", help="Task title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

