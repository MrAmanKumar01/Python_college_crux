print("This always executes, whether run as an idependent script or when imported.")

def main():
    print("FirstModules Main method")
    print(f"Name: {__name__}")
    

if __name__ == "__main__": 
    main()                  # executes only directly as a script, not when imported


