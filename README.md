# 2022+a Airbnb Backend (Django + Poetry(virtual environment / package manager) + ReactJS Version)

#### #01 Poetry

- Poetry는 Python의 현재 가장 강력한 패키지 매니저 중 하나인데 이걸 한번 써봐야겠다 지금까지는 Pipenv를 사용했는데
  이거를 한번 사용해보자. 아래 사이트에 들어가면 설치 방법부터 차근차근 보고 시작할 수 있다.

- https://python-poetry.org/docs/

```bash
poetry init (실행 명령어)

실행하면 아래처럼 뭔가를 입력함 이렇게 따라하면 됨

Package name [chyoneebnb-backend]:
Version [0.1.0]:
Description []:
Author [최치원 <cw.choiit@choechiwon-ui-MacBookPro.local>, n to skip]:
License []:  MIT
Compatible Python versions [^3.9]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no

... (작성될 파일 미리 보여주는 중)

Do you confirm generation? (yes/no) [yes] yes

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
이렇게 하면 pyproject.toml이라는 파일이 생성이 되는데 이러면 우리의 가상환경이 만들어진것
그 안에서 이제 Django를 설치해야하니 아래처럼 입력

poetry add django

이제 가상환경 안으로 들어가야 한다. 그러기 위해서는 아래와 같이 입력
poetry shell

가상환경에서 나오려면 아래와 같이 입력
exit
```

#### #02 django-admin startproject

```bash
django-admin startproject config . (현재 디렉토리에 config 폴더와 manage.py 파일을 생성)
```

###### Python OOP Basic

- _한가지 알고 가야하는것이 있는데, python의 모든 클래스 안에 있는 메소드는 첫번째 인자로 self를 받는다. 무조건 받는다. 안 주면 에러
  아래처럼 모든 메소드안에는 self라는 파라미터를 넘겨받아야 한다. 사용하든 사용하지 않든. 그리고 자바, 자바스크립트, 타입스크립트에서는 constructor라는 생성자 메소드를 파이썬에선 \_\_init\_\_으로 사용한다._

```python
class Player:

  def __init__(self, name):
    self.name = name
  def hello(self):
    print(f"hello my name is: {self.name}")
  def mannual_hello(self):
    print("hello my name is: chyonee)

chyonee = Player("chyonee")
chyonee.hello()
```

- _또 한가지 알아야 할 것이 있는데, 상속에 관한 이야기이다. 상속받은 클래스는 부모의 속성을 사용하기 위해 super()라는 메소드를 호출해야 한다.
  아래 처럼 부모의 속성을 사용하기 위해선 super()라는 메소드를 호출 (여기서 만약, 부모 클래스에서 초기화할 속성이 없다면 즉, 생성자가 없다면 굳이 super()를 사용해서 init메소드를 부를 필요가 없다 여기서는 Human에 생성자가 있으니 저렇게 해야만하는것)_

- _super()는 그냥 부모 클래스를 리턴해준다고 생각해주면 편하다. super().say_hello() 이렇게도 사용할 수 있고 자식 클래스에서 부모 클래스의 메소드를 오버라이딩을 했을 때 부모의 메소드를 사용하고 싶으면 super().부모메소드()를 자식 클래스에서 호출할 수도 있고 여튼 super()는 부모클래스를 리턴한다라고 생각하면 편하다._

```python
class Human:

  def __init__(self, name):
    self.name = name
  def say_hello(self):
    print(f"hello my name is: {self.name}")

class Player(Human):

  def __init__(self, name, age):
    super().__init__(name)
    self.age = age


chyonee = Player("chyonee", 28)
chyonee.say_hello()
```

- _그리고 dir()라는 메소드도 python에서 아주 중요한 메소드인데 얜 클래스의 속성과 메소드를 전부 보여주는 메소드이다. 그래서 dir(chyonee)라고 작성하면 chyonee라는 instance의 클래스의 모든 속성과 메소드를 보여준다. 당연히 python의 가장 상위 클래스를 모든 클래스가 상속받으니 그 가장 상위 클래스의 속성과 메소드도 다 보여준다 (그 클래스를 Object 클래스라고 함)_

#### #03 /admin

- _물론 여러번 했지만 복습차원에서 Django에서는 admin site를 제공해주고 db도 제공해주는데, 장고 서버를 실행하면 /admin 으로 갈 때 admin site가 노출된다.
  이 admin site를 사용하려면 db를 마이그레이션 해야하는데 명령어는 아래와 같다 여기서 중요한건 왜 아무것도 한 게 없는데 마이그레이션을 할까? 인데 장고는 기본적으로
  장고 세션, 데이터베이스, 어드민 패널, 장고 유저등 미리 우리를 위해서 친절하게도 많은 걸 만들어 준 상태이고 우리는 그것을 사용해야만 한다 이는 프레임워크이기 때문인데 여튼,
  장고가 이미 우리를 위해 만들어준 것들이 있고 우린 그걸 사용해야만 하기 때문에 우리가 장고 서버를 실행했을 때 장고가 만들어준 것들을 사용하기 위해 db 파일이 생성되면 우리는 그것을 마이그레이션 해야 한다._

```bash
python manage.py makemigrations
python manage.py migrage
```

#### #04 Superuser

```bash
python manage.py createsuperuser
```

#### #05 Apps

- 앱을 딱 만들기 시작하면 그 앱을 장고에 세팅하고 Model을 작성하는 방법을 묘사
- 아래는 앱을 생성하는 command
- 앱을 생성하면 config > settings.py 에서 APPS에 등록해줘야한다.

```bash
python manage.py startapp <app name>
```

#### #06 Black

```bash
poetry add --dev black --allow-prereleases
```

#### #07 User customized

#### #08 Relationship Database

#### #09 User Models

- Pillow는 ImageField를 위해서 사용해야 하는 패키지

```bash
poetry add Pillow
```

#### #10 Room Models

#### #11 Common Model for CreatedAt, UpdatedAt

#### #12 Room Admin

#### #13 Category, Experience Model

#### #14 Review Model

#### #15 Wishlist Model

#### #16 Booking Model

#### #17 Media Model

#### #18 DM Model

#### #19 Admin method, Model method

#### #20 Model method 2

#### #21 Admin actions

#### #22 Custom filter on Admin Panel

-https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/#using-a-simplelistfilter

#### #23 Django rest framework

```bash
poetry add djangorestframework
```

#### #24 Serializer of djangorestframework

#### #25 ModelViewSet

#### #26 APIView, ModelSerializer is good

#### #27 Amenity views

#### #28 Perk views

#### #29 Nested Serializer

#### #30 ModelSerializer is awesome

- ModelSerializer를 사용하면 save() method에 kwargs로 무엇을 넣든간에 그게
  모델안에 있는거면 알아서 create method를 호출할 때 집어넣어준다 ModelSerializer는 create, update method를 이미 구현해놓은 Serializer이기 때문에

#### #31 Create room with relationship fields

#### #32 ManyToMany Field added way
