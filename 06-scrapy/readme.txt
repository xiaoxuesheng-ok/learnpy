http://c.biancheng.net/view/2747.html

下面大致介绍这些目录和文件的作用：
scrapy.cfg：项目的总配置文件，通常无须修改。
ZhipinSpider：项目的 Python 模块，程序将从此处导入 Python 代码。
ZhipinSpider/items.py：用于定义项目用到的 Item 类。Item 类就是一个 DTO（数据传输对象），通常就是定义 N 个属性，该类需要由开发者来定义。
ZhipinSpider/pipelines.py：项目的管道文件，它负责处理爬取到的信息。该文件需要由开发者编写。
ZhipinSpider/settings.py：项目的配置文件，在该文件中进行项目相关配置。
ZhipinSpider/spiders：在该目录下存放项目所需的蜘蛛，蜘蛛负责抓取项目感兴趣的信息。


调度器：该组件由 Scrapy 框架实现，它负责调用下载中间件从网络上下载资源。
下载器：该组件由 Scrapy 框架实现，它负责从网络上下载数据，下载得到的数据会由 Scrapy 引擎自动交给蜘蛛。
蜘蛛：该组件由开发者实现，蜘蛛负责从下载数据中提取有效信息。蜘蛛提取到的信息会由 Scrapy 引擎以 Item 对象的形式转交给 Pipeline。
Pipeline：该组件由开发者实现，该组件接收到 Item 对象（包含蜘蛛提取的信息）后，可以将这些信息写入文件或数据库中。
