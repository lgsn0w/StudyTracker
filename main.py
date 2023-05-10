from database import create_connection, create_table
from gui import GUI

create_table(create_connection('users.db'))
# Create a connection to the database
conn = create_connection('users.db')

# Create an instance of the GUI class
gui = GUI(conn)

# Run the GUI
gui.run()
