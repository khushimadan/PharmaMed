import pickle
import os

file=open("PharmaMed.dat","wb")
pickle.dump({"Medicine Name": "Paracetamol","Prescribed by":"Dr.Gaba","Dosage": "1-2 tablets/day","Expiry Date":"02/04/23","Price":10.00,"Discount":0},file)
pickle.dump({"Medicine Name": "T-Minic Syrup","Prescribed by":"Dr.Roshni Mahajan","Dosage": "3 times/day","Expiry Date":"07/05/24","Price":100.00,"Discount":0},file)
pickle.dump({"Medicine Name": "Wincold Z","Prescribed by":"Dr.Ajit Tiwari","Dosage": "1 tablet/day","Expiry Date":"01/01/24","Price":30.00,"Discount":0},file)
pickle.dump({"Medicine Name": "Xantox glo","Prescribed by":"Dr.Radha Sharma","Dosage": "3 times a week","Expiry Date":"01/11/23","Price":1062.50,"Discount":15.00},file)
pickle.dump({"Medicine Name": "Tendocel","Prescribed by":"Dr.Sumit Kumar","Dosage": "2 tablets/day","Expiry Date":"12/12/24","Price":313.65,"Discount":15.00},file)
file.close()

def Add():
  with open("PharmaMed.dat","ab") as f:
    mname=input("Enter Medicine Name:")
    doctor=input("Enter Name of the Doctor:")
    dosage=input("Enter Dosage of the Medicine:")
    expiry=input("Enter Expiry Date (dd/mm/yy):")
    price=float(input("Enter Price:"))
    discount=float(input("Enter Discount Offered (if any)"))
    dict1={"Medicine Name":mname,"Prescribed By":doctor,"Dosage":dosage,"Expiry Date":expiry,"Price":price,"Discount":discount}
    pickle.dump(dict1,f)
    print("Record has been saved!")

def Display():
  with open("PharmaMed.dat","rb") as f:
    while f:
      try:
        rec=pickle.load(f)
        print(rec)
      except:
        break

def Modify(searchname,n):
  dict1={}
  found=False
  with open("PharmaMed.dat","rb+") as f:
    while True:
      pos=f.tell()
      try:
        dict1=pickle.load(f)
        if dict1['Medicine Name']==searchname:
          found=True
          dict1['Price']=n
          f.seek(pos)
          pickle.dump(dict1,f)
          print("Record has been modified!")
      except EOFError:
        if found==False:
          print("No Record Found")
        break

def Delete(search):
  oldfile=open("PharmaMed.dat","rb")
  newfile=open("Newfile.dat","ab")
  while True:
    try:
      rec=pickle.load(oldfile)
      if rec["Medicine Name"]==search:
        pass
      else:
        pickle.dump(rec,newfile)
    except EOFError:
      break
  oldfile.close()
  newfile.close()
  os.remove("PharmaMed.dat")
  os.rename("Newfile.dat","PharmaMed.dat")
  print("Record has been deleted!")

#main
ans='y'
while ans in 'yY':
  print("Enter 1 to Add data to the existing records")
  print("Enter 2 to Display all the records")
  print("Enter 3 to Modify an existing record")
  print("Enter 4 to Delete an existing record")
  n=int(input("Enter your choice:"))
  if n==1:
    Add()
  elif n==2:
    Display()
  elif n==3:
    searchname=input("Enter name of the medicine whose price you would like to modify:")
    n=float(input("Enter the new price of the medicine:"))
    Modify(searchname,n)
  elif n==4:
    search=input("Enter name of the medicine whose data you would like to delete from the records:")
    Delete(search)
  else:
    print("Wrong input!")
  ans=input("Would you like to continue? (y/n)")

