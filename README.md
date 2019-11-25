# GeoPython Workshop

Today we will be learning about the combination of Geographic Information Systems (GIS) and python. We will be covering a lot
of topics today. This course is intended to focus on concepts. All the code is provided both in a python file and a Jupyter 
Notebook for you to learn and experiment with on your own.

## ** About Me **

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I046


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various engineering departments
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Goals for Today:

    1. Get an introduction to Python
    2. Get an introduction to GIS concepts
    3. Get introduced to Pandas/GeoPandas
    4. Look at some code!


## Python
[Python Homepage](https://www.python.org/)

If you are not familiar with python, it is a free and open source programming language that has become very popular in recent 
years. [From the python.org webpage](https://www.python.org/about/): Python is powerful, fast, plays well with others, runs
everywhere, is friendly & easy to learn, and is open. 
[From Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language): "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance." 

## Geographic Information Systems (GIS)

A Geographic Information System (GIS) is a system designed to capture, store, manipulate, analyze, manage, and present spatial 
or geographic data.

My interpretation of this: Take your data and see it on a map. Ultimately, GIS is about data visualization. There are reasons things exist where they do in the world. The spatial relationship between things matters. GIS allows you to see the patterns in your data in a way you cannot if you only look at the data in a tabular/spreadsheet view.

There are many GIS tools and applications out there both desktop and online.
[ArcGIS](https://www.esri.com/en-us/home) - The Industry Leading GIS software. Manufactured by ESRI. Available for PC/Windows machines only. ArcGIS has evolved to become a suite of softwares (think Microsoft Office). There is a desktop version (ArcGIS Pro), online version (ArcGIS Online), etc. Interfaces with many other softwares and applications but ultimately you are limited by what ESRI lets you do. Licensing is expensive.

[QGIS](https://www.qgis.org/en/site/) - QGIS is a free and open source Desktop GIS software. Available on PC, Mac, and Windows. This is a collaborative and ongoing FOSS software development project with a large user community. Integrates nicely with other Open Source GIS initiatives and libraries in existence. As far as I can tell, there is really nothing you can't do with ArcGIS that you can't do in QGIS or other FOSS tools. But there is not the same level of dedicated support, documentation, etc. around it.

[PostgreSQL](https://www.postgresql.org/) + [PostGIS](https://postgis.net/) - PostgreSQL is a free and open source relational database which can be extended using PostGIS. Using these two in combination allow you to manage your data as you would in any database and perform spatial analysis on the data as you would in a more traditional GIS software. Also interfaces nicely with Desktop GIS software.

## Python in GIS

Python is a very useful language to learn for GIS users as most (all?) GIS packages provide an interface to do analysis via scripting in python. Why?

    1. Python is free
    2. Python is flexible (supports tons of data formats) 
    3. Python allows you to plug in 3rd party softwares or applications (PostgreSQL database, GeoDjango web application)
    4. Python allows you to automate things
    5. Python allows you to build your own functionality


## Pandas
[Pandas Homepage](https://pandas.pydata.org/)

Pandas is an open source python library providing high-performance, easy-to-use data structures and data analysis tools. We will be using pandas to work with our data before feeding it into QGIS. Pandas allows us to manipulate our data before viewing it using a mapping library or a GIS desktop software. 

## GeoPandas
[GeoPandas Homepage](http://geopandas.org/)

GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. Geometric operations are performed by shapely. Geopandas further depends on fiona for file access and descartes and matplotlib for plotting.

The goal of GeoPandas is to make working with geospatial data in python easier. It combines the capabilities of pandas and shapely, providing geospatial operations in pandas and a high-level interface to multiple geometries to shapely. GeoPandas enables you to easily do operations in python that would otherwise require a spatial database such as PostGIS. 

## Which one of these tools should I use?

There are tons of tools, libraries, applications, packages, etc. out there. Which should you use? It depends:

    1. Your context aka What you need to do
    2. What you are already familiar with
    
Personally, I have used all of these that I've listed and they compliment eachother. But generally my workflow looks like this:

    - Store the data in a database (PostgreSQL)
    - Manipulate it in the database (or now in Python using GeoPandas!)
    - Automate things if needed (Python)
    - Look at it  and make pretty outputs in Desktop GIS (QGIS or ArcGIS)
    
You should develop your own workflow based on what works for you!

## Code

All the code I'm using today is available in this GitHub repository both as a python script (.py) and as a Jupyter Notebook (.ipynb)

## Future Resources

We have touched on a ton of stuff today, you can never know everything about GIS and Python. This is part of the beauty of it. Here are resources to learn more....

# Learn more Python...

-[Research Data Services Workshops](https://data.library.virginia.edu/training/). Including a Python and R series of workshops.
-[Research Data Services - Statlab](https://data.library.virginia.edu/statlab/). Get individual or small group help on statistics, software, programming, etc. projects concerning your class or labwork. Or just email [statlab@virginia.edu](statlab@virginia.edu)
-Pick up a book like [Learn Python 3 The Hard Way](https://search.lib.virginia.edu/catalog/u7434195). Available via the UVA Library!
-Take [CS 1110/1111](https://cs1110.cs.virginia.edu/). All course materials are available online for *FREE*
-[PhD+ Workshop Materials]. All course materials online for *FREE*

# Self Help Via the Internet

  * Google 
        * Ex: "How to make dictionary python"
        * Ex: "python decorators"
        
  * Stack Overflow (https://stackoverflow.com/)
        * A question/answer site for programming questions (actually, not just programming any more)
        * Not only python
        * DO NOT just ask questions, do your research first!
            * Odds are very high someone has already asked your question, especially as a novice
     
  * Youtube
        - Corey Schafer (https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
            - If you have a question about a python programming concept, Corey Schafer has covered it
     
  * Practice Python (http://www.practicepython.org/)
        * Coding challenges for programmers of all levels
        
  * Python Tutor (http://pythontutor.com/)
        * Visualize what your code is doing step-by-step
        * Has limitations once you start importing libraries
        
  * TalkPython Training (https://training.talkpython.fm/)
        * Not free
        * Really awesome courses that help you get "real world" project experience
        
 # Documentation Links
 
 * [ArcPy](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy/what-is-arcpy-.htm) (Python Module for ArcGIS)
 
 * [PyQGIS](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)
 
 * [Introduction to Geopandas](https://automating-gis-processes.github.io/CSC18/lessons/L2/geopandas-basics.html)
 
 * [Spatial Functions in R](https://cran.r-project.org/web/views/Spatial.html)
     * For R Users
     



