# Django
Django Framework for Simple List and Excel

# Requirement

1. Python Version 3.6  
2. Django version 3.0 (support until 2021 April)

## Progress

| Date     |                Content                 | Comment |
| -------- | :------------------------------------: | ------: |
| 9/3-9/7  |           Prepare for change           |  6 days |
| 9/8-9/18 | Add Log in and Log out page with style |  6 days |
| 9/20     |  Add Django Generative Views on Posts  |  2 days |
|9/8-9/18  | Add Log in and Log out page with style | 10 days |
| 11/13    | Add requriement.txt for different env using this repository | N/A |
| 12/1 - 12/31 | Add table function to showing page | 1 M |

## TODO:


## Install Guide

## For coders

### Step-by-step for beginner environment setting and more

1. install python3.6 and Django 3.6 under virtualenv

to install python3.6 under linux environment  
[Install python3.6](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)

to install virtualenv  
[Setup python 3.6 enviroment with virtualenv](https://robbinespu.gitlab.io/blog/2019/07/23/Python-36-with-VirtualEnv/)

* Note that it is better to name your virtualenv as venv  
* Try to make global gitignore file beforehand  

2. make your own requriement.txt including version control

There planty of Django project in github, thought, not many project consider environment setting and frustrating for the beginner to have right nowaday support version to run the project successfully. What's more, your project can be extended if your specify your version for others to use!  

3. Create any Model change

first, you have to generate migrate file for sql(database) to run:

> python manage.py makemigrations

Then, you can make database initiation with `sqlmigrate` in django

> python manage.py sqlmigrate <your_file> <version>

You might have log such as:

```
    BEGIN;
    --
    -- Create model Category
    --
    CREATE TABLE "blog_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
    --
    -- Create model Tag
    --
    CREATE TABLE "blog_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
    --
    ...
    --
    --
    COMMIT;
```

## Trobule shotting

* Django's `django_admin` doesn't support startproject in version 3.0

Okay, first of all, I have no idea of why it doesn't support this function while Django document tutorial say it does. But the quick solution for this is to install some previous Django version, that's say version 2.2 will do the job

    $> sudo pip install Django==2.2

and `django_admin startproject <your_proj>` again you will get what you want


This project is currently underconstruction  

### Data related
- [ ] add database connection to table
- [ ] get data from mongoDB and show on table
- [ ] add query, sort, add, delete to table
- [ ] intergrate with matplotlib showing index
- [ ] Excel export/import
