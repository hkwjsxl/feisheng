## 项目部署的相关概念

关于企业项目上线的部署流程，主要包含以下3个方面：

1. 落实并调整部署方案[1.0/2.0/3.0/]
2. 确认与完善部署环境
3. 确定部署架构与服务器节点

### 部署方案

```
1. 分析项目的产品需求文档，定好部署方案的方向
2. 分析项目开发文档，按照功能边界，设计部署的结点
3. 分析项目功能软件，合理的取舍，选符合当前业务场景的
4. 梳理项目部署涉及到的部署软件实现方案，根据上面第2点确定的结点，确定初版部署方案
5. 根据项目实际情况，调整优化并确定项目部署方案【短期内的持续方案】
```



### 部署环境

#### 个人开发环境

```
工作人员：自己
工作平台：个人笔记本、公司配的电脑
平台特点：根据公司的项目要求，环境是自己配的，团队中不同的个人开发环境可以不一样
工作内容：项目的子模块，子功能的开发和维护
完成标准：完成领导/leeder安排的内容[项目的功能子模块开发]
```

#### 公司内部服务器环境

```
工作人员：开发团队
工作平台：公司内部服务器
平台特点：服务器环境和线上的服务器环境完全一致
工作内容：项目子模块间的功能联调
完成标准：项目阶段开发、调试完成
```

#### 项目测试环境

```
工作人员：测试团队
工作平台：公司内部服务器
平台特点：服务器环境和线上的服务器环境完全一致
工作内容：项目功能/非功能/探索等测试
完成标准：项目阶段功能正常运行
```

#### 项目预发布环境

```
工作人员：运维团队
工作平台：公司线上服务器组中的一台
平台特点：服务器环境和线上的服务器环境完全一致
工作内容：特殊功能测试(比如支付)、数据压力测试、其他安全测试等
完成标准：项目阶段功能正常运行，最后一道防线
```

#### 项目生产环境

```
工作人员：运维团队
工作平台：公司线上服务器组
平台特点：标准线上的服务器环境
工作内容：代码部署和维护、记录内部架构文档
完成标准：项目正常运行
```

![image-20220913231309956](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230415211725592-1495088632.png)



### 线上项目的基本架构

单点部署：容灾性低，不够健壮。

![image-20220913232018593](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230415211725602-1636355850.png)



分布式集群架构：可用性高，容灾性强，费用不低，有较高的维护成本。

![image-20220914001718263](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230415211733831-2045679978.png)



### 服务器相关

服务器： 根据节点来衡量，计算需要多少台服务器才能承受指定的QPS【每秒请求数】访问压力。 

服务器类型：物理服务器，云服务器

并发瓶颈：

```python
短板原理[水桶原理]
1. 带宽：20M/40kb
2. 处理并发的能力[web服务器], nginx 客户端静态资源代理-> 4C4M上3-4W，Uwsgi/Gunicorn/Uvincorn -> 3000-5000
3. 数据库查询能力：
   mysql 默认最大连接数151个，最高可以达到16384个，处理QPS的能力，默认大概1000次/s 。    
   show variables like '%max_connections%';

   redis 默认是1W的连接数，最高可以配置到10W，并发处理能力与连接数有关，默认1W连接的话，5W/s。
   CONFIG GET maxclients

4. 物理服务器本身的承载能力[8核16G起步...]  【腾讯云、华为云、阿里云、网易云、百度云等等，找新手礼包】
当前项目要完整的跑起来，务必购买的服务器配置：2C4G2M
```



可以使用apache ab工具进行压测，根据短板原理得到系统的并发处理数的乐观数据。

```bash
# 安装命令：
# sudo apt install apache2-utils

# 基本使用命令
ab -n 1000 -c 100 -w https://www.luffycity.com/ >> ~/ab.html
# -n 表示本次压测的总请求执行数
# -c 表示本次压测的并发数
# -w 表示以HTML格式输出压测结果

# ab命令会创建多个并发访问线程，模拟多个访问者同时对某一URL地址进行访问。它的测试目标是基于URL的，因此，它既可以用来测试apache的负载压力，也可以测试nginx、lighthttp、tomcat、IIS等其它Web服务器的压力。
```



### 域名相关

域名要正常使用必须要绑定服务器以后，进行ICP（工信部）备案和公安部备案，否则会出现无法通过域名访问站点的情况。

服务器与域名尽量在同一家公司购买，另外服务器要备份务必要三个月以上。

热门的域名商：`.com`，`.cn`，`.net`，`.org`、`com.cn`。

域名在工信部备案的周期：首次备案15个工作日，再次备案10个工作日。

网站在公安部备案的周期：2个工作日。



| 域名等级 | 例子                                                         |
| -------- | ------------------------------------------------------------ |
| 顶级域名 | `luffycity.com`，`sina.com.cn`，`baidu.com`                  |
| 二级域名 | `www.luffycity.com`，`study.luffycity.com`，`www.sina.com.cn`，`www.baidu.com` |
| 三级域名 | `abc.www.luffycity.com`，                                    |
| 四级域名 | `pic.zhuxian.tiebai.baidu.com`                               |



#### 域名影射

```bash
114.115.200.1 api.luffycity.dabanyu.com    api服务端
114.115.200.1 www.luffycity.dabanyu.com    web客户端
```

阿里域名解析设置

https://dns.console.aliyun.com/#/dns/domainList

![image-20230416171431717](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230416171433284-1217616893.png)

![image-20230416171243510](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230416171246145-1902592323.png)



## 使用docker进行容器化集成部署

### 远程服务器更新源

更新ubuntu的apt源

```shell
sudo apt-get update
```

安装包允许apt通过HTTPS使用仓库

```shell
sudo dpkg --configure -a
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
```

添加Docker官方GPG key【这个是国外服务器地址，所以网路不好的时候，会失败！在网路好的情况下，多执行几次就没问题了，如果下一行结果不是OK，则执行多几遍】

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

设置Docker稳定版仓库

```shell
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

添加仓库后，更新apt源索引

```shell
sudo apt-get update
```

前面的准备工作完成以后，接下来安装最新版Docker CE（社区版）

```shell
sudo apt-get install -y docker-ce
```

检查Docker CE是否安装正确

```shell
sudo docker pull ubuntu:20.04
```

要获取基础镜像可以直接去官方网站上获取: https://hub.docker.com/

 

### 启动与停止

安装完成Docker后，默认已经启动了docker服务，如需手动控制docker服务的启停，可执行如下命令

```shell
# 启动docker
sudo service docker start

# 停止docker
sudo service docker stop

# 重启docker
sudo service docker restart
```

安装docker-compose，这种安装方式是基于Linux操作系统的源来决定安装版本的，所以往往版本会比较低。

```bash
apt install -y docker-compose
```



## 客户端项目部署

前端自动化项目构建工具vite提供了一个build命令给我们可以将前端项目中src目录下的所有前端资源进行打包成普通的HTML/CSS/JS，生成到项目的dist文件夹中。这个dist目录下的内容会剔除掉vite中所有的测试服务器运行相关依赖包，只保留项目本身的代码和相关文件，这样将来我们在线上服务器运行时就可以直接通过nginx来运行，而不需要依赖于vite工具。

执行build命令进行项目编译之前，先修改配置文件vite.config.js的信息，例如当前客户端的域名和api服务端的域名。`src/settings.js`，代码：

```javascript
export default {
    // api服务端所在地址
    host: "http://api.fs.hkwpro.com:8000", // 服务器地址
    // 视频更新进度的时间阈值
    seed_time: 5,
}
```

src/http/index.js，代码：

```javascript
import axios from "axios"
import settings from "../settings";

const http = axios.create({
    // timeout: 2500,                          // 请求超时，有大文件上传需要关闭这个配置
    baseURL: settings.host,                    // 设置api服务端的默认地址[如果基于服务端实现的跨域，这里可以填写api服务端的地址，如果基于nodejs客户端测试服务器实现的跨域，则这里不能填写api服务端地址]
    withCredentials: false,                    // 是否允许客户端ajax请求时携带cookie
})
```

终端下，在前端项目的根目录下，执行以下命令：

```bash
vite build
```

编译完成的内容会被保存在dist目录下，并且编译出来的项目不能直接通过file://协议来访问，只能通过http服务器的运行这个项目。同时，我们之前如果通过node进行跨域代理的话，则编译后会丢失跨域代理，此时我们就需要依靠后台实现cors代理了。

通过xftp上传dist目录到线上服务器

因为根据我们上面的部署方案，我们需要安装nginx来运行这个前端项目。



### git拉取项目到服务器

~~~shell
cd /home
git clone https://github.com/HkwJsxl/feisheng.git
~~~

### ubuntu安装yarn

（可以直接在本地打包好前端项目后，放到ubuntu中）

导入软件源的 GPG key 并且添加 Yarn APT 软件源到你的系统，运行下面的命令：

```javascript
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

一旦软件源被启用，升级软件包列表，并且安装 Yarn。

```javascript
sudo apt update
sudo apt install yarn -y
```

上面的命令同时会安装 Node.js。如果你已经通过 nvm 安装了 Node，跳过 Node.js 安装过程：

```javascript
sudo apt install --no-install-recommends yarn
```

完成之后，通过打印 Yarn 版本来验证安装过程：

```javascript
yarn --version
```



### 目录结构

服务器，目录结构：

```bash
/home/feisheng/
├── conf/
│   └── nginx/
│       └── web.conf
├── docker-compose.yml
└── fsweb/
└── fsapi/
```

远程部署服务器终端操作：

```bash
mkdir -p /home/feisheng/conf/nginx/
touch /home/feisheng/conf/nginx/web.conf
vim /home/feisheng/docker-compose.yml
```

阿里云镜像：https://cr.console.aliyun.com/cn-heyuan/instances

### 编排 nginx服务容器

拉取nginx

~~~
docker pull registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:nginx1.23.3
docker tag registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:nginx1.23.3 nginx:1.23.3
~~~

`/home/feisheng/docker-compose.yml`，代码：

```python
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default
networks:
  default:
```

`/home/feisheng/conf/nginx/web.conf`，这个文件是准备给nginx容器内部的虚拟主机配置文件

```bash
vim /home/feisheng/conf/nginx/web.conf
```

web.conf，代码：

```bash
server {
    listen       80;
    server_name  www.fs.hkwpro.com;
    # client_max_body_size    1000M;
    # root         /opt/dist;

    # client_max_body_size 20M;

    # Load configuration files for the default server block.

    location / {
        root  /home/fsweb;
        index index.html;
        # 单入口的url路径转发
        try_files $uri $uri/ /index.html;
    }
}
```

在远程部署终端启动容器服务

```bash
docker-compose -f /home/feisheng/docker-compose.yml up -d
```



## 服务端项目部署

根据我们之前分析的项目部署架构，后端需要调用`mysql、redis、elasticsearch`。因此我们需要先把这些外部软件先预装。

### 目录结构

```bash
/home/luffycity/
├── conf/
│   ├── redis/
│   │   └── master.conf
│   ├── mysql/
│   └── nginx/
│       └── web.conf
├── data/
│   ├── redis/
│   ├── elastic/
│   └── mysql/
├── docker-compose.yml
├── fsweb/
├── fsapi/
├── initdb/
│   └── feisheng.sql
├── logs/
│   └── mysql
└── plugins/
```

### 编排mysql服务容器

拉取mysql镜像

~~~
docker pull registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:mysql8.0.32

docker tag registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:mysql8.0.32 mysql:8.0.32

docker rmi registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:mysql8.0.32
~~~

在远程部署服务器上进行终端操作，创建目录结构

```bash
cd /home/feisheng
mkdir -p data/mysql logs/mysql initdb
vim /home/feisheng/docker-compose.yml
```

`/home/feisheng/docker-compose.yml`，代码：

```python
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.30
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

networks:
  default:
```



#### 把本地的数据导入到SQL文件并上传到服务器

```python
# 把本地的数据库导出到sql文件
mysqldump -uroot -proot123456 fs > fs.sql

# 将导出的sql文件复制到服务器的initdb文件夹下
```

重新启动docker-compose的容器服务

```bash
cd /home/feisheng
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d

# 注意：如果mysql容器要初始化数据库，则必须要保证在运行mysql容器之前，data目录是没有任何内容的！！！
# rm -rf /home/feisheng/data/

# 可以通过以下命令进入mysql容器
docker exec -it mysql_master mysql -uroot -proot123456
use fs;
show tables;
```



### 编排redis服务容器

拉取redis镜像

~~~
docker pull registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:redis7

docker tag registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:redis7 redis:7

docker rmi registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:redis7
~~~

创建目录和必须的文件

```bash
cd /home/feisheng
mkdir -p conf/redis data/redis/master
touch conf/redis/master.conf
vim conf/redis/master.conf
```

`conf/redis/master.conf`，主库配置文件，代码：

```bash
requirepass root123456
masterauth root123456
bind 0.0.0.0

# RDB快照
save 900 1
save 300 10
save 60 10000
dir "/data"
rdbcompression yes
dbfilename dump.rdb

# AOF日志
appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec
```

保存`redis`配置文件，并编辑`/home/luffycity/docker-compose.yml`。

```bash
cd /home/feisheng
vim /home/feisheng/docker-compose.yml
```

代码：

```python
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data

networks:
  default:
```

启动服务

```bash
docker-compose -f docker-compose.yml down

docker-compose -f docker-compose.yml up -d

# 测试
docker exec -it redis_master redis-cli -a root123456
```



### 编排elasticsearch搜索引擎服务容器

拉取es镜像

~~~
docker pull registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:elasticsearch7.17.6

docker tag registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:elasticsearch7.17.6 elasticsearch:7.17.6

docker rmi registry.cn-hangzhou.aliyuncs.com/hankewei/hkwimage:elasticsearch7.17.6
~~~

在服务器网络安全组中，开放9200,9300这2个端口

![image-20230416221427512](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230416221429864-1208771417.png)

编辑`/home/feisheng/docker-compose.yml`，

```bash
vim /home/feisheng/docker-compose.yml
```

代码：(至少2核4G的才能把es启动起来)

```python
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data

  elasticsearch_1:
    image: elasticsearch:7.17.6
    restart: always
    container_name: "elasticsearch_1"
    environment:
      - "discovery.type=single-node"
      - "bootstrap.memory_lock=true"
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "xpack.security.enabled=false"
      - "http.cors.enabled=true"
      - "http.cors.allow-origin=*"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - ./data/elastic:/usr/share/elasticsearch/data
      - ./logs/elastic:/var/log/elasticsearch
      - ./plugins:/usr/share/elasticsearch/plugins
    ports:
      - 9200:9200
    networks:
      - default

networks:
  default:
```

把`ik`分词器下载解压到`/home/feisheng/plugins/`目录下。

```bash
mkdir -p /home/feisheng/data/elastic /home/feisheng/plugins
chmod 777 /home/feisheng/data/elastic

# 下载ik中文分词插件
wget https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.17.6/elasticsearch-analysis-ik-7.17.6.zip

# 解压保存到es的插件目录
apt install unzip
unzip elasticsearch-analysis-ik-7.17.6.zip -d /home/feisheng/plugins/ik-7.17.6

# 启动服务
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d

# postman中测试访问

post http://47.120.38.34:9200/_analyze?pretty

{
  "analyzer": "ik_max_word",
  "text": "我是中国人，我来自北京。"
}
```

```bash
# 监控docker-compose的所有容器运行的日志信息
docker-compose logs -f
```

es索引的生成是要结合django项目的ORM来生成，所以暂时先不用执行其他操作，先完成django项目的部署先。



### 编排uwsgi运行服务端项目容器服务

#### 基于Dockerfile定制服务端项目镜像

##### 把feisheng服务端项目进行部署前的修改和调整

```txt
1. 本地的项目配置，保存在dev.py中，不管mysql数据库密码或者redis的地址或者配置信息都是属于开发阶段，
   项目上线以后肯定换成公司的。所以mysql数据库等信息一定会修改，因为将来还需要本地继续开发新的功能业务，
   所以不能直接修改dev.py，因此我们需要把dev.py的配置内容复制粘贴一份到pro.py中，并修改对应的配置信息，
   改成公司的。

2. 在本地开发时，我们使用的django框架运行在debug模式下的，但是项目上线采用uwsgi运行时肯定会关闭debug模式的，
   而如果关闭了debug模式，则django框架就不再提供静态文件的浏览服务，也就是之前simpleUI，drf的接
   口调试页面的css/js/图片都不能访问了。我们需要使用django提供的命令提前收集这些静态文件到项目的
   指定目录下，后面通过nginx来对外提供http浏览服务

3. 原来的drf项目是运行在python内置的提供的web服务器中，wsgiref
   在项目上线的时候，我们不能使用这个模块来提供对外服务!
   wsgiref不支持多线程多进程，本身性能不好，本身在安全性上并不完善，
   python提供wsgiref这个模块仅供学习和开发测试使用。
   runserver 不能用于生产, 改成uwsgi, gunicorn, uvicorn

4. 原来drf项目在本地开发时，其实要运行这个项目，我们是安装了很多的第三方依赖模块。
   现在项目上线了，我们也肯定需要把本地的模块同步到线上服务器！否则项目跑不起来。
   因此需要使用pip freeze > requirements.txt 把项目运行的模块列表以及它们的版本
   记录到requirements.txt文件中，然后在线上服务器对requirements.txt执行重新安装模块
```



###### 修改现有的django配置文件

在项目中复制开发配置文件dev.py 到生产配置pro.py

修改配置中的IP地址为公网地址，所有的127.0.0.1全部换成公网地址，所有域名替换成真实域名。

所有的第三方接口账号全部换成公司的账号信息。

`settings/pro.py`，代码：

```python
import sys
import datetime
from pathlib import Path

from .const_pro import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# settings配置文件移动后要将这个settings添加到环境变量中
sys.path.insert(0, BASE_DIR)
# 将所有app目录的根加入到环境变量中，后续无需更改app的引入方式
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extension'))
sys.path.insert(1, os.path.join(BASE_DIR, 'libs'))

SECRET_KEY = 'django-insecure-hzsts96!plee1awc1wli5r!z)d@7u41wyr7$ejckvb#0umb&ai'

DEBUG = False
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "simpleui",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "corsheaders",
    "ckeditor",
    "ckeditor_uploader",
    "stdimage",
    "haystack",

    "home.apps.HomeConfig",
    "user.apps.UserConfig",
    "course.apps.CourseConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "coupon.apps.CouponConfig",
    "payments.apps.PaymentsConfig",

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fsapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fsapi.wsgi.application'

# mysql配置
DATABASES = {
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'fs',
        'HOST': "%s" % MYSQL_HOST,
        'PORT': "%s" % MYSQL_PORT,
        'USER': 'fs',
        'PASSWORD': MYSQL_PASSWORD,
        'OPTIONS': {
            'charset': 'utf8mb4',  # 连接选项配置,mysql8.0以上无需配置
        },
        'POOL_OPTIONS': {  # 连接池的配置信息
            'POOL_SIZE': 10,  # 连接池默认创建的链接对象的数量
            'MAX_OVERFLOW': 10  # 连接池默认创建的链接对象的最大数量
        }
    },
    'read': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'fs',
        'HOST': "%s" % MYSQL_HOST,
        'PORT': "%s" % MYSQL_PORT,
        'USER': 'fs',
        'PASSWORD': MYSQL_PASSWORD,
        'OPTIONS': {
            'charset': 'utf8mb4',  # 连接选项配置,mysql8.0以上无需配置
        },
        'POOL_OPTIONS': {  # 连接池的配置信息
            'POOL_SIZE': 10,  # 连接池默认创建的链接对象的数量
            'MAX_OVERFLOW': 10  # 连接池默认创建的链接对象的最大数量
        }
    }
}

# 自动数据库路由
DATABASE_ROUTERS = ["fsapi.db_router.DBRouter"]

# 设置redis缓存
CACHES = {
    # 默认缓存
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://:密码@IP地址:端口/库编号",
        "LOCATION": "redis://:%s@%s:%s/0" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供给admin运营站点的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/1" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供存储短信验证码
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/2" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供存储搜索热门关键字
    "hot_word": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/3" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 提供存储购物车课程商品
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/4" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 提供存储优惠券
    "coupon": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/5" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# 设置用户登录admin站点时,记录登录状态的session保存到redis缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session保存的位置对应的缓存配置项
SESSION_CACHE_ALIAS = "session"

# haystack连接elasticsearch的配置信息
HAYSTACK_CONNECTIONS = {
    'default': {
        # haystack操作es的核心模块
        'ENGINE': 'haystack.backends.elasticsearch7_backend.Elasticsearch7SearchEngine',
        # es服务端地址
        'URL': 'http://%s:9200/' % SERVER_IP,
        # es索引仓库
        'INDEX_NAME': 'haystack',
    },
}
# 当mysqlORM操作数据库改变时，自动更新es的索引，否则es的索引会找不到新增的数据
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 地区相关
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = False  # 关闭时区转换以后，django会默认使用TIME_ZONE作为时区

# 静态路径配置
# 访问静态文件的url地址前缀
STATIC_URL = "/static/"
# 设置django的静态文件目录[手动创建]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# 访问上传文件的url地址前缀
MEDIA_URL = 'media/'
# 项目中存储上传文件的根目录[手动创建]
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 日志
LOGGING = {
    'version': 1,  # 使用的日志模块的版本，目前官方提供的只有版本1，但是官方有可能会升级，为了避免升级出现的版本问题，所以这里固定为1
    'disable_existing_loggers': False,  # 是否禁用其他的已经存在的日志功能？肯定不能，有可能有些第三方模块在调用，所以禁用了以后，第三方模块无法捕获自身出现的异常了。
    'formatters': {  # 日志格式设置，verbose或者simple都是自定义的
        'verbose': {  # 详细格式，适合用于开发人员不在场的情况下的日志记录。
            # 格式定义：https://docs.python.org/3/library/logging.html#logrecord-attributes
            # levelname 日志等级
            # asctime   发生时间
            # module    文件名
            # process   进程ID
            # thread    线程ID
            # message   异常信息
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',  # 变量格式分隔符
        },
        'simple': {  # 简单格式，适合用于开发人员在场的情况下的终端输出
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {  # 过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理流程，console或者mail_admins都是自定义的。
        'console': {
            'level': 'DEBUG',  # 设置当前日志处理流程中的日志最低等级
            'filters': ['require_debug_true'],  # 当前日志处理流程的日志过滤
            'class': 'logging.StreamHandler',  # 当前日志处理流程的核心类，StreamHandler可以帮我们把日志信息输出到终端下
            'formatter': 'simple'  # 当前日志处理流程的日志格式
        },
        # 'mail_admins': {
        #     'level': 'ERROR',                  # 设置当前日志处理流程中的日志最低等级
        #     'class': 'django.utils.log.AdminEmailHandler',  # AdminEmailHandler可以帮我们把日志信息输出到管理员邮箱中。
        #     'filters': ['special']             # 当前日志处理流程的日志过滤
        # }
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名，日志保存目录logs必须手动创建
            'filename': BASE_DIR.parent / "logs/fs.log",
            # 单个日志文件的最大值，这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 备份日志文件的数量，设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志处理的命名空间
        'django': {
            'handlers': ['console', 'file'],  # 当基于django命名空间写入日志时，调用那几个日志处理流程
            'propagate': True,  # 是否在django命名空间对应的日志处理流程结束以后，冒泡通知其他的日志功能。True表示允许
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    # 额外允许的请求头
    'jwt-token',
]

# 用户模型表
AUTH_USER_MODEL = 'user.UserInfo'

# drf配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'fsapi.extension.exceptions.custom_exception_handler',
    # 自定义认证（从上到下挨个认证）
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # jwt认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 默认分页
    "DEFAULT_PAGINATION_CLASS": "fsapi.extension.paginations.RePageNumberPagination",
}

# jwt认证相关配置项
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),  # 设置jwt的有效期，一周有效
    # 自定义载荷
    'JWT_PAYLOAD_HANDLER': 'fsapi.extension.authenticate.custom_jwt_payload_handler',
    # 自定义响应数据
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'fsapi.extension.authenticate.jwt_response_payload_handler',
    # Token的头为：jwt XXX
    "JWT_AUTH_HEADER_PREFIX": "jwt",
}

# django自定义认证
AUTHENTICATION_BACKENDS = ['fsapi.extension.authenticate.CustomAuthBackend', ]

# ckeditor上传文件路径
CKEDITOR_UPLOAD_PATH = "ckeditor/"
# ckeditor工具条配置
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full', # full 显示全部工具
        # 'toolbar': 'Basic', # Basic 显示基本工具
        'toolbar': 'Custom',  # 自定义工具条的显示数量
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Image', 'Styles', 'Format', 'Font', 'Fontsize'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Table'],
            ['RemoveFormat', 'Source']
        ],
        # 设置编辑器的高度
        'height': 130,
    },
}
# 支付宝相关配置
ALIPAY = {
    # 'gateway': 'https://openapi.alipay.com/gateway.do',   # 真实网关地址
    'gateway': 'https://openapi.alipaydev.com/gateway.do',  # 沙箱网关地址
    'appid': '2021000122613847',  # 支付应用ID
    'sign_type': 'RSA2',  # 签证的加密算法
    'debug': True,  # 沙箱模式下必须设置为True
    'verbose': True,  # 是否在调试模式下输出调试数据
    'timeout': 15,  # 请求超时时间，单位：秒
    "app_private_key_path": os.path.join(BASE_DIR, "apps/payments/keys/app_private_key.pem"),  # 应用私钥路径
    "alipay_public_key_path": os.path.join(BASE_DIR, "apps/payments/keys/alipay_public_key.pem"),  # 支付宝公钥路径
    "return_url": f"{FRONT_END_URL}/alipay",  # 同步回调结果通知地址
    "notify_url": f"{BACKEND_URL}/payments/alipay/notify",  # 异步回调结果通知地址
}

```

`settings/const_pro.py`，代码：

~~~python
import os

from django.conf import settings
# admin站点公共配置
from django.contrib import admin

# 服务器ip
SERVER_IP = "47.120.38.34"

# mysql相关
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST = SERVER_IP
MYSQL_PORT = 3306
# redis相关
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_HOST = SERVER_IP
REDIS_PORT = 6379
# 容联云短信
RONGLIANYUN = {
    "accId": '2c94811c86c00e9b0186f2873a040afa',
    "accToken": os.environ.get("RONGLIANYUNACCTOKEN"),
    "appId": '2c94811c86c00e9b0186f2873b0d0b01',
    "reg_tid": 1,  # 注册短信验证码的模板ID
    "sms_expire": 60,  # 短信有效期，单位：秒(s)
    "sms_interval": 60,  # 短信发送的冷却时间，单位：秒(s)
}

# 用户默认头像
DEFAULT_USER_AVATAR = "avatar/2023/avatar.jpg"

"""
celery相关配置
"""
# Celery异步任务队列框架的配置项[注意：django的配置项必须大写，所以这里的所有配置项必须全部大写]
# 任务队列
CELERY_BROKER_URL = 'redis://:%s@%s:%s/14' % (
    REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
)
# 结果队列
CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/15' % (
    REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
)
# 时区，与django的时区同步
CELERY_TIMEZONE = settings.TIME_ZONE
# 防止死锁
CELERY_FORCE_EXECV = True
# 设置并发的worker数量
CELERYD_CONCURRENCY = 200
# celery的任务结果内容格式
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
# 设置失败允许重试[这个慎用，如果失败任务无法再次执行成功，会产生指数级别的失败记录]
# CELERY_ACKS_LATE = True
# 每个worker工作进程最多执行500个任务被销毁，可以防止内存泄漏，500是举例，根据自己的服务器的性能可以调整数值
# CELERYD_MAX_TASKS_PER_CHILD = 500
# 单个任务的最大运行时间，超时会被杀死[慎用，有大文件操作、长时间上传、下载任务时，需要关闭这个选项，或者设置更长时间]
# CELERYD_TIME_LIMIT = 10 * 60
# 任务发出后，经过一段时间还未收到acknowledge, 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True

# 之前定时任务（定时一次调用），使用了apply_async({}, countdown=30);
# 设置定时任务（定时多次调用）的调用列表，需要单独运行SCHEDULE命令才能让celery执行定时任务：
# celery -A celeryapp.main beat，当然worker还是要启动的
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html

# from celery.schedules import crontab
# CELERY_BEAT_SCHEDULE = {
#     "send_sms1": {  # 定时任务的注册标记符[必须唯一的]
#         "task": "send_sms1",  # 定时任务的任务名称
#         "schedule": 10,  # 定时任务的调用时间，10表示每隔10秒调用一次add任务
#         # "schedule": crontab(hour=7, minute=30, day_of_week=1),  # 定时任务的调用时间，每周一早上7点30分调用一次add任务
#     }
# }


admin.AdminSite.site_header = '飞升在线'
admin.AdminSite.site_title = '飞升在线教育站点管理'

# 登录界面logo
SIMPLEUI_LOGO = '/media/backends/logo.png'
# 快速操作
SIMPLEUI_HOME_QUICK = True
# 服务器信息
SIMPLEUI_HOME_INFO = True

# 关闭simpleui内置的使用分析
SIMPLEUI_ANALYSIS = False
# 离线模式
SIMPLEUI_STATIC_OFFLINE = True
# 首页图标地址
SIMPLEUI_INDEX = 'http://www.fs.hkwpro.com/'

# 后台访问地址
BACKEND_URL = "http://api.fs.hkwpro.com:8000"
# 前端访问地址
FRONT_END_URL = 'http://www.fs.hkwpro.com'

# 保利威视频加密服务
POLYV = {
    "userId": "085a2e302a",
    "writeToken": "a1765fbd-19e4-48a9-8386-4a5802107842",
    "readToken": "12e97ba9-1c84-43b1-ba63-962cbad5824a",
    "secretkey": "yi10YtdCHd",
    "tokenUrl": "https://hls.videocc.net/service/v1/token",
}

~~~

`fsapi/db_router.py`，代码：

```python
import random


class DBRouter(object):
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return random.choice(['read', ])

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'default'

```



###### 从服务端项目中收集静态文件

当Django运行在生产环境中，我们会关闭debug调试，那么项目将不再提供静态文件的支持，需要将静态文件交给静态文件的nginx服务器来提供访问支持。

我们先收集所有静态文件。项目中的静态文件除了我们使用的上传文件之外，django本身还有自己的静态文件，如rest_framework、simpleUI、admin、ckeditor等。我们需要收集这些静态文件，集中一起放到静态文件服务器中。

**我们要将收集的静态文件放到项目的static目录中，所以先创建目录static。**

Django提供了收集静态文件的方法。先在配置文件中配置收集之后存放的目录

settings/dev.py 和settings/pro.py，追加以下代码：

```python
# 收集到的静态文件存储目录
STATIC_ROOT = BASE_DIR.parent / 'static'
```

因为目前在本地我们依然使用了dev.py配置文件通过manage.py运行项目，所以我们在本地项目收集静态文件就需要把配置信息同步到dev.py

在本地终端下feisheng根目录下执行收集命令

```shell
python manage.py collectstatic
```



###### django项目通常使用uwsgi服务器或者gunicorn来运行

uwsgi/gunicorn服务器 同步模式运行项目

uvicorn服务器 异步模式运行项目

先修改fsapi/wsgi.py，加载线上的pro配置文件：

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fsapi.settings.prod')
```

安装uwsgi 直接使用pip安装就可以了

```
sudo pip3 install uwsgi
```

安装过程中如果出现Exception: you need a C compiler to builduWSGI 是因为服务器上没有c编译器，先安装

```arduino
apt-get install gcc
```

出现错误 fatal error: Python.h: No such file or directory compilation terminated.

```
apt install python-dev
```

安装完成测试是否安装正常

```css
uwsgi --version
```

在项目根目录下创建uwsgi配置文件uwsgi.ini

```bash
touch uwsgi.ini
```

注意：在manage.py的同级目录下创建uwsgi.ini配置文件。

```ini
[uwsgi]
# 使用nginx连接时使用，Django程序所在服务器地址[反向代理】
# socket=0.0.0.0:8000
# 直接做web服务器使用，Django程序所在服务器地址
http=0.0.0.0:8000
# 项目根目录[一定要使用绝对路径，否则无法访问]
chdir=/home/feisheng/fsapi
# 项目中主应用下的wsgi.py文件的路径[相对于项目根目录]
wsgi-file=fsapi/wsgi.py
# 进程数[CPU逻辑核数]
processes=4
# 线程数[CPU线程数]
threads=4
# uwsgi服务器的角色[是否开启主进程管理模式]
master=True
# 存放进程编号的文件[相对于项目根目录]
pidfile=uwsgi.pid
# 日志文件，因为uwsgi可以脱离终端在后台运行，日志看不见。我们以前的runserver是依赖终端的[相对于项目根目录]
daemonize=uwsgi.log
# 指定依赖的虚拟环境[聚堆路径，写到虚拟环境目录名]
;virtualenv=/home/anaconda3/envs/luffycity
```

启动uwsgi服务器，必须在uwsgi.ini配置文件所在的目录中运行下面的命令

注意，在本地环境中必须先把runserver关闭

```shell
uwsgi --ini uwsgi.ini
```

停止uwsgi服务器，还可以通过使用kill命令停止

```
uwsgi --stop uwsgi.pid
```

访问项目 http://127.0.0.1:8000/nav/header/



###### 把django项目代码上传部署到服务器并使用uwsgi服务器运行

在本地导出当前虚拟环境中的模块包列表到requirements.txt文件中

```bash
pip freeze > requirements.txt

# 注意：在requirements.txt中如果有conda安装的模块以 file://开头的，务必删除，否则将来报错。
# PyMySQL @ file:///home/conda/feedstock_root/build_artifacts/pymysql_1610208984992/work
# uWSGI @ file:///home/conda/feedstock_root/build_artifacts/uwsgi_1640027751896/work

# 另外，把django-haystack==3.2.1 改为 django-haystack==3.1.1

把本地修改的文件同步到服务器上
```



##### 编写Dockerfile定制服务端项目的镜像

使用 Dockerfile之前，先切换成国内docker镜像源

```bash
mkdir -p /etc/docker
sudo vim /etc/docker/daemon.json


{
    "registry-mirrors" : [
        "https://registry.docker-cn.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://hub-mirror.c.163.com",
        "https://cr.console.aliyun.com/"
    ]
}
```

下载Miniconda3

官网：https://docs.conda.io/en/latest/miniconda.html

```bash
https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh
```

创建Dockerfile文件：

```bash
vim /home/feisheng/Dockerfile
```

`/home/feisheng/Dockerfile`，代码：

```dockerfile
FROM ubuntu:20.04
LABEL maintainer="feisheng.Edu"

ENV PYTHONUNBUFFERED 1

COPY ./Miniconda3-py38_23.1.0-1-Linux-x86_64.sh /opt/
COPY ./sources.list /etc/apt/sources.list
COPY ./fsapi /fsapi
COPY ./fsapi/requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get -y install wget \
    && mkdir /root/.conda \
    && bash /opt/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh -b \
    && rm -f /opt/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh

ENV PATH /root/miniconda3/bin:$PATH

RUN conda install pymysql -c conda-forge \
    && conda install uwsgi -c conda-forge \
    && pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && chmod -R 755 /fsapi

WORKDIR /fsapi

EXPOSE 8000

VOLUME /fsapi

```

注释版：

```python
# 设置当前镜像的基础镜像,FROM指令只能使用一次，而且在Dockerfile顶部第一个使用
FROM ubuntu:20.04
# 设置描述信息
LABEL maintainer="feisheng.Edu"
# 设置环境变量，PYTHONUNBUFFERED设置python解析器在终端下stdout错误信息，一次性输出，要不在暂存区积攒
ENV PYTHONUNBUFFERED 1

# 复制文件    容器外部:容器内部
COPY ./Miniconda3-py38_23.1.0-1-Linux-x86_64.sh /opt/
COPY ./sources.list /etc/apt/sources.list
COPY ./fsapi /fsapi
COPY ./fsapi/requirements.txt /requirements.txt
# 运行系统命令
RUN apt-get update \  # 更新源
    && apt-get -y install wget \  # 安装wget下载工具
    && mkdir /root/.conda \
    && bash /opt/Miniconda3-py38_4.10.3-Linux-x86_64.sh -b \
    && rm -f /opt/Miniconda3-py38_4.10.3-Linux-x86_64.sh  # 设置环境变量

ENV PATH /root/miniconda3/bin:$PATH  # 设置环境变量

# 给conda全局base虚拟环境安装pymysql和uwsgi
RUN conda install pymysql -c conda-forge \
    && conda install uwsgi -c conda-forge \
    # 递归安装requirements.txt中的所有依赖模块
    && pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    # 设置目录权限
    && chmod -R 755 /fsapi

# 设置进入容器的默认工作目录
WORKDIR /fsapi
# 暴露容器的端口
EXPOSE 8000
# 设置/luffycityapi目录为逻辑卷，方便创建容器时，可以把当前目录的内容映射到容器外面进行持久化存储
VOLUME /fsapi
```

```bash
vim /home/feisheng/sources.list
```

/home/feisheng/sources.list，代码：

```bash
deb http://repo.huaweicloud.com/ubuntu/ focal main restricted
deb http://repo.huaweicloud.com/ubuntu/ focal-updates main restricted
deb http://repo.huaweicloud.com/ubuntu/ focal universe
deb http://repo.huaweicloud.com/ubuntu/ focal-updates universe
deb http://repo.huaweicloud.com/ubuntu/ focal multiverse
deb http://repo.huaweicloud.com/ubuntu/ focal-updates multiverse
deb http://repo.huaweicloud.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://repo.huaweicloud.com/ubuntu focal-security main restricted
deb http://repo.huaweicloud.com/ubuntu focal-security universe
deb http://repo.huaweicloud.com/ubuntu focal-security multiverse
```

通过docker-compose启动fsapi镜像，docker-compose.yml，代码：

```yaml
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data

  api1:
    build: .
    image: fsapi:1.0.0
    container_name: api1
    restart: always
    ports:
      - 8000:8000
    networks:
      - default
    volumes:
      - ./fsapi:/fsapi
    command: >
      sh -c "uwsgi --http :8000 --workers 4 --master --enable-threads --module fsapi.wsgi"
    environment:
      - "DJANGO_SETTINGS_MODULE=fsapi.settings.prod"
      - "MYSQL_PASSWORD=root123456"
      - "REDIS_PASSWORD=root123456"
      - "RONGLIANYUNACCTOKEN=b6c417ddecb64f899a0a48e30c97b55d"
    depends_on:
      - mysql_master
      - redis_master

networks:
  default:
```

启动服务

```bash
cd /home/feisheng

docker-compose -f docker-compose.yml down

docker-compose -f docker-compose.yml up -d

# 如果有es的，等待1分钟后给elasticsearch构建索引
docker exec -it api1 python manage.py rebuild_index

# 进入api1容器内部
docker exec -it api1 /bin/bash

# 在mysql容器中导入数据
docker cp /home/feisheng/initdb/fs.sql mysql_master:/home/
docker exec -it mysql_master /bin/bash
mysql -uroot -p
root123456
use fs;
set names utf8mb4;
source /home/fs.sql
```

访问：http://api.fs.hkwpro.com:8000/home/banner/



### 使用nginx对uwsgi进行反向代理

接下来，我们就需要把api1服务端容器里面的uwsgi的运行模式从http改成socket模式。

docker-compose.yml，修改如下。

```yaml
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data


  api1:
    build: .
    image: fsapi:1.0.0
    container_name: api1
    restart: always
    ports:
      - 8000:8000
    networks:
      - default
    volumes:
      - ./fsapi:/fsapi
    command: >
      sh -c "uwsgi --socket :8000 --workers 4 --master --enable-threads --module fsapi.wsgi"
    environment:
      - "DJANGO_SETTINGS_MODULE=fsapi.settings.prod"
      - "MYSQL_PASSWORD=root123456"
      - "REDIS_PASSWORD=root123456"
      - "RONGLIANYUNACCTOKEN=b6c417ddecb64f899a0a48e30c97b55d"
    depends_on:
      - mysql_master
      - redis_master

networks:
  default:
```

修改nginx配置文件

```bash
vim /home/feisheng/conf/nginx/web.conf
```

conf/nginx/web.conf，如下：

```bash
upstream feisheng {
    server 47.120.38.34:8000;
}


server {
    listen  80;
    server_name api.fs.hkwpro.com;

    location / {
        include uwsgi_params;
        uwsgi_pass feisheng;
    }
}


server {
    listen       80;
    server_name  www.fs.hkwpro.com;
    # client_max_body_size    1000M;
    # root         /opt/dist;

    # client_max_body_size 20M;

    # Load configuration files for the default server block.

    location / {
        root  /home/fsweb;
        index index.html;
        # 单入口的url路径转发
        try_files $uri $uri/ /index.html;
    }
}


```

重启docker-compose

```bash
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d

# 在mysql容器中导入数据
docker cp /home/feisheng/initdb/fs.sql mysql_master:/home/
docker exec -it mysql_master /bin/bash
mysql -uroot -p
root123456
use fs;
set names utf8mb4;
source /home/fs.sql

# 接下来，我们直接在浏览器中，通过如下地址访问：
http://api.fs.hkwpro.com/home/nav/header/
http://www.fs.hkwpro.com/
```



### 针对后端服务器的运营站点提供静态文件的访问支持

直接让前端的nginx容器同时提供服务端静态文件的访问支持。

修改docker-compose.yml，把服务端的静态文件目录映射到nginx容器中。代码：

```python
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsapi/static:/home/fsapi/static
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data


  api1:
    build: .
    image: fsapi:1.0.0
    container_name: api1
    restart: always
    ports:
      - 8000:8000
    networks:
      - default
    volumes:
      - ./fsapi:/fsapi
    command: >
      sh -c "uwsgi --socket :8000 --workers 4 --master --enable-threads --module fsapi.wsgi"
    environment:
      - "DJANGO_SETTINGS_MODULE=fsapi.settings.prod"
      - "MYSQL_PASSWORD=root123456"
      - "REDIS_PASSWORD=root123456"
      - "RONGLIANYUNACCTOKEN=b6c417ddecb64f899a0a48e30c97b55d"
    depends_on:
      - mysql_master
      - redis_master

networks:
  default:
```

修改nginx配置文件web.conf，服务端对应的server配置项中增加一个location配置信息。conf/nginx/web.conf，如下：

```bash
upstream feisheng {
    server 47.120.38.34:8000;
}


server {
    listen  80;
    server_name api.fs.hkwpro.com;

    location / {
        include uwsgi_params;
        uwsgi_pass feisheng;
    }

    location /static {
        root /home/fsapi;
    }
}


server {
    listen       80;
    server_name  www.fs.hkwpro.com;
    # client_max_body_size    1000M;
    # root         /opt/dist;

    # client_max_body_size 20M;

    # Load configuration files for the default server block.

    location / {
        root  /home/fsweb;
        index index.html;
        # 单入口的url路径转发
        try_files $uri $uri/ /index.html;
    }
}


```

完成上面操作以后，我们可以看到当前api服务端的静态文件就提供了http正常浏览了。

```bash
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d
```

因为服务端的访问端口从8000变成了80，所以此处我们需要重新调整下客户端的`settings.js`中的url路径的值。

终端下，在前端项目的根目录下，执行以下命令：

```bash
# 删除原来的dist，重新生成，然后上传到服务器中
vite build
```

再次重启docker-compose

```bash
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d

# 在mysql容器中导入数据
docker cp /home/feisheng/initdb/fs.sql mysql_master:/home/
docker exec -it mysql_master /bin/bash
mysql -uroot -p
root123456
use fs;
set names utf8mb4;
source /home/fs.sql

# 访问（80端口）
http://api.fs.hkwpro.com/home/banner/
```



### 启动celery

关于celery的启动，因为需要依赖于django项目的。所以celery的启动自然也就和当前api容器一并运行。

修改celery的启动配置文件

```bash
vim /home/feisheng/fsapi/script/fs_celery_worker.ini
```

代码：

````ini
[program:fs_celery_worker]
# 启动命令 conda env list
command=/root/miniconda3/bin/celery -A fsapi worker -l info -n worker1
# 以管理员身份执行运行celery
user=root
numprocs=1
# 项目根目录的绝对路径，通过pwd查看
directory=/fsapi
# 项目虚拟环境
enviroment=PATH="/root/miniconda3/bin"
# 输出日志绝对路径
stdout_logfile=/fsapi/logs/celery.worker.info.log
# 错误日志绝对路径
stderr_logfile=/fsapi/logs/celery.worker.error.log
# 自动启动，开机自启
autostart=true
# 重启
autorestart=true

# 进程启动后跑了几秒钟，才被认定为成功启动，默认1
startsecs=10
# 进程结束后60秒才被认定结束
stopwatisecs=60

# 优先级
priority=999
````

```bash
vim /home/feisheng/fsapi/script/fs_celery_beat.ini
```

代码：

```ini
[program:fs_celery_beat]
# 启动命令 conda env list
command = /root/miniconda3/bin/celery -A fsapi  beat -l info
# 项目根目录的绝对路径，通过pwd查看
directory = /fsapi
# 项目虚拟环境
enviroment = PATH="/root/miniconda3/bin"
# 输出日志绝对路径
stdout_logfile = /fsapi/logs/celery.beat.info.log
# 错误日志绝对路径
stderr_logfile = /fsapi/logs/celery.beat.error.log
# 自动启动，开机自启
autostart = true
# 重启
autorestart = true

# 进程启动后跑了几秒钟，才被认定为成功启动，默认1
startsecs = 10

# 进程结束后60秒才被认定结束
stopwatisecs = 60

# 优先级
priority = 998
```

```bash
vim /home/feisheng/fsapi/script/fs_celery_flower.ini
```

代码：

```ini
[program:fs_celery_flower]
# 启动命令 conda env list
command = /root/miniconda3/bin/celery -A fsapi flower --port=5555
# 项目根目录的绝对路径，通过pwd查看
directory = /fsapi
# 项目虚拟环境
enviroment = PATH="/root/miniconda3/bin"
# 输出日志绝对路径
stdout_logfile = /fsapi/logs/celery.flower.info.log
# 错误日志绝对路径
stderr_logfile = /fsapi/logs/celery.flower.error.log
# 自动启动，开机自启
autostart = true
# 重启
autorestart = true

# 进程启动后跑了几秒钟，才被认定为成功启动，默认1
startsecs = 10

# 进程结束后60秒才被认定结束
stopwatisecs = 60

# 优先级
priority = 990
```

```bash
vim /home/feisheng/fsapi/script/supervisor.service
```

代码：

```shell
[Unit]
Description=supervisor
After=network.target

[Service]
Type=forking
ExecStart=/root/miniconda3/bin/supervisord -n -c /fsapi/script/supervisord.conf
ExecStop=/root/miniconda3/bin/supervisorctl $OPTIONS shutdown
ExecReload=/root/miniconda3/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

服务端的安全组，开放5555端口。

docker-compose，代码：

```yaml
version: '3'
services:
  nginx:
    image: nginx:1.23.3
    restart: always
    ports:
      - "80:80"
    container_name: "nginx"
    volumes:
      - ./fsapi/static:/home/fsapi/static
      - ./fsweb:/home/fsweb
      - ./conf/nginx/web.conf:/etc/nginx/conf.d/nginx.conf
    networks:
      - default

  mysql_master:
    image: mysql:8.0.32
    restart: always
    container_name: "mysql_master"
    networks:
      - default
    environment:
      - "MYSQL_ROOT_PASSWORD=root123456"
      - "MYSQL_USER=fs"
      - "MYSQL_PASSWORD=root123456"
      - "MYSQL_DATABASE=fs"
      - "TZ=Asia/Shanghai"
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --explicit_defaults_for_timestamp=true
    ports:
      - 3306:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
      - ./logs/mysql:/logs
      - ./initdb:/docker-entrypoint-initdb.d/

  redis_master:
    image: redis:7
    restart: always
    networks:
      - default
    ports:
      - "6379:6379"
    command:
      ["redis-server", "/usr/local/etc/redis/redis.conf"]
    container_name: "redis_master"
    volumes:
      - ./conf/redis/master.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis/master:/data

  elasticsearch:
    image: elasticsearch:7.17.2
    restart: always
    environment:
      - "discovery.type=single-node"
      - "bootstrap.memory_lock=true"
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "xpack.security.enabled=false"
      - "http.cors.enabled=true"
      - "http.cors.allow-origin=*"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - ./data/elastic:/usr/share/elasticsearch/data
      - ./logs/elastic:/var/log/elasticsearch
      - ./plugins:/usr/share/elasticsearch/plugins
    ports:
      - 9200:9200
    networks:
      - default


  api1:
    build: .
    image: fsapi:1.0.0
    container_name: api1
    restart: always
    ports:
      - 8000:8000
    networks:
      - default
    volumes:
      - ./fsapi:/fsapi
    command: >
      sh -c "supervisord -c script/supervisord.conf && uwsgi --socket :8000 --workers 4 --master --enable-threads --module fsapi.wsgi"
    environment:
      - "DJANGO_SETTINGS_MODULE=fsapi.settings.prod"
      - "C_FORCE_ROOT=1"
      - "MYSQL_PASSWORD=root123456"
      - "REDIS_PASSWORD=root123456"
      - "RONGLIANYUNACCTOKEN=b6c417ddecb64f899a0a48e30c97b55d"
    depends_on:
      - mysql_master
      - redis_master
      - elasticsearch
      
networks:
  default:

```

启动服务

```bash
cd /home/feisheng
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up -d

# 在mysql容器中导入数据
docker cp /home/feisheng/initdb/fs.sql mysql_master:/home/
docker exec -it mysql_master /bin/bash
mysql -uroot -p
root123456
use fs;
set names utf8mb4;
source /home/fs.sql

# 进入容器
docker exec -it api1 /bin/bash
```

## 结束
