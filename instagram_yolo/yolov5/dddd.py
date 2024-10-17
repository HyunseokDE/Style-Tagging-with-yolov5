import sqlite3 as sq3

con = sq3.connect('../django_zero_to_instagram/db.sqlite3')
cur = con.cursor()
query = "insert into content_label values (:id, :labels )"
parameters = {
    "id":2,
    "labels":2
}
cur.execute(query, parameters)
con.commit()
