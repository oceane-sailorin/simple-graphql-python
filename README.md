# simple-graphql-python

### installation

- python -m venv simple-graphql-python-env

- pip install flask ariadne flask-sqlalchemy

- export FLASK_APP=main.py

- flask run

check http://127.0.0.1:5000

### playground

url : 127.0.0.1:5000/graphql

![app screenshot](api/img/playground.png "Playground")


### queries

- Get all residents: 

query fetchAllResidents {
  residents {
    success
    errors
    residents {
      name
      age
      id
    }
  }
}

- Get one resident: 

query fetchResident {
  resident(residentId: "1") {
    success
    errors
    resident { id name age installed installationDate }
  }
}

- Create a resident: 

mutation newResident {
  createResident(name:"LiveHere", age:28, installed: false, installationDate:"16-12-2021") {
    success
    errors
    resident {
      id
      name
      age
      installationDate
      installed
    }
  }
}


mutation newResident {
  createResident(name:"LiveAlsoHere", age:29, installed: false, installationDate:"16-12-2021") {
    success
    errors
    resident {
      id 
      name 
      age 
      installed 
      installationDate
    }
  }
}

mutation newResident {
  createResident(name:"Another Resident", age:30, installed: true, installationDate:"15-12-2021") {
    success
    errors
    resident {
      id 
      name 
      age 
      installed 
      installationDate
    }
  }
}

- Update status installed:

mutation installedResident {
  installedResident(residentId: "1") {
    success
    errors
    resident { id name age installed installationDate}
  }
}

- Delete a resident:

mutation deleteResident{
  deleteResident(residentId: "2") {
    success
    errors
  }
}

- Update age of a resident:

mutation updateAgeResident {
  updateAgeResident(residentId: "1", newAge: 78) {
    success
    errors
  }
}

