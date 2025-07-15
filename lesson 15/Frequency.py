studentdata={
    'id1':{
        'name':'Daniel',
        'class':'III',
        'subjects':['chemistry','maths','history','arts']
    },'id2':{
        'name':'David',
        'class':'VIII',
        'subjects':['chemistry','maths','arts']
    },'id3':{
        'name':'Bruno',
        'class':'II',
        'subjects':['maths','history','arts']
    },'id4':{
        'name':'Daniel',
        'class':'III',
        'subjects':['chemistry','maths','history','arts']
    },'id5':{
        'name':'Daniel',
        'class':'III',
        'subjects':['chemistry','maths','history','arts']
        }
        
}
result={}
count=0
for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value
    else:
        count+=1
print(result)
print("count is ",count+1)