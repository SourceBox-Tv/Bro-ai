def mailer(): 
            try: 
                import smtplib
                print("We dont take your any email or its passwords u can check on github our code to even verify")
                print("if u have 2 factor authienticaion use app password https://myaccount.google.com/apppasswords")
                print("otherwise if not then pls enable allow from less apps here at your https://myaccount.google.com/lesssecureapps")
                print("if u dont do this u wont be able to send mails")
                server = smtplib.SMTP("smtp.gmail.com",587)
                email = input("Enter email id of yours: \n")
                passd = input("Enter password: \n")
                print("What should I say?")
                print("pls type")
                content = input()
                print("whoome should i send")
                print("pls type")
                to = input()
                server.starttls()
                server.login(email,passd)
                server.sendmail(email,to,content)
                server.quit()  
                print("Email has been sent !")
            except Exception as e:
                print(e)
                print("I am not able to send this email")