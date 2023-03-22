# BS4-Flask-WeatherApp

# BeautifullSoup
![Capture](https://user-images.githubusercontent.com/107461719/226921624-086e3c61-4653-485a-bdf1-9623405ab3f5.PNG)

- Beautiful Soup is a Python library for pulling data out of HTML and XML files
- Installlation

 pip install bs4
```python
from bs4 import BeautifulSoup
```

- if we need some page then fisrt get some url using requests modul



## Access Atributs :
```python
    res = requests.get(url)
    soup = bfs(res.text, 'html.parser')
```
- soup.p['class'] # in paragraph find class for only one 
- soup.find_all('span') # find all span tags in html
- soup.prettify() # user for html Attractive 

best way :
- find tree vise (IMP for all Loops ) :
```python
    soup.find('Tag', {"class": "class_name"})
```
- find data usin data atribute :

```python
    soup.find(attrs={'data-testid':'MoonriseTime'})
```


for lopping:
- find all same class name items for length of loop 
- use find_all method to find all 
- if we add text then only give then but we dont add text then full html tag retrn 
