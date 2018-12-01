# PLD - Problem List of Dalaos

## 项目结构

```
├── index.html
├── bzoj.py
├── process.cpp
└── ...
```

## 使用说明

``bzoj.py``是爬虫代码，按提示输入您需要在[BZOJ](https://www.lydsy.com/JudgeOnline/)爬取的用户名，程序会按照做题的顺序爬取您做过的题目，运行完成后会自动生成以用户名为文件名的``.txt``文件。

``process.cpp``是网页部分生成程序，会生成以``<tr>``为单位的html表格代码到``pro.txt``。

``index.html``是网页的首页。每个大佬文件夹中有个单独的个人首页。

## 注意

1. 爬虫默认每一页爬完后停歇0.5s，可以根据需求修改
2. 个人主页中的复选框暂时无法使用、

## 更新

2018.12.1 创建项目

## TODO

-[] 爬虫更多功能支持
-[] 应用个人主页中复选框
-[] 更多大佬的做题记录

## License

MIT