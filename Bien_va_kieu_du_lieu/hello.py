def processEmail(email):
    try:
        email_username = email[0:email.index("@")]
        email_domain = email[email.index("@") + 1:]
        return [email_username, email_domain]
    except:
        print("Email ko dung dinh dang")
        return [None, None]
    
def cToFConverter():
    cTemp = float(input("Nhap nhiet do:"))
    while not cTemp:
        cTemp = float(input("Vui long nhap nhiet do:"))
    fTemp = 9 * cTemp / 5 + 32
    print(f"{cTemp}C is converted to {fTemp}F")
    


def main():
    email = input("Vui long nhap email:")
    email_username, email_domain = processEmail(email)
    if email_domain and email_username:
        print(f"Username is {email_username}\nEmail Domain is {email_domain}")


if __name__ == "__main__":
    main()
    # cToFConverter()

    # cach truy cap chuoi con
    my_string = "Hello world"
    sub_string = my_string[1:5] # ello
    sub_string = my_string[:5] # Hello
    sub_string = my_string[6:] # world
    sub_string = my_string[-5:] #world
    sub_string = my_string[::-1] # reverse the string
    sub_string = my_string[::2] # Take every second character (Hlowrd) 
    
    # cach noi trong chuoi
    name = "nam"
    greeting = "Hello"
    sectence = greeting + " " + name

      