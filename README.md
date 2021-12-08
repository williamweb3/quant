
the project is forked from VNPY. For easy to learn and easy to install the vnpy project. 
# 安装 installation 

you can directly download the source code. then open your termal,
then script the following command

> pip install -r requirements.txt 

> python setup.py install 

1. firstly you need to create a folder(quant) at your project, at
   this folder, there are log file or configuration file. If you're not
   sure how to config, you can simply run the main_window.py at examples
   folder, you can play with UI.
# 数据爬取
howtrader可以通过data_manager的app直接下载数据，但是这个过程比较慢，适合少量数据的更新。
如果你想批量获取数据，可以参考examples下面的download_data_demo2.py文件.

you can download the data through data_manage app, but it's pretty slow,
it just designs for small piece of data updating and strategy data
warming. If you want to download the data as soon as possible, you can
try the download_data_demo2.py or download_data_demo1.py at examples
folder by using the multi-threads for speeding.

