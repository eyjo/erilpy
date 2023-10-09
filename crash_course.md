# Python 3 Crash Course

Fáein atriði til að koma sér af stað.

## Hvað er Python
Python er forritunarmál sem [Guido van Rossum](https://gvanrossum.github.io/) 
bjó til og gaf út 1991. Guido hafði þar áður komið að þróun á forritunarmálinu 
ABC sem ætlað var til þess að kenna forritun (í staðin fyirir BASIC og Pascal).
Hann hannaði forritunarmálið m.a. með það að leiðarljósi að það kóðinn sé 
læsilegur. Þetta er eitt af því sem einkennir Python, það er (yfirleitt) hægt 
að skilja hvað forritið gerir með því að lesa kóðann. Á þeim tíma þegar það 
var gefið út voru forrit og tól ekki jafn aðgengileg og þau eru í dag. Til 
þess að gera þetta auðvelt og aðgengilegt var Python hannað til þess að sjá 
fyrir flest öllu, grunn pakkinn inniheldur undirstöður fyrir flest 
viðfangsefni. Þess vegna er sagt að Python sé "batteries included" 
forritunarmál með vísun í að grunn pakkinn er svo yfirgripsmikill. Svo 
framarlega að þú sért með grunn pakkan uppsettan (þ.e. búið að setja upp 
CPython) ætti að vera auðvelt og aðgengilegt að forrita nánast hvað sem er, en 
jafnframt ætti að vera gaman. Gleði og gaman í tengslum við Python er ekkert grí
n, jafnvel nafnið er til marks um gamanið. Nafnið Python hefur ekkert með snáka 
tegundian að gera. Nafnið er tileinkað grín leikhópnum Monthy Python. Þess 
vegna er líka talsvert af tilvísunum í brandara og atriði frá Monthy Python. 
Til dæmis er pakka geymslan [Python Package Index](https://pypi.org/) með 
(ekki svo) leynilegt vinnuheitið CheeseShop, sem er bein tilvitnun í Monthy 
Python atriði. Að sama skapi er stundum notuð hugtök eins og "spam" og "egg" í 
sýnidæmum í staðinn fyrir merkingalausu hugtökin "foo" og "bar" sem oft annars 
eru notuð víðast hvar.

## Nokkur atriði

### Code Execution
Python forrit er ræst með því að keyra skránna sem inniheldur forritið með python 
skipuninni:
```bash
python main.py
# eða
python3 main.py
```

### REPL - Read Evaluate Print Loop
Ef engin skrá þá oppnast REPL umhverfið. Þar bíður tölvan eftir að notandi
skrifar skipun og keyrir (parsar & execute) hana svo jafnóðum. Þetta er 
skipanaviðmót líkt og þegar unnið er í skel (terminal) fyrir stýri-/skrárar- 
umhverfið eða í hugbúnaði eins og R og Matlab.

Það eru til nokkrir pakkar sem reyna að bæta þetta umhverfi og vert að nefna
- iPython
- bPython


### Notebook 
Stílabókaviðmótið er að mörgu leyti svipað og REPL, nema að skipanir eru 
hólfaðar saman og hægt að hafa (markdown) texta inná milli.
- Jupyter Notebook
- Jupyter Lab
- All the other notebooks

JuPyteR er samskeyti af Julia, Python og R. Þetta er verkefni sem spratt upp 
úr iPython verkefninu. Jupyter Lab er nýjungin frá Jupyter og er vinnu 
umhverfi þar sem hægt er að oppna Jupyter Notebook inní, jafnvel margar og 
með frekari viðbætur. VSCode getur einnig oppnað Jupyter Notebook og unnið með 
sambærilegum hætti.


# Byrjum að skrifa!
Það er fátt betra að læra en að gera hlutina sjálfur. Því er best að vera með 
opið REPL og prófa sig áfram.

1. Í skel, búið til nýja möppu og staðsetjið ykkur þar.
```bash
mkdir ~/Tilraunir
cd ~/Tilraunir
```
2. Búið til nýtt umhverfi:
```bash
python3 -m venv tilraun
```
3. Sækið pakka:
```bash
pip install scipy numpy pandas matplotlib ipython jupyter jupyterlab
```
4. Kveikið á iPython REPL viðmótinu:
```bash
ipython
```



Variables
- Truth Values - Bool
- Numeric Types - int, float, complex
- Text Sequence Type - str

Data structures
- list, tuple, set, dict
- Mutable vs. Immutable Objects


Flow control
- if x < 10:
- elif x < 5:
- else:

Loops
- for i in range(10):
- print("Hello world!")

Functions

Modules

pip

Objects & Methods

