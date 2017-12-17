
import urllib2
from bmp import BitMap,Color


def get_as_string(lst):
    lst = lst.decode()
    lst = lst.split("\n")
    total_str = "";
    for str_t in lst:
        total_str += str(str_t)
    return total_str


quota = urllib2.urlopen("https://www.random.org/quota/?format=plain").read()
print(quota)

rows = 128
cols = 128
val = 2
bmp_img = BitMap(rows,cols)
for i in range(0,rows):
    print("row:",i)
    for j in range(0,cols):
        res1 = urllib2.urlopen("https://www.random.org/strings/?num=1&len=3&max=255&digits=on&unique=on&format=plain&rnd=new").read()
        res2 = urllib2.urlopen("https://www.random.org/strings/?num=1&len=3&max=255&digits=on&unique=on&format=plain&rnd=new").read()
        res3 = urllib2.urlopen("https://www.random.org/strings/?num=1&len=3&max=255&digits=on&unique=on&format=plain&rnd=new").read()
        bmp_img.setPenColor(Color(int(res1), int(res2), int(res3)))
        bmp_img.plotPoint(i, j)

bmp_img.saveFile("my_img.bmp", compress=True)





