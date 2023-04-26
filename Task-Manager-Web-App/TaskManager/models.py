import db
from sqlalchemy import Column, Integer, String, Boolean

"""Class called Task
This is our data model of the task which is used for the database
This class stores all the info for a task
"""


class Task(db.Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    done = Column(Boolean)

    def __init__(self, content, done):
        self.content = content
        self.done = done

    def __repr__(self):
        return "Task {}: {} ({})".format(self.id, self.content, self.done)
