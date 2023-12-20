# Explanation

We will be taking `Puppy Adoption` from `8. Databases` and restructuring it to be more readable

`__init__.py` will contain all of the code that creates the application and the database
`base.html` usually just holds the navbar

```shell
.
├── README.md
├── app.py
├── migrations
├── project
│ ├── **init**.py
│ ├── base.html
│ ├── data.sqlite
│ ├── models.py
│ ├── owners
│ │ ├── forms.py
│ │ ├── templates
│ │ │ └── add_owner.html
│ │ └── views.py
│ ├── puppies
│ │ ├── forms.py
│ │ ├── templates
│ │ │ ├── add_puppies.html
│ │ │ ├── delete_puppies.html
│ │ │ └── list_puppies.html
│ │ └── views.py
│ └── static # where you store your CSS, JS, Images, Fonts, etc
└── requirements.txt
```
