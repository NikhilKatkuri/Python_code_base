# my first project in python - quiz app 
import json
from pathlib import Path
from question import mcqs 

title ='welcome to quiz app \n'
option_flag =['a','b','c','d']
modes = ['1. score board','2. Attempt Quiz']
points=0
name =''

def scoreBoard():
    print('\n--- SCOREBOARD ---\n')
    try:
        with open('scoreboard.json', 'r') as f:
            data = json.load(f)
            sorted_data = sorted(data,key=lambda x:x['score'],reverse=True) 
            for i,record in enumerate(sorted_data):
                print(f"Rank-{i+1} {record['name']} - {record['score']}")

    except FileNotFoundError:
        print('[file not found]')
        exit()

    except Exception as e:
        print('An error occurred:', e)
        exit()

def modeSelector():
    global modes
    for mode in modes:
        print(mode)
    try:
        option = input('choose an option(1 or 2) :').lower()
    except KeyboardInterrupt:
           print('KeyboardInterrupt')
           exit()
    except EOFError:
           print('error')
           exit()
    return option

def userName():
    global name
    try:
       name = input('enter your name please : ') 
    except KeyboardInterrupt:
           print('KeyboardInterrupt')
           exit()
    except EOFError:
           print('error')
           exit()

def questions():
    global points
    global option_flag 
    for key, value in mcqs.items(): 
        print(key.replace('_', ' '),'\n')
        print(value['question'])
        options = value['options']
        for i,option in enumerate(options): 
            print(option_flag[i]+') '+option)
        try: 
            chosedOption = input('choose an option(a/b/c/d) : ').lower()
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            exit()
        except EOFError:
            print('error')
            exit()
        index = option_flag.index(chosedOption)
        if(options[index]==value['correct']):
            points+=1
        print('\n')
        if(key =='question_20'):
          return str(points)
        
def main():
    print(title)
    mode = modeSelector()
    if mode == '1':
        scoreBoard()
    elif mode == '2':
        userName()
        points = questions()
        if points:
            file = Path('scoreboard.json')
            if file.exists():
                try:
                    with open(file, 'r+') as f:
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError:
                            data = [] 
                        data.append({
                            'name': f"{name}",
                            'score': f"{points}"
                        }) 
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
                        exit()
                except Exception as e:
                    print('An exception occurred:', e)
            else:
                try:
                    with open(file, 'w') as f:
                        data = [{
                            'name': f"{name}",
                            'score': f"{points}"
                        }]
                        json.dump(data, f, indent=4)
                except Exception as e:
                    print('An exception occurred:', e)
        else:
            print('** please enter options from above range only **')

    else:
        print('** Invalid mode selected! **')

main()