from os import getlogin
import sys
import datetime

def main():
    print(sys.argv[1])
    print(sys.argv[2])

def help():
    op='''Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'''
    sys.stdout.buffer.write(op.encode('utf8'))

def report():
    now=datetime.datetime.now().date()
    todos=getLines('todo.txt')
    dones=getLines('done.txt')
    print("{} Pending : {} Completed : {}".format(str(now),len(todos),len(dones)))


def ls():
    todos=getLines('todo.txt')
    if len(todos)==0:
        print("There are no pending todos!")
        return
    temp=''
    for i in reversed(range(len(todos))):
        temp+='[{}] {}\n'.format(i+1,todos[i])
    sys.stdout.buffer.write(temp.encode('utf8'))

def getLines(file):
    try:
        f=open(file,'r')
    except:
        f=open(file,'x')
        f.close()
        f=open(file,'r')
    todos=[line.strip() for line in f]
    f.close()
    return todos

def putLines(file,lines):
    w=open(file,'w')
    w.write('\n'.join(lines))
    w.close()

def add(text):
    todos=getLines('todo.txt')
    todos.append(text)
    putLines('todo.txt',todos)
    print("Added todo: \"{}\"".format(text))

def delete(number):
    number=int(number)
    todos=getLines('todo.txt')
    if(number>len(todos) or number<1):
        print("Error: todo #{} does not exist. Nothing deleted.".format(number))
        return
    else:
        del todos[number-1]
        putLines('todo.txt',todos)
        print("Deleted todo #{}".format(number))
        
def done(number):
    now=datetime.datetime.now().date()
    number=int(number)
    todos=getLines('todo.txt')
    if(number>len(todos) or number<1):
        print("Error: todo #{} does not exist.".format(number))
        return
    else:
        done=todos[number-1]
        del todos[number-1]
        putLines('todo.txt',todos)
        dones=getLines('done.txt')
        done='x '+str(now)+' '+done
        dones.append(done)
        putLines('done.txt',dones)
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
        elif sys.argv[1].lower()=='done':
            print("Error: Missing NUMBER for marking todo as done.")
        elif sys.argv[1].lower()=='del':
            print("Error: Missing NUMBER for deleting todo.")
        elif sys.argv[1].lower()=='add':
            print("Error: Missing todo string. Nothing added!")

    elif (len(sys.argv)==3):
        if sys.argv[1].lower()=='add':
            add(sys.argv[2])
        elif sys.argv[1].lower()=='del':
            delete(sys.argv[2])
        elif sys.argv[1].lower()=='done':
            done(sys.argv[2])

    
    # main()