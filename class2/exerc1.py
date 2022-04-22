from nornir import InitNornir

def main():
    nr = InitNornir(config_file ="config1a.yaml")
    #nr = InitNornir()
    workers = nr.config.runner.options
    print(workers)
    workers = 20 if workers == {} else workers["num_workers"]
    print(f"\nNumber of workers: {workers}\n")



if __name__ == "__main__":
    main()

