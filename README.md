# rest-flask

## 出现的一些问题

- `KeyError: 'migrate'`，这个问题是由于`flask-migrate`初始化时没有填充db，正确的写法是`migrate=Migrate(app,db)`
- ` Error: Can't locate revision identified by '0730427f2888'`，这个是数据库中表不一致，所以我们尽量保证一个系统一个数据库，只指定模型也是不行的，而这个表`alembic_version`是放在public模式中的
- 我们指定不同的schema，只能在具体模型中实现，所以，如果两个使用migrate的插件的系统在同一个数据库中，都会默认去public模式下插入版本表，这会产生冲突，那么合理的方式就是建立不同的数据库，一个系统一个数据库
- `6000`端口是不安全端口，最好不要使用
- 在创建app时，一定要引入一次数据库模型，否则，是无法验证更改的，建议在工厂函数中使用或是在主文件导入一次
- 直接render一个admin的模板是不行的，只能指定目录重写，在它们的视图内使用，或者是按照我的写法来，继承，但是不推荐


## 运行配置选项

`flask run --host 0.0.0.0`

`share-远程苹果事件`

`flask run -p 5010`

## 目标

- 仿造微博api制作api
- 迅速了解架构


## 心得

- flask-wtf继承自wtforms，本身是通过渲染页面，获取表单数据，那么我们如何在设计api的过程中也使用它来验证表单数据呢，这就需要我们继承wtforms，编写一个方法
- return一个错误和raise一个错误的性质是不一样的

## 帐密组合

`{"username":"johnson","password":"123456", "email":"12354@qq.com"}`


pip install httpie

` http --json --auth 12354@qq.com:123456 GET http://127.0.0.1:5008/api/tokens`
