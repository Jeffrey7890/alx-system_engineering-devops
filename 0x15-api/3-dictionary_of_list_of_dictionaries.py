#!/usr/bin/python3
""" Gets data from users todo from REST API and exports as json file """

if __name__ == "__main__":
    import json
    import requests
    import sys

    try:
        dictData = {}
        empUrl = 'https://jsonplaceholder.typicode.com/users/'
        employees = requests.get(empUrl)
        if (employees.status_code == 200):
            employeesJson = employees.json()
            for employee in employeesJson:
                empId = str(employee['id'])
                name = employee['username']
                todoUrl = empUrl+empId+'/todos'
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
            with open('todo_all_employees.json', 'w') as file:
                json.dump(dictData, file)
    except Exception as e:
        print(e)
