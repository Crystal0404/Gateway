# 折跃门小助手
  一个用于生成出口折跃门的程序。
  在Minecraft中，出口折跃门生成的位置是可以控制的，具体控制方法可以查看下面两个链接
  
  https://youtu.be/xo7QT3cH2k4
  
  https://www.bilibili.com/video/BV117411J7hs
  
  在Minecraft中实际操作不在坐标轴上的折跃门是非常困难的，这个程序可以生成Minecraft数据包，来帮助你控制出口折跃门生成的位置
  
  # 使用方法
  ①
  
  获取入口折跃门传送方块的X坐标与Z坐标
  
  <img width="1277" alt="image" src="https://user-images.githubusercontent.com/120556221/215429466-8591f0c7-26de-46b4-9b69-c40803de9208.png">

  ②

  按照软件提示输入X坐标与Z坐标以及versions（注：versions是数据包的版本，具体自行查阅。演示版本为1.19.2，填10）
  
  <img width="397" alt="image" src="https://user-images.githubusercontent.com/120556221/215430652-a9b5017a-7c8f-4303-a27b-09c670bfd9b7.png">

  ③
  
  随后软件会在所在路径生成一个名gateway.zip的数据包，将其放入world（你的存档）\datapacks 路径下
  
  ④
  
  进入存档输入/reload加载数据包
  
  ⑤
  
  将视距调整到合适大小（没具体测试，我调了15Chunks），输入/function gateway:start运行函数（因为游戏本身的问题，可能要多运行几次）
  
  数据包会帮你自动填充需要覆盖（填充r=768---r=1024的方块）的方块，具体如何控制出口折跃门生成请参照上面两个视频
  
  当然你必须开启作弊模式，推荐在单机存档中运行该数据包，然后使用litematica拷贝到你需要的存档。
  
   # 一些注意事项
   
   在程序所在目录不要存在名为data的文件夹和名为pack.mcmeta的文件，不然文件生成会出现错误
   
   X坐标与Z坐标均为0的时候输出的数据是错误的，因为这个位置不存在折跃门，所以这个BUG就不修了（lazy）
   
   我不知道在1.13中平滑石台阶下半部分是不是叫smooth_stone_slab[type=bottom],所以在1.13可能会出问题，如果出现了问题可以反馈给我
   
   1.13以下没有数据包emmmmmmm，那自然这个软件生成的数据包是用不了的，但我把运算结果全部打印出来了，你可以一条一条在聊天框输进去（逃），但是这个软件输出的结果在1.9+都是有效的！
   
   # 作者碎碎念
   
   这个程序其实做了挺久的，作者python萌新，这个算是第一个可以拿出手的作品，仔细看看代码还是写的很混乱的。最后附一张运行成功的效果图
   
   <img width="1280" alt="image" src="https://user-images.githubusercontent.com/120556221/215434607-ae86828f-4293-4059-a7e4-9acb5b3a31ac.png">
