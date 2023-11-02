youtube link: https://www.youtube.com/watch?v=49jkfC48KyM&ab_channel=mbosoft
github https://github.com/mbosoft/fastapi-crud

python -m venv venv
cd venv/Scripts 
. activate

pip install fastapi
python.exe -m pip install --upgrade pip

pip install uvicorn
pip list
pip freeze > requirements.txt

uvicorn main:app --reload

beanie
https://pypi.org/project/beanie/
Asynchronous Python ODM for MongoDB
pip install beanie

49:00
