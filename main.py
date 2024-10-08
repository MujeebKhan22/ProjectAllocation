from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/database_name')

@app.route('/register_student', methods=['POST'])
def register_student():
    student_data = request.json
    query = f"INSERT INTO students (first_name, last_name, skillset, level, interest) VALUES ('{student_data['first_name']}', '{student_data['last_name']}', '{student_data['skillset']}', '{student_data['level']}', '{student_data['interest']}')"
    engine.execute(query)
    return "Student registered successfully"

if __name__ == '_main_':
    app.run(debug=True)