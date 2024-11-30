在Django中编写符合RESTful规范的接口，通常会使用Django REST framework（DRF），它是一个强大的、灵活的、易于使用的工具，用于构建Web API。下面我将引导你通过一些基本步骤来创建一个简单的RESTful API。

### 1. 安装Django和Django REST framework

首先，确保你已经安装了Django。然后，通过pip安装Django REST framework：

```bash
bash复制代码

pip install djangorestframework
```

### 2. 创建一个Django项目和应用

```bash
django-admin startproject myproject  
cd myproject  
python manage.py startapp myapp
```

### 3. 配置settings.py

在`myproject/settings.py`文件中，添加`rest_framework`到你的`INSTALLED_APPS`列表中：

```python
INSTALLED_APPS = [  
    ...  
    'rest_framework',  
    'myapp',  
]
```

### 4. 定义模型（Models）

在`myapp/models.py`中定义你的模型。例如，我们创建一个简单的`Person`模型：

```python
from django.db import models  
  
class Person(models.Model):  
    name = models.CharField(max_length=100)  
    age = models.IntegerField()  
  
    def __str__(self):  
        return self.name
```

然后，运行迁移来创建数据库表：

```bash
python manage.py makemigrations  
python manage.py migrate
```

### 5. 创建序列化器（Serializers）

在`myapp`目录下创建一个`serializers.py`文件，并定义一个序列化器用于将`Person`实例转换为JSON格式的数据：

```python
from rest_framework import serializers  
from .models import Person  
  
class PersonSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Person  
        fields = '__all__'
```

### 6. 创建视图（Views）

在`myapp/views.py`中，使用DRF的视图集（ViewSets）来创建API的视图：

```python
from rest_framework import viewsets  
from .models import Person  
from .serializers import PersonSerializer  
  
class PersonViewSet(viewsets.ModelViewSet):  
    queryset = Person.objects.all()  
    serializer_class = PersonSerializer
```

### 7. 配置URLs

在`myapp`目录下创建一个`urls.py`文件，然后设置你的API URL路由：

```python
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import PersonViewSet  
  
router = DefaultRouter()  
router.register(r'persons', PersonViewSet)  
  
urlpatterns = [  
    path('', include(router.urls)),  
]
```

然后，在`myproject/urls.py`中包含这个应用的URL配置：

```python
from django.contrib import admin  
from django.urls import include, path  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('api/', include('myapp.urls')),  
]
```

### 8. 运行服务器

现在，你可以运行Django开发服务器来查看你的API：

```bash
bash复制代码

python manage.py runserver
```

然后，在浏览器中访问`http://127.0.0.1:8000/api/persons/`来查看`Person`对象的列表，或使用Postman等API测试工具来执行更复杂的操作，如添加、删除和更新`Person`对象。

以上就是使用Django和Django REST framework创建一个简单的RESTful API的基本步骤。你可以根据需要扩展和自定义这些示例。