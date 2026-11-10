def check_status():

    status = "pending"

    def update_status():
        nonlocal status
        status = "completed"

    update_status()

    print("Final Status:", status)


check_status()