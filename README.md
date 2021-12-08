# 安装 installation 
直接在终端输入:
> pip install git+https://github.com/williamquant/quant.git

you can use pip to install the howtrader.

> pip install git+https://github.com/williamquant/quant.git 

if you encounter the error with --use-feature=2020-resolver, you can
solve with the following command: 
> pip install git+https://github.com/williamquant/quant.git --use-feature=2020-resolver

如果安装报错，可能各个包之间存在冲突，可以通过以下命令解决:
> pip install git+https://github.com/williamquant/quant.git --use-feature=2020-resolver


或者你直接把代码下载下来，然后切换到你的虚拟环境，或者使用当前的环境也是可以的，
在终端输入：

> pip install -r requirements.txt 

> python setup.py install 

or you can directly download the source code. then open your termal,
then script the following command

> pip install -r requirements.txt 

> python setup.py install 


# 更新版本 update
直接在终端输入: 

> pip install git+https://github.com/williamquant/quant.git -U 



# 使用 Usage
你需要在项目下面创建一个文件夹加，quant, 这个主要是存放一些日记和配置文件的信息。
如果不不知道配置文件如何配置，你可以启动examples文件目录下面的main_window.py文件，就可以看到其下面的一些日志和配置文件信息了。

# 数据爬取
如果你想批量获取数据，可以参考examples下面的download_data_demo2.py文件.

