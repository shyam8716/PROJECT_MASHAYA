student_id={1:"mashya",2:"id",3:"proof"}
if "id"in student_id.values():
  print("id verified")
else:
  print("id not verified")
student_name={1:"kurma",2:"varaha",3:"name"}
if student_name.get(3)=='name':
  print("name checked")
else:
  print("name not verified")