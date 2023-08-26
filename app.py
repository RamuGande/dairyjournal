from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

@app.route('/save-entry', methods=['POST'])
def save_entry():
    entry_data = request.json
    entry_title = request.form['title']
    entry_content = request.form['content']
    attachment = request.files['attachment']
    reminder = request.form['reminder']


    # Process and store the journal entry data in the database

    # Return a response to the frontend
    return jsonify({'message': 'Entry saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)

# Establish MySQL connection
connection = pymysql.connect(
    host='localhost',
    user='Ram',
    password='Ramu@1729',
    database='project1',
    cursorclass=pymysql.cursors.DictCursor
)
with connection.cursor() as cursor:
    create_journal_entries_table_query = '''
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            attachment VARCHAR(255),
            reminder DATETIME
        )
    '''
    cursor.execute(create_journal_entries_table_query)

# Commit the changes to the database
connection.commit()

