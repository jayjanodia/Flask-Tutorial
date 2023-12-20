# Explanation

We will be taking `Puppy Adoption` from `8. Databases` and restructuring it to be more readable

```shell
.
├── README.md
├── __pycache__
│   └── app.cpython-311.pyc
├── app.py
├── migrations
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-311.pyc
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 34dcd792bcf8_created_owners_and_puppies.py
│       └── __pycache__
│           └── 34dcd792bcf8_created_owners_and_puppies.cpython-311.pyc
├── project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   └── models.cpython-311.pyc
│   ├── data.sqlite
│   ├── models.py
│   ├── owners
│   │   ├── __pycache__
│   │   │   ├── forms.cpython-311.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── forms.py
│   │   ├── templates
│   │   │   └── owners
│   │   │       └── add_owner.html
│   │   └── views.py
│   ├── puppies
│   │   ├── __pycache__
│   │   │   ├── forms.cpython-311.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── forms.py
│   │   ├── templates
│   │   │   └── puppies
│   │   │       ├── add_puppies.html
│   │   │       ├── delete_puppies.html
│   │   │       └── list_puppies.html
│   │   └── views.py
│   ├── static # where you store CSS, JS etc
│   └── templates
│       ├── base.html
│       └── index.html
└── requirements.txt
```

`__init__.py` will contain all of the code that creates the application and the database
`base.html` usually just holds the navbar
`requirements.txt` is populated using the command: `pip freeze > requirements.txt`
