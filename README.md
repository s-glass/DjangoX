# Lab - Class 29
## Project: DjangoX

Author: Sarah Glass for Python 401

- Worked at a Remo table with Anthony, Dan, Slava, Logan, and Jared.

## Overview

It is quite common to set up your Django projects the same way every time.

Some of those common tasks are…

Create a custom user
Configure static assets
Add authentication
Set up styling
Install common libraries
Wire up 3rd party development tools
Repeating these steps over and over violates the DRY (Don’t Repeat Yourself) rule. So pro developers usually create a skeleton application they use to start off their projects.

Luckily for us, there’s already a great example of such a skeleton - [DjangoX](https://github.com/wsvincent/djangox)

**Choice 2**

-Create a website using DjangoX as a template.
-Click the Use this template button on home page of DjangoX repository.

-Name your repo whatever you like.
-Create a Django app of your choosing.
-The specific functionality of the site is up to you but should have a model that makes use of get_user_model

-Delete these configuration files not needed for your project:
Pipfile
Pipfile.lock
Dockerfile
docker-compose.yml

## Links and Resources

* TA help
* Reviewing class demo.
* Links to images from Google Images search using Creative Commons licenses filter.
* Wikipedia for about content
* Base code -> DjangoX from [https://github.com/wsvincent/djangox](https://github.com/wsvincent/djangox)

## Setup

No .env requirements; gitignore invludes venv.

## How to initialize/run your application

- python manage.py runserver

## Libraries

No requirements outside of Django

## Tests

Built-in Django testing

- python manage.py test
