# coding: utf-8

def Step1():
    peoples = {
        "1" : "Timothée",
        "2" : "Cécilia",
        "3" : "Théo",
        "4" : "Nicolas",
        "5" : "Gaël"
    }

    for Element in peoples.items():
        print(f"{Element[0]} -> {Element[1]}")

    print()

    for Key, Value in peoples.items():
        print(f"{Key} -> {Value}")


def Step2():
    peoples = {
        "1" : ("Timothée", "Vannier", 2003),
        "2" : ("Cécilia", "Conquet", 1997),
        "3" : ("Théo", "Fassi", 2005),
        "4" : ("Nicolas", "Libert", 1980),
        "5" : ("Gaël", "Monlouis", 1997)
    }

    for Key, Value in peoples.items():
        print(f"{Key} -> {Value}")
        FirstName, LastName, BirthYear = Value
        print(f"{FirstName} {LastName} est né(e) en {BirthYear}, il a donc {2021-BirthYear} ans")


def Step3():
    peoples = [
        {
            "FirstName" : "Timothée", 
            "LastName" : "Vannier",
            "BirthYear" : 2003
        },
        {
            "FirstName" : "Cécilia", 
            "LastName" : "Conquet",
            "BirthYear" : 1997
        },
        {
            "FirstName" : "Théo", 
            "LastName" : "Fassi",
            "BirthYear" : 2005
        },
        {
            "FirstName" : "Nicolas", 
            "LastName" : "Libert",
            "BirthYear" : 1980
        },
        {
            "FirstName" : "Gaël", 
            "LastName" : "Monlouis",
            "BirthYear" : 1997
        }
    ]

    for Person in peoples:
        print(f"{Person['FirstName']} {Person['LastName']} est né(e) en {Person['BirthYear']}, il a donc {2021-Person['BirthYear']} ans")


def Step4():
    peoples = [
        {
            "FirstName" : "Timothée", 
            "LastName" : "Vannier",
            "BirthYear" : 2003,
            "Sex" : "Masculin"
        },
        {
            "FirstName" : "Cécilia", 
            "LastName" : "Conquet",
            "BirthYear" : 1997,
            "Sex" : "Féminin"
        },
        {
            "FirstName" : "Théo", 
            "LastName" : "Fassi",
            "BirthYear" : 2005,
            "Sex" : "Masculin"
        },
        {
            "FirstName" : "Nicolas", 
            "LastName" : "Libert",
            "BirthYear" : 1980,
            "Sex" : "Masculin"
        },
        {
            "FirstName" : "Gaël", 
            "LastName" : "Monlouis",
            "BirthYear" : 1997,
            "Sex" : "Masculin"
        }
    ]

    for Person in peoples:
        # Person["Sex"] = "Masculin"
        SexString = ""
        if Person["Sex"] == "Féminin":
            SexString = "e"
        print(f"{Person['FirstName']} {Person['LastName']} est né{SexString} en {Person['BirthYear']}, il a donc {2021-Person['BirthYear']} ans")
        print(Person)
        print(Person.pop("Sex"))
        print(Person)
        print()


# Code starts here
if __name__ == "__main__":
    Step4()
