<h1 align="center">MyManhwa</h1>

<font size="3">

MyManhwa scrapes popular scanlation and aggregator sites to get manhwa and chapter information.

## 🔨 &nbsp; Installation
Install python:
``` bash
https://www.python.org/downloads/
```

Download source file and add to your project folder
``` bash
https://github.com/Aeonss/MyManhwa/blob/master/MyManhwa.py
```

Download the requirements:
``` bash
pip install -r requirements.txt
```

## 🚀 &nbsp; Usage


Get manhwa information
``` bash
from MyManhwa import Manhwa
manhwa = Manhwa("https://www.asurascans.com/manga/8239705535-revenge-of-the-iron-blooded-sword-hound/")

# Get manhwa information

# Manhwa title
title = manhwa.title

# Manhwa description
description = manhwa.description

# Manhwa cover thumbnail
image = manhwa.image

# Manhwa rating by users
rating = manhwa.rating

# Manhwa status (ongoing, completed, dropped)
status = manhwa.status

# Manhwa type (manga, manhwa, manhua)
type = manhwa.type

# Manhwa tags (action, fantasy, etc); Result is a list of tags
tags = manhwa.tags

# Manhwa chapters links (list of chapter links)
chapters = manhwa.chapters
```

Get manhwa chapter information
``` bash
from MyManhwa import ManhwaChapter
chapter = ManhwaChapter("https://www.asurascans.com/0906168628-revenge-of-the-iron-blooded-sword-hound-chapter-2/")

# Get chapter information

# Get the chapter image urls (list of image urls)
pages = chapter.pages

# Get the manhwa name
name = chapter.name

# Get the main manhwa url
manhwa = chapter.manhwa

# Get the next chapter url
next = chapter.next

# Get the previous chapter url
prev = chapter.prev

```


## 🌐 &nbsp; Supported Sites
<table>
<thead valign="bottom">
<tr>
    <th>Site</th>
    <th>URL</th>
    <th>Theme</th>
</tr>
</thead>
<tbody valign="top">
<tr>
    <td>AsuraScans</td>
    <td>https://www.asuratoon.com/</td>
    <td>MangaStream</td>
</tr>
<tr>
    <td>FlameScans</td>
    <td>https://flamecomics.com/</td>
    <td>MangaReader</td>
</tr>
<tr>
    <td>ReaperScans</td>
    <td>https://reaperscans.com/</td>
    <td></td>
</tr>
<tr>
    <td>Void-Scans</td>
    <td>https://void-scans.com/</td>
    <td>MangaStream</td>
</tr>
<tr>
    <td>Toonily</td>
    <td>https://toonily.com/</td>
</tr>
</tbody>
</table>

## 📘 &nbsp; License
MyManhwa is released under the [MIT license](https://github.com/Aeonss/MyManhwa/blob/master/LICENSE.md).

</font>