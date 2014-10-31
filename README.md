Django Antimat
==============

About
-----

Detect dirty slang in russian text and process it.

Конечно же, бороться с русской ненормативной лексикой очень сложно
и данный модуль не претендует на однозначную победу, но помочь в этой борьбе
может.

Список слов и регулярные выражения, лежащие в основе модуля, взяты
в разное время в забытых местах Интернета и, если кто-то обнаружит своё авторство,
то я с радостью это авторство укажу или удалю проприетарную часть по требованию.

В основе модуля лежат два принципа:
  * морфологический анализ слов посредством модуля
  [pymorphy2](https://pypi.python.org/pypi/pymorphy2/),
  их сопоставление с базой заранее заготовленных
  * анализ текста на основе регулярного выражения.

Можно использовать либо тот, либо другой способ.

Второй вариант работает быстрее, но менее точный. Зато работает вне Django.
Первый вариант медленнее, но его легко "обучать", добавляя слова в список.
Первый вариант также можно использовать вне Django, но Вам придется самим
разобрать базу из файла ``djantimat/fixtures/initial_data.json`` и подменить
свойство ``PymorphyProc.words`` их списком.

Модуль работает только с unicode-объектами.

Installation
------------

```bash
$ pip install djantimat
```

Dependencies
------------
[Pymorphy2](https://pypi.python.org/pypi/pymorphy2/)

Pymorph2 Method Usage
---------------------

```bash
$ python manage.py shell
```
```python
>>> from djantimat.helpers import PymorphyProc
```
Есть ли матерные слова в тексте:
```python
>>> slang_detected = PymorphyProc.test(u'Здесь текст с матерками')
```
Замена матерных слов в тексте шаблоном:
```python
>>> without_slang = PymorphyProc.replace(u'Здесь текст с матерками', repl='[xxx]')
```
Оборачивание матерных слов в тексте например тегом:
```python
>>> without_slang = PymorphyProc.wrap(u'Здесь текст с матерками', wrap=('<pre>', '</pre>',))
```

Regexp Method Usage
-------------------

```bash
$ python
```
```python
>>> from djantimat.helpers import RegexpProc
```
Есть ли матерные слова в тексте:
```python
>>> slang_detected = RegexpProc.test(u'Здесь текст с матерками')
```
Замена матерных слов в тексте шаблоном:
```python
>>> without_slang = RegexpProc.replace(u'Здесь текст с матерками', repl='[xxx]')
```
Оборачивание матерных слов в тексте например тегом:
```python
>>> without_slang = RegexpProc.wrap(u'Здесь текст с матерками', wrap=('<pre>', '</pre>',))
```
