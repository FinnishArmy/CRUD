<h1 align="center"> CRUD in Python </h1>
<p align="center"> Developing CRUD in Python and MongoDB </p>

## Table of Contents
---
- [About the Project](#about-the-project)
- [Motivation](#motivation)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Code Examples](#code-examples)
- [Tests](#tests)
- [Roadmap](#roadmap--features)

## About the project
The purpose of this project is to implement the fundamental operations of CRUD (creating, reading, update, delete) in Python.

## Motivation
The reason behind creating this was to learn how to create Python modules and use them in a test script as well as getting to understand MongoDB in depth. Lastly, it was created to learn about and implement best practices for creating your own README files.

## Getting Started
To get a local copy up and running, follow these simple example steps.

1. Clone the repository with the following command:
   - `https://github.com/FinnishArmy/CRUD.git`

2. Within CRUD.py, edit the connection variables accordingly to access your own database and user.
   - `USER = 'aacuser'`
   - `PASS = 'SNHU1234'`
   - `HOST = 'nv-desktop-services.apporto.com'`
   - `PORT = 34419`
   - `DB   = 'AAC'`
   - `COL  = 'animals'`

3. Use `mongoimport` to import your desired Database into your MongoDB instance.
4. To test the module, run `python crud_test_script.ipynb`.
5. You can import the module with `from crud_module import AnimalShelter`.

## Installation
* Python 3.7 or later
+ You must use this as the runtime for the CRUD module and test scripts.
* PyMongo
+ Python Driver for MongoDB to execute CRUD operations on the database.
* Git
+ To close the repo from Github.
* Jupyter Notebook
+ This is to run the test script(s). However you may use your own IDE.

## Usage
Follow these code examples to help run the scripts.

### Code Examples
#### Set login details
<img width="1089" height="179" alt="image" src="https://github.com/user-attachments/assets/19aca942-e2e9-4763-8b4a-cb76afe015b2" />

#### Setup MongoDB Interface
<img width="1089" height="441" alt="image" src="https://github.com/user-attachments/assets/e01a55d8-bb34-41a4-87e8-07002bf8c3f8" />

#### When running the test script, you should be able to add a new entry and receive this output
<img width="1086" height="176" alt="image" src="https://github.com/user-attachments/assets/0a8d01ea-9778-430c-826f-9ebe537b19f5" />

#### When deleting an entry you should recieve this output
<img width="1092" height="136" alt="image" src="https://github.com/user-attachments/assets/b7dfb187-905b-46cb-9652-49e6f086c7fd" />

### Tests
#### Check to ensure you can read all documents
<img width="895" height="223" alt="image" src="https://github.com/user-attachments/assets/84f60bcc-c027-4fc3-ab6a-c4615cfbc243" />

### Roadmap / Features
Feature releases of this project will have:
* Ability to Update an entry.

### Contact
Ronny Z. Valtonen






