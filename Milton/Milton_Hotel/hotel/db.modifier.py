import sqlite3
conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

# Create table
c.execute('''ALTER TABLE miltons_room RENAME to milton_rooms''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()