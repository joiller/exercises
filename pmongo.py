import pymongo

mongo=pymongo.MongoClient('localhost',27017)
db=mongo.grade
table=db.class0 #type:pymongo.collection.Collection
print(db)
print(table)
# table.insert([{'name':'小明','age':18,'sex':'m'},
#               {'name': '小鸟', 'age': 15, 'sex': 'w'},
#               {'name': '小宁', 'age': 20, 'sex': 'm'}])
# table.remove({'name':'小明'},False)
tables1=table.find()
for i in tables1:
    for key,value in i.items():
        if key != 'sex' and key != '_id':
            print(i[key],end=' ')
    print()
print('*'*10)

tables2=table.find({'age':{'$lt':18}})
for i in tables2:
    print(i['name'],i['age'])

tables3=table.find()
print('*'*10)
for i in tables3.sort('age',-1):
    print(i['name'],i['age'])

# table.update_one({'name':'小萌'},{'$set':{'name':'小宁','age':22,'sex':'w'}},False)
print('*'*10)
tables3=table.find()
for i in tables3:
    for key,value in i.items():
        if key != 'sex' and key != '_id':
            print(i[key],end=' ')
    print()