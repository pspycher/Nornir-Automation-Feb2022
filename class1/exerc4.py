from nornir import InitNornir
#nr = InitNornir(config_file="/home/pspycher/config.yaml")

def my_task(task):
    print()
    print(task.host.hostname) 
    print("-" * 24)
    print("This is the Hostname of our Host.")
    print()




if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr.run(task=my_task)

