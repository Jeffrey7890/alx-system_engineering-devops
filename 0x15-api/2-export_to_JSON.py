#!/usr/bin/python3
""" Gets data from users todo from REST API and exports as json file """

if __name__ == "__main__":
    import json
    import requests
    import sys

    arguments = sys.argv
    if (len(arguments) < 2):
        exit(-1)

    empId = arguments[1]
    if (not empId.isdigit()):
        exit(-1)
    try:
        dictData = {}
        empUrl = 'https://jsonplaceholder.typicode.com/users/' + empId
        todoUrl = 'https://jsonplaceholder.typicode.com/users/'+empId+'/todos'
        employee = requests.get(empUrl)
        if (employee.status_code == 200):
            employeeJson = employee.json()
            name = employeeJson['username']
            employeeTodo = requests.get(todoUrl)
            if (employeeTodo.status_code == 200):
                todos = employeeTodo.json()
                listData = []
                for item in todos:
                    nestDict = {}
                    nestDict["task"] = item['title']
                    nestDict["completed"] = item['completed']
                    nestDict["username"] = name
                    listData.append(nestDict)
                dictData[empId] = listData
                with open(empId + '.json', 'w') as file:
                    json.dump(dictData, file)
        else:
            print("Employee Not exist")
    except Exception as e:
        print(e)
