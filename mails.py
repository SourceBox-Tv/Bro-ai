def mailer():
            try:
                import ai
                import smtplib
                print("We dont take your any email or its passwords u can check on github our code to even verify")
                print("if u have 2 factor authienticaion use app password https://myaccount.google.com/apppasswords")
                print("otherwise if not then pls enable allow from less apps here at your https://myaccount.google.com/lesssecureapps")
                print("if u dont do this u wont be able to send mails")
                server = smtplib.SMTP("smtp.gmail.com",587)
                email = input("Enter email id of yours:")
                passd = input("Enter password:")
                ai.assistant_speaks("What should I say?")
                ai.assistant_speaks("Should I type for you ; Say yes for typing from speech to text or otherwise you can type yourself")
                rams = input("Yes or no : ")
                raj = ai.ai_mic()
                if rams == "Yes" or "y" or "yes":
                    content = raj
                else:
                    print("pls type what to be written")
                    content=input()
                ai.assistant_speaks("whoome should i send")
                print("pls type")
                to = input()
                server.starttls()
                server.login(email,passd)
                server.sendmail(email,to,content)
                server.quit()  
                ai.assistant_speaks("Email has been sent !")
            except Exception as e:
                print(e)
                ai.assistant_speaks("I am not able to send this email")