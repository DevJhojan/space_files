#!/usr/bin/env python3
#import sys
from start_todo.todo_promp import TodoProm
import asyncio
async def main():
    todo_promp = TodoProm()
    await todo_promp.todo_promp()
if __name__ == "__main__":
    TodoProm()