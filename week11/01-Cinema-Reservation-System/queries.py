DROP_MOVIE_TABLE = '''DROP TABLE IF EXISTS MOVIES'''

DROP_PROJECTIONS_TABLE = '''DROP TABLE IF EXISTS PROJECTIONS'''

DROP_USERS_TABLE = '''DROP TABLE IF EXISTS USERS'''

DROP_RESERVATIONS_TABLE = '''DROP TABLE IF EXISTS RESERVATIONS'''

CREATE_MOVIE_TABLE = '''
    CREATE TABLE IF NOT EXISTS MOVIES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        RATING DECIMAL(0, 10) NOT NULL
    )
'''

CREATE_PROJECTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS PROJECTIONS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_ID INTEGER NOT NULL,
        TYPE VARCHAR(3),
        DATE TEXT NOT NULL,
        TIME TEXT NOT NULL,
        FOREIGN KEY(MOVIE_ID) REFERENCES MOVIES(ID)
    )
'''

CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        IS_ACTIVE INTEGER NOT NULL DEFAULT 0
    )
'''

CREATE_RESERVATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS RESERVATIONS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_ID INTEGER  NOT NULL,
        PROJECTION_ID INTEGER NOT NULL,
        ROW INTEGER NOT NULL,
        COL INTEGER NOT NULL,
        FOREIGN KEY(USER_ID) REFERENCES USERS(ID),
        FOREIGN KEY(PROJECTION_ID) REFERENCES PROJECTIONS(ID)
    )
'''

CREATE_MOVIE = '''INSERT INTO movies (name, rating)
                  VALUES (%s, %s);'''

LIST_MOVIES = '''SELECT * FROM movies'''

INSERT_INTO_MOVIES = '''INSERT INTO MOVIES (name, rating)
                             VALUES
                             ("The Hunger Games", 7.9),
                             ("Wreck-It Ralph", 7.8),
                             ("Her", 8.3)
                            '''

INSERT_INTO_PROJECTIONS = '''INSERT INTO PROJECTIONS (movie_id, type, date, time)
                             VALUES
                             (1, "3D", "2014-04-01", "19:10"),
                             (1, "2D", "2014-04-01", "19:00"),
                             (1, "4DX", "2014-04-02", "21:00"),
                             (3, "2D", "2014-04-05", "20:20"),
                             (2, "3D", "2014-04-02", "22:00"),
                             (2, "2D", "2014-04-02", "19:30")
                            '''


INSET_INTO_RESERVATIONS = '''INSERT INTO RESERVATIONS (user_id, projection_id, row, col)
                             VALUES
                             ("RadoRado", 1, 2, 1),
                             ("RadoRado", 1, 3, 5),
                             ("RadoRado", 1, 7, 8),
                             ("Ivo", 3, 1, 1),
                             ("Ivo", 3, 1, 2),
                             ("Mysterious", 5, 2, 3),
                             ("Mysterious", 5, 2, 4)
                            '''


GET_MOVIE_IN_PROJECTIONS = '''
SELECT ID, NAME, DATE, TIME FROM (SELECT * FROM PROJECTIONS JOIN MOVIES ON MOVIES.ID = PROJECTIONS.MOVIE_ID) WHERE MOVIE_ID=?
'''
# def _get_reservations(self, projection_id):
#         return self.cursor.execute('''SELECT row, col FROM Reservations WHERE projection_id=?''', (projection_id,))
