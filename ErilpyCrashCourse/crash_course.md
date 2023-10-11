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
opið REPL og prófa sig áfram. Til þess að koma þessu á er best að hafa góða 
skel (terminal) til að vinna í. Ef notað er Windows er best að nota nýrri 
kosti svo sem Terminal og þá PowerShell (ekki Command Promt, það er frekar
takmarkað). Einnig er mjög gott ef tök er á að nota WSL í staðinn. 


1. Í skel, búið til nýja möppu og staðsetjið ykkur þar.
```bash
mkdir ~/Tilraunir
cd ~/Tilraunir
```
2. Búið til nýtt umhverfi:
```bash
python -m venv tilraun
# eða
python3 -m venv tilraun
```
3. Sækið pakka:
```bash
pip install scipy numpy pandas matplotlib ipython jupyter jupyterlab lxml
```
4. Kveikið á iPython REPL viðmótinu:
```bash
ipython
```
5. Grunntegundir 
```python
True
type(True)      # bool

10
type(10)        # int

1.5
type(1.5)       # float

"einn"
type("einn")    # str
```
6. Data structures
```python
[1, 2, 3]
type([1, 2, 3])     # list

(1, 2, 3)
type((1, 2, 3))     # tuple

{1, 2, 3}
type({1, 2, 3})     # set

{"einn": 1, "tveir": 2, "þrír": 3}
type({"einn": 1, "tveir": 2, "þrír": 3})    # dict
```


### Dæmi 3 tekið úr: Singh, B og Skjeret, F (2006) "Ownership relations and cooperation in the Norwegian power market".
Dreyfing á framleiðslugetu leiðrétt fyrir beinum og óbeinum fjárhagslegum eignartengslum. Þá er _net production capacity_:
$$
\begin{aligned}
\mathbf{T} & = \mathbf{X} + \mathbf{Y}, \\
\mathbf{X} & = \left[ diag(\mathbf{I} - \mathbf{\bar{A}}) (\mathbf{I} - \mathbf{A})  \mathbf{A} \right] \mathbf{K} \\
\mathbf{Y} & = diag(\mathbf{I} - \mathbf{\bar{A}}) \mathbf{K},
\end{aligned}
$$
þ.s. $\mathbf{A} = [a_{ij}]$ er fylki yfir eignarhald fyrirtkækis $i$ í fyrirtæki $j$, $\mathbf{\bar{A}} = [a_j]$ og $a_j = \sum_i a_{ij}$, og $\mathbf{K}$ er production capacity, $\mathbf{X}$ er þá capacity úthlutað fyrirtækinu frá fjárhagslegum eingartengslum og $\mathbf{Y}$ frá ytri hluthöfum.

```python
import numpy as np

A = np.matrix([[0,0.5,0], [0,0,0.5], [0,0.5,0]])
K = np.matrix([[25], [15], [0]])
I = np.identity(3)

dIA = np.diag(np.diag(I - A.sum(axis=0)))

V = dIA * A * np.linalg.inv(I - A)

X = V * K
Y = dIA * K
T = X + Y
```

### Miðgengisskráning frá Seðlabankanum:
```python
import pandas as pd

gengi = pd.read_html(
    "https://sedlabanki.is/hagtolur/opinber-gengisskraning/", 
    thousands="", 
    decimal=",")[0]

gengi

for _, gj in gengi.iterrows():
    print(f"Gjaldmiðillinn {gj.Gjaldmiðill} ({gj.Mynt}) hefur miðgengi {gj.Miðgengi}")


gengi.loc[gengi.Mynt == "EUR", "Miðgengi"]

gengi.Miðgengi[gengi.Mynt == "EUR"]


gj = {g.Mynt: g.Miðgengi for _, g in gengi.iterrows()}

gj["CZK"]

```

### Functions

```python
import pandas as pd

def get_gengi():
    tables = pd.read_html(
        "https://sedlabanki.is/hagtolur/opinber-gengisskraning/", 
        thousands="", 
        decimal=",")
    gengi = {
        gj.Mynt : gj.Miðgengi
        for _, gj
        in tables[0].iterrows()
    }
    return gengi

gengi = get_gengi()

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

