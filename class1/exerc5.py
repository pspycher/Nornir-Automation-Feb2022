from nornir import InitNornir
#nr = InitNornir(config_file="/home/pspycher/config.yaml")

def my_task(task):
    #host = task.host
    print()
    print("-" * 24)
    print(task.host.hostname) 
    print("-" * 24)
    #print("This is the Hostname + DNS of our Host.")
    print(f"This is the Hostname + DNS of our Host: {task.host.hostname}")
    print(f"DNS1: {task.host['dns1']}")
    print(f"DNS2: {task.host['dns2']}")
    print()




if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr.run(task=my_task)

