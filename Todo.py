class Todo:
    def __init__(self,task=""):
        self.Taskinput=task
    def create(self):
        
        
        with open("data.txt","a") as self.file1:
                self.file1.write(f"{self.Taskinput} ,")
    def update(self,index):
        
        with open("data.txt","r") as file1:
                data=file1.read()
        Todotask=data.split(" ,")
        Todotask[index]=self.Taskinput
        
        with open("data.txt","w+") as file1:
               
               file1.write(" ,".join(Todotask))
               file1.seek(0,2)
    def view(self):
        with open("data.txt","r") as file1:
                data=file1.read()
        Todotask=data.split(" ,")
        a=(len(Todotask))-1
        
        for i in range(a):
            print(f"Task{i}: {Todotask[i]}")
while True:
        print('''
TODO LIST
1.Write TASKS    
2.Update TASKS 
3.View TASKS
4.Exit Todo List ''')
        option=int(input("CHOOSE AN OPTION:"))
        if option==1:
            Taskinput=input("Enter Task:")
            todo=Todo(Taskinput)
            todo.create()

        elif option==2:
           
           index=int(input("Enter the number of task you want to  update:"))
           
           Taskinput=Taskinput=input("Enter updated Task:")
           todo=Todo(Taskinput)
           todo.update(index)
           
               
           
        elif option==3:
            todo=Todo()
            todo.view()
        else:
           break;
      
        
          
    


   
s
