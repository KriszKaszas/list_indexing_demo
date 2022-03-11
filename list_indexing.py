import os
import time



def print_list(current_index, demo_list):
    print("\033[33mdemo_list\033[0m = [", end="")
    for i in range(len(demo_list)):
        if i == current_index:
            print("\033[34m", end="")
        print(demo_list[i], "\033[0m",  end="")
        if i != len(demo_list)-1:
            print(", ", end="")
    print("]")



def print_list_attributes(index, demo_list):
    print("    \033[33mdemo_list\033[0m["+ "\033[1;32m" + str(index) + "\033[0m" + "]")
    print_list(index, demo_list)
    print("\n\033[0m         list \033[1;32mindex\033[0m:", "\033[1;32m", index)
    print("\033[0mlist \033[34mvalue\033[0m at \033[1;32mindex\033[0m:", "\033[34m", demo_list[index], "\033[0m")



def print_for_loop_demo(index):
    print("\nFor loop starts from 0")
    print("\033[1;32mi\033[0m = \033[1;32m" + str(index) + "\033[0m")
    print("for \033[1;32mi\033[0m in range(len(\033[33mdemo_list\033[0m):   \n    \033[33mdemo_list\033[0m[\033[1;32mi\033[0m]" )
    print("             ||")
    print("             ||")
    print("            \\  /")
    print("             \\/")
    print("\033[1;32mi\033[0m = \033[1;32m" + str(index) + "\033[0m")
    print("for \033[1;32m" + str(index) + "\033[0m in range(len(\033[33mdemo_list\033[0m):   \n    \033[33mdemo_list\033[0m[\033[1;32m" + str(index) + "\033[0m]" )
    print("             ||")
    print("             ||")
    print("            \\  /")
    print("             \\/")


def print_demo(demo_list):
    for i in range(len(demo_list)):
        os.system("cls")
        print_list(i, demo_list)
        print_for_loop_demo(i)
        print_list_attributes(i, demo_list)
        time.sleep(2)



def main():
    demo_list = [1, 2, 3, 4, 5]
    print_demo(demo_list)



if __name__ == "__main__":
    main()
