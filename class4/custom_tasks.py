from nornir import InitNornir
from nornir.core.task import Result
#from nornir.plugins.functions.text import print_result
#from nornir.plugins.tasks import networking

#listet auf, in welcher group dies hosts sind
def my_task(task):
    print(task.host.groups[0])

def main():
    nr = InitNornir(config_file="config.yaml", logging={"enabled": True})
    nr.run(task=my_task)

if __name__ == "__main__":
    main()
