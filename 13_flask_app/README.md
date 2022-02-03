# Model View Controller (MVC) w/ Python Flask

## Frond-end Development
- HTML (HyperText Markup Language)
    >HTML is the standard markup language used to create web pages. Web browsers can read HTML files and render them into visible or audible web pages. HTML describes the structure of a website semantically along with cues for presentation, making it a markup language, rather than a programming language - [_Wikipedia_](https://en.wikipedia.org/wiki/HTML)
- CSS (Cascading StyleSheet)
    > Cascading Style Sheets (CSS) is a style sheet language used for describing the look and formatting of a document written in a markup language. Although most often used to change the style of web pages and user interfaces written in HTML - [_Wikipedia_](https://en.wikipedia.org/wiki/CSS)
- JS (JavaScript)
    > JavaScript is a high-level programming language; It was originally designed as a scripting language for websites but became widely adopted as a general-purpose programming language. JavaScript is usually found running in a web browser as interactive or automated content - [_Wikipedia_](https://en.wikipedia.org/wiki/JavaScript)
- Bootstrap
    > Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and (optionally) JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components - [_Wikipedia_](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))

## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps

Firstly, we need to install the Flask framework using `pip install flask` in the terminal.
Now within our main python page, we import the module, `from flask import Flask`.

To use flash, we first need to create an object using the class `Flask` as follows,
```python
app = Flask(__name__)
```
We can direct user to the homepage of our site using decorators,
```python
# connects the function below to the browser using a decorator
@app.route("/")
# creates a function to link our homepage
def index():
    return 'Homepage!'
```

