import numpy as np 
from tensorflow.keras.models import load_model


def makedata(l):
  res=[]
  for num in l:
    data=[0]
    val=num
    for i in range(5):
      data.append(val%10)
      val=val//10
    res.append(data)
  return res

def bound(a,b):
  res=[]
  for i,j in zip(a,b):
    res.append([i,j])
  return res

def create_answer(a,b):
    a = int(document["weight"].value)
    b = int(document["height"].value)
    model = load_model("my_model.h5")
    x=[a]
    y=[b]
    partx=makedata(x)
    party=makedata(y)
    train=np.array(bound(partx,party))
    ans=x+y
    z=makedata(ans)
    label=np.array(z)
    train=train.transpose(0, 2, 1)
    result=model.predict(train)
    result=result.flatten().astype(np.uint8)
    res=""
    flag=False
    for i in range(5):
    if (not flag) and (result[5-i]!=0):
        flag=True
    if flag:
        res+=str(result[5-i])
    rslt = document["result"]
    rslt.text = res

execute_btn = document["execute"]
execute_btn.bind("click", create_answer)