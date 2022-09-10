# 2022+a Airbnb Backend (Django + Poetry(virtual environment / package manager) + ReactJS Version)

#01 Poetry

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
