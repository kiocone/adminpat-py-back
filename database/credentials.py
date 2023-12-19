import os


def get_credentials():
    data = []
    work_dir = os.getcwd()
    try:
        with open(f"{work_dir}/credentials.ini", "r") as config_file:
            for line in config_file:
                if "=" in line:
                    line = line.strip()
                    data.append(line.split('=')[1])
            config_file.close()
    except FileNotFoundError:
        print("Config file dosn't exist! \rPlease define new credentials.")
        user = input("Database username: ").strip()
        password = input("Password: ").strip()
        host = input("Host[127.0.0.1]: ").strip()
        if host == "":
            host = "127.0.0.1"
        config_file = open("credentials.ini", "w")
        config_file.write(f"user={user}\n")
        data.append(user)
        config_file.write(f"password={password}\n")
        data.append(password)
        config_file.write(f"host={host}\n")
        data.append(host)
        config_file.close()
    return data
