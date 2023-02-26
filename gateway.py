from math import ceil,floor,sqrt,copysign
# 向上取整、向下取整、开根号、输入（x，y）用y的正负代替x的正负
from pathlib import Path
# 文件操作模块
from shutil import rmtree
# 好用的文件夹删除
from zipfile import ZipFile
# 压缩包模块

def rounding(Number):
    if Number >= 0:
        Number = ceil(Number)
    else:
        Number = floor(Number)
    return Number
# 数字取整函数
def circle(r):
    global x1,y1
    x1 = copysign(sqrt(r**2 / (k**2 + 1)),cos)
    y1 = k * x1
    x1 = rounding(x1)
    y1 = rounding(y1)
# 圆相关计算
def output(x,y):
    p = Path.cwd()
    n = p/"data/gateway/functions"
    n.mkdir(exist_ok=True,parents=True)
    with open(n/"start.mcfunction","a") as f:
        f.write("setblock " + str(x) + " 100 " + str(y) + " smooth_stone_slab[type=bottom]\n")
        print("setblock " + str(x) + " 100 " + str(y) + " smooth_stone_slab[type=bottom]")
# 输出函数(主要用来生成数据包主体部分)
def Toutput(x,y):
    p = Path.cwd()
    n = p/"data/gateway/functions"
    n.mkdir(exist_ok=True,parents=True)
    with open(n/"start.mcfunction","a") as f:
        f.write("tp " + str(x) + " 100 " + str(y) + "\n")
        print("tp " + str(x) + " 100 " + str(y))
# 前置输出函数(解决游戏内部错误用的= =)
def zero():
    if y > 0:
        Toutput(0,896)
        for i in range(768,1025):
            output(0,i)
    else:
        Toutput(0,-896)
        for i in range(-1024,-767):
            output(0,i)
# 除0错误处理函数


try:
    gateway = Path.cwd()/"gateway.zip"
    gateway.unlink()
except:
    pass
# 删除原有数据包，防止后续代码报错，无法删除则捕获异常


x = int(input("x:"))
y = int(input("z:"))
versions = str(input("versions:"))
# 向用户获取输入


with open("pack.mcmeta","a") as pack:
    pack.write("""{
"pack":{
"pack_format":"""+str(versions)+""",
"description":"gateway_V1.0_by_Crystal_0404"
}
}""")
# 数据包信息文件生成


cos = x / sqrt((x**2 + y**2))
try:
    k = y / x
except:
    zero()
    with ZipFile("gateway.zip","a") as zip:
        zip.write("data/gateway/functions/start.mcfunction")
        zip.write("pack.mcmeta")
    rmtree("data")
    pack = Path.cwd()/"pack.mcmeta"
    pack.unlink()
    input("代码跑完了,回车退出")
    raise ZeroDivisionError("没啥意思，只是想强行终止程序")
# 输入预处理部分。      注：k无法被计算，则使用特殊计算，顺便打包强行终止


x1,y1 = None,None
circle(768)
x2,y2 = x1,y1
circle(1024)
# 输出两个点


if -sqrt(2) / 2 <= cos <= sqrt(2) / 2:
    if y >= 0:
        Toutput((x1 + x2) / 2,(y1 + y2) / 2)
        for y in range(y2,y1+1):
            x = y / k
            x = rounding(x)
            output(x,y)
    else:
        Toutput((x1 + x2) / 2,(y1 + y2) / 2)
        for y in range(y1,y2+1):
            x = y / k
            x = rounding(x)
            output(x,y)
else:
    if x >= 0:
        Toutput((x1 + x2) / 2,(y1 + y2) / 2)
        for x in range(x2,x1+1):
            y = k * x
            y = rounding(y)
            output(x,y)
    else:
        Toutput((x1 + x2) / 2,(y1 + y2) / 2)
        for x in range(x1,x2+1):
            y = k * x
            y = rounding(y)
            output(x,y)
# 主运算部分


with ZipFile("gateway.zip","a") as zip:
    zip.write("data/gateway/functions/start.mcfunction")
    zip.write("pack.mcmeta")
rmtree("data")
pack = Path.cwd()/"pack.mcmeta"
pack.unlink()
input("代码跑完了,回车退出")
# 整理成数据包
# BY Crystal_0404