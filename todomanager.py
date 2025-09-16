tasks = {}
first = True
delne = True
markne = True
unmarkne = True

while True:
    if first:
        menu = int(input('Welcome to To-Do-manager\n1 - Add a task\n2 - Delete a task\n3 - To mark a task as done\n4 - Show all my tasks\n: '))
        first = False
    else:
        menu = int(input('Choose an option: '))
    
    if menu == 1:
        task = input('Enter your task: ')
        if task in tasks:
            print("Task already exists!")
        else:
            tasks[task] = 'Not Done'
    elif menu == 2:
        delne = True
        while delne:
            for i, key in enumerate(tasks.keys(), start = 1):
                print(f'{i}. {key}: {tasks[key]}')
            
            num = int(input('Enter the number of task you want to delete: '))
            keys = list(tasks.keys())
        
            if 1 <= num <= len(keys):
                del tasks[keys[num-1]]
                print('Task deleted!')
            else:
                print('Invalid number')
        
            for i, key in enumerate(tasks.keys(), start = 1):
                print(f'{i}. {key}: {tasks[key]}')
            z = int(input('Do you want to delete something else? (1-Yes, 0-No): '))
            if z == 1:
                continue
            elif z == 0:
                delne = False
                print('You exited to menu.')
            else:
                print('Invalid number')
    elif menu == 3:
        markne = True
        while markne:
            for i, key in enumerate(tasks.keys(), start = 1):
                print(f'{i}. {key}: {tasks[key]}')
            
            nume = int(input('Enter the number of task you want to mark as done: '))
            keys = list(tasks.keys())
        
            if 1 <= nume <= len(keys):
                tasks[keys[nume-1]] = 'Done'
                print('Marked succesfully')
            else:
                print('Invalid number')
        
            for i, key in enumerate(tasks.keys(), start = 1):
                print(f'{i}. {key}: {tasks[key]}')
            
            done_tasks = [k for k, v in tasks.items() if v == 'Done']
            if done_tasks:
                m = int(input('Do you want to mark as done something else or unmark something? (2-Unmark, 1-Mark smth else, 0-No): '))
            else:
                m = int(input('Do you want to mark as done something else? (1-Yes, 0-No): '))
            if m == 2:
                unmarkne = True
                while unmarkne:
                    done_tasks = [k for k, v in tasks.items() if v == 'Done']
                    
                    for i, key in enumerate(done_tasks, start = 1):
                        print(f'{i}. {key}: {tasks[key]}')
                    
                    numme = int(input('Enter the number of task you want to unmark: '))
                    if 1 <= numme <= len(done_tasks):
                        tasks[done_tasks[numme - 1]] = 'Not Done'
                        print('The task unmarked successfully')
                    else:
                        print('Invalid number')
                    
                    for i, key in enumerate(tasks.keys(), start = 1):
                        print(f'{i}. {key}: {tasks[key]}')
                    
                    z2 = int(input('Do you want to unmark something else? (1-Yes, 0-No): '))
                    if z2 == 1:
                        continue
                    elif z2 == 0:
                        unmarkne = False
                        markne = False 
                        print('You exited to menu.')
                    else:
                        print('Invalid number')
            elif m == 1:
                continue
            elif m == 0:
                markne = False
                print('You exited to menu.')
            else:
                print('Invalid number')
    elif menu == 4:
        if tasks:
            for key, value in tasks.items():
                print(f'{key}: {value}')
        else:
            print("You haven't got any task")
        
                
                
    