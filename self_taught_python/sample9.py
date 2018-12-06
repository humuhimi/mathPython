import os

os.path.join("Users","humu")#これでどのpathでも動くようになる。

# with openでwithブロック内の処理が終わり次第、closeを自動的にしてくれる。

with open("sample.txt","w") as s:
    s.write("Hi from python")

my_list = []

with open("sample.txt","r") as s:
    print(s.read())
    my_list.append(s.read)
# csv

import csv

with open("sample.scv","w", newline='') as f:





