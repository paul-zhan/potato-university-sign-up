import sqlite3
class Database():
    def setup(self):
        
    # creating a database
        self.con = sqlite3.connect('user.db')
        # we create a cur object in order to perform SQL command
        self.cur = self.con.cursor()

            # create a table
        self.cur.execute('''CREATE  TABLE IF NOT EXISTS user(
            name text, surname text, age integer, sex text, email  text, username text, password text)''')

        self.con.commit()

    # Insert data 
    def insert_data (self, name , surname, age, sex, email , username , password):
        self.cur.execute("INSERT INTO user VALUES(?,?,?,?,?,?,?)",(name, surname ,age , sex, email, username ,password))
        self.con.commit()
        self.cur.close()
        


    
