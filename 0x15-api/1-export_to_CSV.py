#!/usr/bin/python3
""" Gets data from users todo from REST API """

if __name__ == "__main__":
    import csv
    import requests
    import sys

    arguments = sys.argv
    if (len(arguments) < 2):
        exit(-1)

    empId = arguments[1]
    if (not empId.isdigit()):
        exit(-1)
    try:
        csv_data = []
        empUrl = 'https://jsonplaceholder.typicode.com/users/' + empId
        todoUrl = 'https://jsonplaceholder.typicode.com/users/'+empId+'/todos'
        employee = requests.get(empUrl)
        if (employee.status_code == 200):
            employeeJson = employee.json()
            name = employeeJson['username']
            employeeTodo = requests.get(todoUrl)
            if (employeeTodo.status_code == 200):
                todos = employeeTodo.json()
                for item in todos:
                    row = [empId, name, item['completed'], item['title']]
                    csv_data.append(row)
            with open(empId + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                writer.writerows(csv_data)
        else:
            print("Employee Not exist")
    except Exception as e:
        print(e)
