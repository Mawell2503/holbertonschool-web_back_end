# NoSQL

## Description
 A type of database system that stores & manages data

### Files
0-list_databases
show dbs >>>
show is  helper function and works specifically with mongod and list/display all databases
dbs is a keyword for database.

1-use_or_create_database
use my_db >>>
use is a helper function like show which updates what db ur utulizing
my_db is the current databse

2-insert
db.school.insert({ name: "Holberton school" }) >>>
db like stated earlier refers to your current db you selected with the use command
.school creates a collecction named school
.insert stores the data {name: "Holberton school"}

3-all
db.school.find() >>>
---
---
.find() finds data for you by scanning the collection your searching. key dif: it does not create like insert.


4-match
db.school.find({name: "Holberton school"}) >>>
---
---
same thing except that now in parantheses theres {name: "Holberton school"} so it will look specifically for that

5-count
db.school.count() >>>
---
---
count() counts wthe content of a collection

6-update
db.school.updateMany(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } }
);  >>>
---
---
update() updates data of a document
updateMany() updates data in bulk

7-delete
db.school.deleteMany({ name: "Holberton school" }) >>>
---
---
deleteMany() deletes every document thaat matches the filter

8-all.py

9-insert_school
10-update_topics
11-schools_by_topic
12-log_stats