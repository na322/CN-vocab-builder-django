# CN-vocab-builder-django
A simple Django web app that enables users to input a sentence or phrase in Mandarin. The app will then segment the sentence
into different groups of words/phrases while providing the pinyin, definitions and the Chinese characters in both simplified and traditional form. Users will also be able to look up past input history.

This project was started mainly as a learning experience to get familiar with the Django framework and implementing a REST API, for a separate front end application to communicate with(perhaps implemented in React.js). Also meant as a way to practise different python testing frameworks such as Behave/Lettuce and pytest.

Python libraries used: -
Django/Django-REST
jieba
pinyin
hanziconv
hanzidentifier
