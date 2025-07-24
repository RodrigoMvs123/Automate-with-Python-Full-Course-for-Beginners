## Automate-with-Python-Full-Course-for-Beginners

- https://www.youtube.com/watch?v=PXMJ6FS7llk 

### Extract Data from 
- https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320) 

#### Jupyter Notebook

```python
In: ! pip install pandas
In: import pandas as pd
In: simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
In: len(simpsons)
Out: 
23
In: simpsons [1]
```

| No. overall | No. in season | Title | Directed by | Written by | Original air date | Prod. code | U.S. viewers (millions) |
|-------------|---------------|-------|-------------|------------|-------------------|------------|-------------------------|
| 1 | 1 | "Simpsons Roasting on an Open Fire" | David Silverman | Mimi Pond | December 17, 1989 | 7G08 | 26.7[46] |
| 2 | 2 | "Bart the Genius" | Jon Vitti | January 14, 1990 | 7G02 | 24.5[46] |
| 3 | 3 | "Homer's Odyssey" | Wes Archer | Jay Kogen & Wallace Wolodarsky | January 21, 1990 | 7G03 | 27.5[47] |
| 4 | 4 | "There's No Disgrace Like Home" | Gregg Vanzo & Kent Butterworth | Al Jean & Mike Reiss | January 28, 1990 | 7G04 | 20.2[48] |
| 5 | 5 | "Bart the General" | David Silverman | John Swartzwelder | February 4, 1990 | 7G05 | 27.1[49] |
| 6 | 6 | "Moaning Lisa" | Wes Archer | Al Jean & Mike Reiss | February 11, 1990 | 7G06 | 27.4[50] |
| 7 | 7 | "The Call of the Simpsons" | John Swartzwelder | February 18, 1990 | 7G09 | 27.6[51] |
| 8 | 8 | "The Telltale Head" | Rich Moore | Al Jean, Mike Reiss, Sam Simon & Matt Groening | February 25, 1990 | 7G07 | 28.0[52] |
| 9 | 9 | "Life on the Fast Lane" | David Silverman | John Swartzwelder | March 18, 1990 | 7G11 | 33.5[53] |
| 10 | 10 | "Homer's Night Out" | Rich Moore | Jon Vitti | March 25, 1990 | 7G10 | 30.3[54] |
| 11 | 11 | "The Crepes of Wrath" | Wes Archer & Milton Gray | George Meyer, Sam Simon, John Swartzwelder & Jon Vitti | April 15, 1990 | 7G13 | 31.2[55] |
| 12 | 12 | "Krusty Gets Busted" | Brad Bird | Jay Kogen & Wallace Wolodarsky | April 29, 1990 | 7G12 | 30.4[56] |
| 13 | 13 | "Some Enchanted Evening" | David Silverman & Kent Butterworth | Matt Groening & Sam Simon | May 13, 1990 | 7G01 | 27.1[57] |

### Table extraction: Extract CSV files from Websites

#### Jupyter Notebook
```python
import pandas as pd
```

#### 1 - Read a CSV from a URL with Pandas
Target website: https://www.football-data.co.uk/data.php 

#### Jupyter Lite
- https://jupyter.org/try-jupyter/lab/index.html 

```python
# reading 1 csv file from the website
In:  df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
Out:

# showing dataframe
In: df_premier21
Out:

# rename columns 
In: dfpremier21.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)
# show dataframes
In: df_premier21 
Out:                                 home_goals away_goals
```

### Table extraction: Extract tables from PDF´s

#### Visual Studio Code
en-extract-pdf.py

#### Visual Studio Code Terminal
```bash
pip install tk
pip install ghostscript
pip install camelot-py
```

#### Visual Studio Code en-extract-pdf.py

```python
import camelot

tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)
```

#### Visual Studio Code Terminal 
```
<1 internal line>
<TableList n=1>
process finished with exit code 0
```

```python
import camelot

tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)

tables.export('foo.cvs', f='cvs', compress=True)
tables[0].to_csv('foo.csv')
print(tables[0].df)
```

#### foo.csv
```
Cycle Name KI (1/km) Distance (mi) Percent Fuel Savings Improved Speed Decreased Accel Eliminate Stops Decreased Idle 
2012_2 3.30 1.3 5.9% 9.5% 29.2% 17.4% 
2145_1 0.68 11.2 2.4% 0.1% 9.5% 2.7% 
4234_1 0.59 58.7 8.5% 1.3% 8.5% 3.3% 
2032_2 0.17 57.8 21.7% 0.3% 2.7% 1.2% 
4171_1 0.07 173.9 58.1% 1.6% 2.1% 0.5% 
```

- https://camelot-py.readthedocs.io/en/master/_static/pdf/foo.pdf 

### Web Automation and Web Scraping: HTML - Tags 

#### HTML Element 

- https://subslikescript.com/movie/titanic-120338 

| Tag Name | Attribute Name | Attribute Value | Affected content | End tag |
|----------|----------------|-----------------|------------------|---------|
| `<h1` | `class=` | `"title">` | `Titanic ( 1997 )` | `</h1>` |
 
#### Tags
- `<head>`
- `<body>`
- `<header>`
- `<article>`
- `<p>`: paragraph
- `<h1>`, `<h2>`, `<h3>`: heading
- `<div>` divider
- `<nav>` navigational
- `<li>` list item
- `<a>` anchor
- `<a href="http://example.com"> Text</a>`
- `<button>`
- `<table>`
- `<td>` table data
- `<tr>` table row element
- `<ul>` unordered list
- `<iframe>`

#### HTML code example

```html
<article class="main-article">
       <h1> Titanic ( 1997 ) </h1> // Title 
       <p class="plot"> 84 years later… </p> // Description 
       <div class="full-script"> 13 meters. You… </div> // Transcription
</article>
```

#### NODE
```
                                                             Root Element
                                                                <article>                 Parent Node
Element                 Attribute                     Element                                           Element Siblings
  <h1>             class="main-article"             <p>                                                  <div>
   Text                                              Attribute    Text                           Attribute               Text
Titanic(1997)                                class="plot"  84 years later class="full-script" 13 meters.You
    Title
```

### Web Automation and Web Scraping: XPath - Syntax

#### XPath Guide ( Selenium ) 
#### XPath Syntax

```xpath
// tagName
// tagName[1]
// tagName[@AttributeName="Value"]
```

contains()
start-with()

```xpath
//tagName[contains(@AttributeName, "Value")]
```

and 
or 

```xpath
// tagName[(expression 1) and (expression 2)]
```

### Web Automation and Web Scraping: XPath-Testing XPath

- https://scrapinghub.github.io/xpath-playground/ 

#### XPath Playground 

#### Input
```html
<article class="main-article">
       <h1> Titanic ( 1997 ) </h1> // Title 
       <p class="plot"> 84 years later… </p> // Description 
       <p class="plot2"> In the end </p>
       <div class="full-script"> 
               "13 meters. You should see it." 
               "Okay, take her up and over the bow rail."
       </div> // Transcription
</article>
```

#### XPath
```xpath
//h1
```
#### Result
```html
<h1> Titanic ( 1997 ) </h1>
```
#### XPath
```xpath
//h1/text()
```
#### Result
```
Titanic(1997)
```
#### XPath
```xpath
//p
```
#### Result
```html
<p class="plot"> 84 years later… </p> // Description 
<p class="plot2"> In the end </p>
```
#### XPath
```xpath
//p[1]
```
#### Result
```html
<p class="plot"> 84 years later… </p> // Description 
```
#### XPath
```xpath
//p[2]
```
#### Result
```html
<p class="plot2"> In the end </p>
```
#### XPath
```xpath
//div
```
#### Result
```html
<div class="full-script"> "
       13 meters. You should see it." 
        "Okay, take her up and over the bow rail."
</div> // Transcription
```
#### XPath
```xpath
//div/text()
```
#### Result
```
"13 meters. You should see it." 
"Okay, take her up and over the bow rail."
```
#### XPath
```xpath
//div[@class="full-script]
```
#### Result
```html
<div class="full-script"> "13 meters. You should see it." "Okay, take her up and over the bow rail."
</div> // Transcription
```
#### XPath
```xpath
//div[@class="full-script]/text()
```
#### Result
```
"13 meters. You should see it." "Okay, take her up and over the bow rail."
```
#### XPath
```xpath
//p[(@class="plot") or (@class="plot2")]
```
#### Result
```html
<p class="plot"> 84 years later… </p> // Description 
<p class="plot2"> In the end </p>
```
#### XPath
```xpath
//p[contains(@class, "plot")]
```
#### Result
```html
<p class="plot"> 84 years later… </p> // Description 
<p class="plot2"> In the end </p>
```
#### XPath
```xpath
//div[contains(@class, "script")]
```
#### Result
```html
<div class="full-script"> "13 meters. You should see it." "Okay, take her up and over the bow rail."
</div> // Transcription
```

### Web Automation and Web Scraping: XPath-Special Characters

#### Special Characters
- `/`: Select the children from the node set on the left side of this character
- `//`: Specifies that the matching node set should be located at any level within the document
- `.` : Specifies the current context should be used ( refers to present node )
- `..` : Refers to a parent node
- `*`: A wildcard character that selects all elements or attributes regardless of names
- `./*`: Select all the children nodes considering the current context
- `@`: Select an attribute
- `()`: Grouping an XPath expression
- `[n]`: Indicates that a node with index "n" should be selected

#### XPath Playground 
#### XPath
```xpath
//article
```
#### Result
```html
<article class="main-article">
       <h1> Titanic ( 1997 ) </h1> // Title 
       <p class="plot"> 84 years later… </p> // Description 
       <p class="plot2"> In the end </p>
       <div class="full-script"> 
               "13 meters. You should see it." 
               "Okay, take her up and over the bow rail."
       </div> // Transcription
</article>
```
#### XPath
```xpath
//article/h1
```
#### Result
```html
  <h1> Titanic ( 1997 ) </h1> // Title 
```
#### XPath
```xpath
//article/p
```
```html
<p class="plot"> 84 years later… </p> // Description 
<p class="plot2"> In the end </p>
```
#### XPath
```xpath
//article/div
```
#### Result
```html
<div class="full-script"> 
       "13 meters. You should see it." 
       "Okay, take her up and over the bow rail."
</div> // Transcription
```
#### XPath
```xpath
//article/h1/text()
```
#### Result
```
Titanic(1997)
```
#### XPath
```xpath
//article//text()
```
#### Result
```
Titanic(1997)
84 years later…
```
#### XPath
```xpath
//h1
```
#### Result
```html
<h1> Titanic ( 1997 ) </h1> // Title 
```
#### Xpath
```xpath
//h1/.
```
#### Result
```html
<h1> Titanic ( 1997 ) </h1> // Title
```
#### XPath
```xpath
//h1/..
```
#### Result
```html
<article class="main-article">
       <h1> Titanic ( 1997 ) </h1> // Title 
       <p class="plot"> 84 years later… </p> // Description 
       <p class="plot2"> In the end </p>
       <div class="full-script"> 
               "13 meters. You should see it." 
               "Okay, take her up and over the bow rail."
       </div> // Transcription
</article>
```
#### XPath
```xpath
//article/*
```
#### Result
```html
<h1> Titanic ( 1997 ) </h1> // Title 
       <p class="plot"> 84 years later… </p> // Description 
       <p class="plot2"> In the end </p>
 <div class="full-script"> 
        "13 meters. You should see it." 
        "Okay, take her up and over the bow rail."
</div> // Transcription
```
#### XPath
```xpath
//article/*/text()
```
#### Result
```
Titanic(1997)
83 years later…
"13 meters. You should see it." "Okay, take her up and over the bow rail."
```

### Automate the News: Installing Selenium and Chrome Driver

- https://chromedriver.chromium.org/downloads ( Download )

#### Visual Studio Code Terminal 
```bash
pip instal selenium 
```

### Automate The News: Creating the Driver

- https://www.thesun.co.uk/sport/football/ 

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
```

### Automate The News: Finding Elements

- https://www.thesun.co.uk/sport/football/ 

Inspect
Select Title and Subtitle 
Control + F
Find by string, selector or XPath 
//div[@class="teaser-item teaser__small theme-football"]
//div[@class="teaser__copy-container"]

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

for container in containers:
       title = container.find_elements(by="xpath", value='./a/span)
').text
       subtitle = container.find_elements(by="xpath", value='./a/h3').text
       link = container.find_element(by="xpath", value='./a').get_attribute("href")

# //div[@class="teaser__copy-container"]
# //div[@class="teaser__copy-container"]/a/span
# //div[@class="teaser__copy-container"]/a/h3
```

```html
<div>
<a>
<span>
<h3>
```

### Automate The News: Exporting Data to a CSV File

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles =[]
subtitles =[]
links =[]

for container in containers:
       title = container.find_elements(by="xpath", value='./a/span)
').text
       subtitle = container.find_elements(by="xpath", value='./a/h3').text
       link = container.find_element(by="xpath", value='./a').get_attribute("href")
       titles.append(title)
       subtitles.append(subtitle)
       links.append(link)

my_dict = {'title': titles, 'subtitle': subtitle, 'link': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline_csv')

driver.quit()
```

#### Visual Studio Code Terminal 
```bash
pip install pandas
```

#### Visual Studio Code Terminal
Web Browser 
User

### Automate The News: Headless mode

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles =[]
subtitles =[]
links =[]

for container in containers:
       title = container.find_elements(by="xpath", value='./a/span)
').text
       subtitle = container.find_elements(by="xpath", value='./a/h3').text
       link = container.find_element(by="xpath", value='./a').get_attribute("href")
       titles.append(title)
       subtitles.append(subtitle)
       links.append(link)

my_dict = {'title': titles, 'subtitle': subtitle, 'link': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline-headless.csv')

driver.quit()
```

### Automate The News: Preparing Script to Be Run Everyday 

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year =now.strftime(" %m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles =[]
subtitles =[]
links =[]

for container in containers:
       title = container.find_elements(by="xpath", value='./a/span)
').text
       subtitle = container.find_elements(by="xpath", value='./a/h3').text
       link = container.find_element(by="xpath", value='./a').get_attribute("href")
       titles.append(title)
       subtitles.append(subtitle)
       links.append(link)

my_dict = {'title': titles, 'subtitle': subtitle, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name) 
df_headlines.to_csv(final_path)

driver.quit()
```

- https://strftime.org/ 

### Automate The News: Convert py to exe

#### Visual Studio Code news-headlines.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year =now.strftime(" %m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = "Users/Matheus/Downloads/chromedriver"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles =[]
subtitles =[]
links =[]

for container in containers:
       title = container.find_elements(by="xpath", value='./a/span)
').text
       subtitle = container.find_elements(by="xpath", value='./a/h3').text
       link = container.find_element(by="xpath", value='./a').get_attribute("href")
       titles.append(title)
       subtitles.append(subtitle)
       links.append(link)

my_dict = {'title': titles, 'subtitle': subtitle, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name) 
df_headlines.to_csv(final_path)

driver.quit()
```

#### Visual Studio Code Terminal 
```bash
pip install pyinstaller
cd . .
cd tutorial
pyinstaller - -onefile news-headlines.py
```

exec
Terminal
dist
headline-04282022.csv

### Automate The News: Schedule Python Script with crontab ( macOS )

#### New Terminal
```bash
crontab -e
0 9 * * *
```
Command ( e k )
Drag and Drop the exec on the terminal window
```bash
0 9 * * */Users/frankandrade/PycharmProjects/automation/automation-project/2.football\ Headlines/tutorial/dist/news-headlines
```
esc ( scape )
:wq ( write quite )
#### Terminal 
```bash
crontab -l 
0 9 * * */Users/frankandrade/PycharmProjects/automation/automation-project/2.football\ Headlines/tutorial/dist/news-headlines
```

- https://crontab.guru/ 

### Automate Excel Report: Create a Pivot Table with Python

#### Visual Studio Code 1.pivot-table.py

```python
import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

df[['Gender,' 'Product Line', 'Total']]
print(df)

pivot_table = df.pivot_table(index='Gender', columns='Product Line', 
                                            value='Total', aggfunc='sum').round(0)

pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
```

```
-pivot_table()
                        columns
                        Product Line
index [ gender    Values
                        (aggfunc)
```

#### pivot_table ( Excel Sheet )
| Gender | Electronic accessories | Fashion accessories | Food and beverages | … |
|--------|------------------------|--------------------|--------------------|---|
| Female | … | | | |
| Male | … | | | |

Report 

### Automate Excel Report: Add a Barchart

#### Visual Studio Code .add-chart.py

```python
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

wb = load_workbook('pivot_table.xlsx')
sheet = wb['Report']

min.column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active. max_row

print(min.column)
print(max_column)
print(min_row)
print(max_row)

barchart = BarChart()

data = Reference(sheet, min_col=min_colomn+1, max_col=max_column, min_row=min_row, max_row=max_row)

categories = Reference(sheet, min_col=min_colomn+1, max_col=max_column, min_row=min_row+1, max_row=max_row)
barchart.add_data(data,titles_from_data=True)
barchart.set_categories(categories)

sheet.add_chart(barchart, "B12")

barchart.title = "Sales by Product Line"
barchart.style = 5
wb.save('barchart.xlsx')
```

#### Visual Studio Code Terminal
```bash
pip install openpyxl 
```

### Automate Excel Report: Write Excel Formulas with Python 

#### Visual Studio Code 3.apply-formula.py

```python
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook('pivot_table.xlsx')
sheet = wb['Report']

min.column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active. max_row

for i in range(min_column+1,max_column+1):
       letter = get_column_letter(i)
       sheet(f'{letter}{max_row+1}'] = f'=SUM({letter}{min_row+1}:{letter}{max_row})'
       sheet['{letter}{max_row+1}'].style = 'Currency'

wb.save('report.xlsx')
```

### Automate Excel Report: Format Cells

#### Visual Studio Code 4.format.py

```python
from openpyxl import load_workbook
from openpyxl.style import Font

wb = load_workbook('report.xlsx')
sheet = wb['Report']

sheet['A1'] = 'Sales Report' 
sheet['A2'] = 'January' 
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Fonte('Arial', bold=True, size=10)

wb.save('report_january.xlsx')
```

### Automate Excel Report: Convert Pivot Table to Excel Report 

#### Visual Studio Code 5.pivot-to-report.py

```python
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

# Putting together #2, #3, and #4 (input: pivot_table.xlsx + month , output: Report with barchart, formulas and format)
month = 'february'

# Read workbook and select sheet
wb = load_workbook('pivot_table.xlsx')
sheet = wb['Report']

# Active rows and columns
min_column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active.max_row

# Instantiate a barchart
barchart = BarChart()

# Locate data and categories
data = Reference(sheet, min_col=min_column+1, max_col=max_column, min_row=min_row, max_row=max_row)  # including headers
categories = Reference(sheet, min_col=min_column, max_col=min_column, min_row=min_row+1, max_row=max_row)  # not including headers

# Adding data and categories
barchart.add_data(data, titles_from_data=True)
barchart.set_categories(categories)

# Make chart
sheet.add_chart(barchart, "B12")
barchart.title = 'Sales by Product line'
barchart.style = 5  # choose the chart style

# Write multiple formulas with a for loop
for i in range(min_column+1, max_column+1):  # (B, G+1)
    letter = get_column_letter(i)
    sheet[f'{letter}{max_row + 1}'] = f'=SUM({letter}{min_row + 1}:{letter}{max_row})'
    sheet[f'{letter}{max_row + 1}'].style = 'Currency'

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = month
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save(f'report_{month}.xlsx')
```

### Automate Excel Report: Generate Reports with One Click ( py to exe )

#### Visual Studio Code 6.py-to-exe.py

```python
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# Putting together #2, #3, and #4 (input: pivot_table.xlsx + month , output: Report with barchart, formulas and format)
month = input('Introduce month: ')

# Read workbook and select sheet
input_path = os.path.join(application_path, 'pivot_table.xlsx')
wb = load_workbook(input_path)
sheet = wb['Report']

# Active rows and columns
min_column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active.max_row

# Instantiate a barchart
barchart = BarChart()

# Locate data and categories
data = Reference(sheet,
                 min_col=min_column+1,
                 max_col=max_column,
                 min_row=min_row,
                 max_row=max_row)  # including headers
categories = Reference(sheet,
                       min_col=min_column,
                       max_col=min_column,
                       min_row=min_row+1,
                       max_row=max_row)  # not including headers

# Adding data and categories
barchart.add_data(data, titles_from_data=True)
barchart.set_categories(categories)

# Make chart
sheet.add_chart(barchart, "B12")
barchart.title = 'Sales by Product line'
barchart.style = 5  # choose the chart style

# Write multiple formulas with a for loop
for i in range(min_column+1, max_column+1):  # (B, G+1)
    letter = get_column_letter(i)
    sheet[f'{letter}{max_row + 1}'] = f'=SUM({letter}{min_row + 1}:{letter}{max_row})'
    sheet[f'{letter}{max_row + 1}'].style = 'Currency'

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = month
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

output_path = os.path.join(application_path, f'report_{month}.xlsx')
wb.save(output_path)
```

#### Visual Studio Code Terminal 
```bash
pyinstaller - -onefile 6.py-to-exe.py
```

Work directory 
pivot_table.xlsx
6.py-to-exe.py ( Open with Terminal )

Introduce month: march
Work directory 
pivot_table.xlsx
report_march.xlsx
6.py-to-exe.py 

### Automate WhatsApp: Basic Automation with pywhatkit

#### Visual Studio Code Terminal
```bash
pip install pywhatkit
```

#### Visual Studio Code whatsapp-pywhatkit.py

```python
import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Test", 7, 21)
pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)

# Send message to a group
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31)
```

- https://www.whatsapp.com/download
