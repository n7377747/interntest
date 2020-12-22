import sys
import datetime

def main():
    print(sys.argv[1])
    print(sys.argv[2])

def help():
    print('''
$ ./todo help
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
        ''')

def report():
    print("report")

def ls():
    f=open('./todo.txt','r')
    todos=[line.strip() for line in f]
    for i in reversed(range(len(todos))):
        print('[{}] {}'.format(i+1,todos[i]))
    f.close()

def getLines(file):
    f=open(file,'r')
    todos=[line.strip() for line in f]
    f.close()
    return todos

def putLines(file,lines):
    w=open(file,'w')
    w.write('\n'.join(lines))
    w.close()

def add(text):
    todos=getLines('./todo.txt')
    todos.append(text)
    putLines('./todo.txt',todos)
    

def delete(number):
    number=int(number)
    todos=getLines('./todo.txt')
    if(number>len(todos) or number<1):
        print("Error: todo #{} does not exist. Nothing deleted.".format(number))
        return
    else:
        del todos[number-1]
        putLines('./todo.txt',todos)
        print("Deleted todo #{}".format(number))
        
def done(number):
    now=datetime.datetime.now().date()
    number=int(number)
    todos=getLines('./todo.txt')
    if(number>len(todos) or number<1):
        print("Error: todo #{} does not exist.".format(number))
        return
    else:
        done=todos[number-1]
        del todos[number-1]
        putLines('./todo.txt',todos)
        dones=getLines('./done.txt')
        done='x '+str(now)+' '+done
        dones.append(done)
        putLines('./done.txt',dones)
        print("Marked todo #{} as done.".format(number))

if __name__=="__main__":
    if len(sys.argv)==1:
        help()
    elif (len(sys.argv)==2):
        if sys.argv[1].lower()=='help':
            help()
        elif sys.argv[1].lower()=='report':
            report()
        elif sys.argv[1].lower()=='ls':
            ls()
    elif (len(sys.argv)==3):
        if sys.argv[1].lower()=='add':
            add(sys.argv[2])
        elif sys.argv[1].lower()=='del':
            delete(sys.argv[2])
        elif sys.argv[1].lower()=='done':
            done(sys.argv[2])

    
    # main()