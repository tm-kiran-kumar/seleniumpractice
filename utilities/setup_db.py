import sqlite3

connection = sqlite3.connect(r'/Users/kiran/Developer/AutomationProjects/seleniumpractice/data/automation.db')
print('Database created and connected successfully')

# Create a cursor object
cursor = connection.cursor()

#SQL Command to CREATE TABLE
# create_table_query = """
# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     task_name TEXT NOT NULL,
#     priority INTEGER,
#     status TEXT DEFAULT 'pending'
# );
# """

# # Inserting a dummy row
# print('---Inserting a test task---')
# cursor.execute("INSERT INTO tasks (task_name, priority) VALUES (?,?)", ("Check Next Logs", 2))
#
# print("\n--- Current Data in 'tasks' Table ---")
# View Table
cursor.execute("SELECT * FROM tasks")

# Fetch all rows
all_rows = cursor.fetchall()

# Print rows individually
for row in all_rows:
    print(row)

#connection.commit()
connection.close()

#print('Table tasks created successfully')