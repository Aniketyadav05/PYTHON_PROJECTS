def main():
    print("WELCOME TO OUR EMAIL SLICER APP")
    print("")


    email_input = input("ENTER YOUR EMAIL ADDRESS:")


    (username , domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"USERNAME IS: {username}")
    print(f"DOMAIN IS: {domain}")
    print(f"EXTENSION IS: {extension}")


while True:

    main()