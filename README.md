# 树藤 vine


## 项目介绍 Overview

树藤提供中文分词、标注、打标签、句法和语义解析、实体名识别等功能。Vine provides Chinese Natural Language Processing, including word segmentation, word tagging, syntactic and semantic parsing, named entity recognition and etc.


## 开始 Getting started


1. 项目依赖 Requirements

```

Ubuntu 16.x
Python 3.6.x
Django 2.0.7
MySQL 5.7.x

```

Vine require python 3.6+ and MySQL 5.7+, and works with both Mac OS X or Linux. While in theory it should work on Windows, it has never been tried.


2. 安装 Installation

```

source activate python3

mkvirtualenv vine

workon vine

pip install -r requirements.txt

CREATE DATABASE IF NOT EXISTS vine DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

mysql -u USER -p vine < db/init.sql


python manage.py migrate

nohup python manage.py runserver 0.0.0.0:8000  &

```

Go to `http://localhost:8000` and you'll see the Vine project's website.



## 协议 License

Vine project is released under the [MIT License](https://opensource.org/licenses/MIT).


