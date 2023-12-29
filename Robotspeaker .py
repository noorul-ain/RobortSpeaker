import os 
if __name__=='__main__':
    print("Wellcome to RoboSpeaker 1.1 Created by Noor")
    while True:
        x  = input("Enter what you want to speak: ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)
