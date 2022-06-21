"""_summary_
_Descreption_: TQDM 4.63.1 Python module practice
_URL_:https://pypi.org/project/tqdm/
_Compatibility_: Python 3.x
_Author by_: Peter Mutter <mutter.peter@protonmail.com>
_Created by_: 2022-03-29
"""
#Szükséges csomagtelepítések:
#pip install tqdm

#Használt modulok:
from tqdm import tqdm
from time import sleep

#Példa:
for i in tqdm(range(int(9e6))):
    pass

#for i in tqdm(range(int(9e9)), ncols=7):
#    pass

for i in tqdm(range(int(9e6)), ascii=True, desc="hello"):
    pass

pbar = tqdm(total=100)
for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()

mylist = tqdm(["a", "b", "c", "d"])
for char in mylist:
    sleep(0.25)
    mylist.set_description("Processing %s" % char)