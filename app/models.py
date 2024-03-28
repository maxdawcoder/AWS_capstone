from flask_sqlalchemy import SQLAlchemy

# This is the database object that will be used to interact with the database.
db = SQLAlchemy()

class Task(db.Model):
    # The name of the table in the database
    __tablename__ = 'tasks'

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Fixed sub-categories, Work, Personal, School, Others
    category = db.Column(db.Enum('Work', 'Personal', 'School', 'Others'))
    dueDate = db.Column(db.DateTime, nullable=False)

    # def __repr__(self):
    #     # Return a string representation of the object
    #     # This is used for debugging and logging purposes
    #     return f'<Task id={self.id} name={self.name} category={self.category} dueDate={self.dueDate}>'

