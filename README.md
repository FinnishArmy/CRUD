<h1 align="center"> CRUD in Python </h1>
<p align="center"> Developing CRUD in Python and MongoDB </p>

<img width="1354" height="485" alt="image" src="https://github.com/user-attachments/assets/1d6d019f-e9e6-4bb5-ac44-0e257610d0f4" />



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
The purpose of this project is to implement the fundamental operations of CRUD (creating, reading, update, delete) in Python. Having this knowledge will give you the ability to begin manipulation of various MongoDB databases using Python.

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
### Description of drivers
* Python 3.7 or later
   + You must use this as the runtime for the CRUD module and test scripts.
* PyMongo
   + Python Driver for MongoDB to execute CRUD operations on the database.
* Git
   + To close the repo from Github.
* Jupyter Notebook
   + This is to run the test script(s). However you may use your own IDE.
 
### Attributes
* C - Create: Making a new entry in the database.
* R - Read: Given a specific query, return the details in a list.
* U - Update: Given a specific query, update the details of that entry.
* D - Delete: Remove an entry.

## Usage
Follow these code examples to help run the scripts.

### Code Examples
#### Import the database
<img width="1087" height="360" alt="image" src="https://github.com/user-attachments/assets/b388e8d4-6bcd-4129-9567-e53e8132f06a" />

#### Set login details
<img width="1089" height="179" alt="image" src="https://github.com/user-attachments/assets/19aca942-e2e9-4763-8b4a-cb76afe015b2" />

#### Setup MongoDB Interface
<img width="1089" height="441" alt="image" src="https://github.com/user-attachments/assets/e01a55d8-bb34-41a4-87e8-07002bf8c3f8" />

#### Create a new user account
<img width="1088" height="283" alt="image" src="https://github.com/user-attachments/assets/592940b0-f8c8-4aee-aff2-7f9f854e9e31" />

#### You can now use the new user in a new window
* Note that you will need to change the port and host according to your own interface.
<img width="1094" height="608" alt="image" src="https://github.com/user-attachments/assets/acba5aa2-4d41-41e1-a161-b73b402c62f2" />


#### When running the test script, you should be able to add a new entry and receive this output
<img width="1086" height="176" alt="image" src="https://github.com/user-attachments/assets/0a8d01ea-9778-430c-826f-9ebe537b19f5" />

### Tests
#### Check to ensure you can read all documents
<img width="895" height="223" alt="image" src="https://github.com/user-attachments/assets/84f60bcc-c027-4fc3-ab6a-c4615cfbc243" />

#### CRUD Functionality Test Execution
Below shows the test for creation, reading, updating and deletion. If this does not complete, you will receive an Exception flag.
<img width="1729" height="1082" alt="image" src="https://github.com/user-attachments/assets/7d055ebf-a61b-43c6-801a-3912d745fcfb" />

#### Check that you can access MongoDB and list the database using both the admin and self-created user
<img width="831" height="440" alt="image" src="https://github.com/user-attachments/assets/8d7a249e-2e6a-4dc8-8dd8-def2f01887f4" />

<img width="828" height="521" alt="image" src="https://github.com/user-attachments/assets/8043404a-6e7a-45a1-aa0f-de9b34a4bc14" />


### Roadmap / Features
Feature releases of this project will have:
* Ability to Update an entry.
   + Committed on 07/28/2025

### Contact
Ronny Z. Valtonen






