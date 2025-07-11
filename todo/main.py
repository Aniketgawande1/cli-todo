from todo.parser import parse_args
from todo.dispatcher import dispatch

def main():
    command, args = parse_args()  # kya command aaya aur kya argument
    if command:
        dispatch(command, args)  # usko dispatch karo
    else:
        print("⚠️ Bhai command nahi diya. Try: add, list")

if __name__ == "__main__":
    main()
