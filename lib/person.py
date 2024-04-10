#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        if isinstance(name, str) and 1 >= len(name) <=25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("The job must be in the following list of jobs")