//delete one
  db.teachers.deleteOne({name:"Prof. K Iyer"});

//output
{
  acknowledged: true,
  deletedCount: 1
}

//deleteMany
  db.teachers.deleteMany({});
//output
{
  acknowledged: true,
  deletedCount: 3
}

//find all
db.teachers.find()

//output
{
  _id: ObjectId('68e33dcc3a63827502152c57'),
  id: 1,
  name: 'Dr. P Mehta',
  subject: 'Physics',
  experience: 12,
  city: 'Delhi'
}
{
  _id: ObjectId('68e33dcc3a63827502152c58'),
  id: 2,
  name: 'Prof. K Iyer',
  subject: 'Mathematics',
  experience: 8,
  city: 'Chennai'
}
{
  _id: ObjectId('68e33dcc3a63827502152c59'),
  id: 3,
  name: 'Mrs. N Kapoor',
  subject: 'Computer Science',
  experience: 10,
  city: 'Hyderabad'
}
{
  _id: ObjectId('68e33dcc3a63827502152c5a'),
  id: 4,
  name: 'Mr. SP Singh',
  subject: 'Chemistry',
  experience: 6,
  city: 'Bangalore'
}

//find by field
db.teachers.find({subject:"Physics"});

//output
{
  _id: ObjectId('68e33dcc3a63827502152c57'),
  id: 1,
  name: 'Dr. P Mehta',
  subject: 'Physics',
  experience: 12,
  city: 'Delhi'
}

//create a collection called teachers

db.teachers.insertMany([
  { id: 1, name: "Dr. P Mehta", subject: "Physics", experience: 12,city:"Delhi"},
  { id: 2, name: "Prof. K Iyer", subject: "Mathematics", experience: 8,city:"Chennai"},
  { id: 3, name: "Mrs. N Kapoor", subject: "Computer Science", experience: 10,city:"Hyderabad"},
  { id: 4, name: "Mr. SP Singh", subject: "Chemistry", experience: 6,city:"Bangalore"}
])

//output
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68e33dcc3a63827502152c57'),
    '1': ObjectId('68e33dcc3a63827502152c58'),
    '2': ObjectId('68e33dcc3a63827502152c59'),
    '3': ObjectId('68e33dcc3a63827502152c5a')
  }
}

//updateone
db.teachers.updateOne(
  {name:"Mr. SP Singh"},
  {$set :{city:"Jaipur"}}
);

//output
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}



