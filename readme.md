之前写了一个纯过程版本的，本版本mvc面向对象，

测试了一下， 在获取歌单的时候，速度慢了一倍，可能是对数据库连接的频繁的打开和关闭造成的




网易云音乐评论爬取，python实现

目前支持以下功能

    听众的增/查
    断点爬取某一个人的歌单里的歌的评论(也不完全正确，但是由于特殊的数据结构，理论上可以获取全部的评论。最多造成数据的冗余，但不会漏解)

一些小功能就算了吧， 算是挖坑不填😂(比如直接获取全部的歌单id，未完成)
python这块完全是就是自学，一些框架也不会，就只直接用了mvc

至于view层，就。。。。
脚(其)本(实)程(就)序(是)要(不)啥(会)界面。。。。

至于为什么要写这东西，爬评论嘛，懂得人都知道这是一个悲伤的故事
其实写的还是挺累的，这大概就是用爱发电吧



欸，我为什么不一开始就直接用java写。。。。




