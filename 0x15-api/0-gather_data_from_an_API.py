#!/usr/bin/python3
""" Gets data from users todo from REST API """

if __name__ == "__main__":
    import requests
    import sys

    arguments = sys.argv
    if (len(arguments) < 2):
        exit(-1)

    empId = arguments[1]
    if (not empId.isdigit()):
        exit(-1)
    try:
        empUrl = 'https://jsonplaceholder.typicode.com/users/' + empId
        todoUrl = 'https://jsonplaceholder.typicode.com/users/'+empId+'/todos'
        employee = requests.get(empUrl)
        if (employee.status_code == 200):
            employeeJson = employee.json()
            name = employeeJson['name']
            employeeTodo = requests.get(todoUrl)
            if (employeeTodo.status_code == 200):
                todos = employeeTodo.json()
                cmpt = sum(item['completed'] for item in todos)
                numb = len(todos)
                txt = "Employee {name} is done with tasks({cmpt}/{numb}):"
                print(txt.format(name=name, cmpt=cmpt, numb=numb))
                for item in todos:
                    if (item['completed']):
                        print("\t {title}".format(title=item['title']))
        else:
            print("Employee Not exist")
    except Exception as e:
        print(e)
