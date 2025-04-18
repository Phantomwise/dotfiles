#!/usr/bin/env python3

# AI Disclaimer:
# This code was generated by a LLM.

def print_truecolor_gradient():
    for b in range(0, 256, 4):
        print(f"\033[48;2;0;0;{b}m \033[0m", end="")
    print(f"\033[38;2;0;0;0m #\033[38;2;0;0;0m000000\033[0m-\033[38;2;0;0;255m0000FF\033[0m")
    
    for b in range(0, 256, 4):
        print(f"\033[48;2;255;0;{b}m \033[0m", end="")
    print(f"\033[38;2;255;0;0m #\033[38;2;255;0;0mFF0000\033[0m-\033[38;2;255;0;255mFF00FF\033[0m")
    
    for g in range(0, 256, 4):
        print(f"\033[48;2;0;{g};0m \033[0m", end="")
    print(f"\033[38;2;0;0;0m #\033[38;2;0;0;0m000000\033[0m-\033[38;2;0;255;0m00FF00\033[0m")
    
    for g in range(0, 256, 4):
        print(f"\033[48;2;255;{g};0m \033[0m", end="")
    print(f"\033[38;2;255;0;0m #\033[38;2;255;0;0mFF0000\033[0m-\033[38;2;255;255;0mFFFF00\033[0m")
    
    for r in range(0, 256, 4):
        print(f"\033[48;2;{r};0;0m \033[0m", end="")
    print(f"\033[38;2;0;0;0m #\033[38;2;0;0;0m000000\033[0m-\033[38;2;255;0;0mFF0000\033[0m")
    
    for r in range(0, 256, 4):
        print(f"\033[48;2;{r};255;0m \033[0m", end="")
    print(f"\033[38;2;0;255;0m #\033[38;2;0;255;0m00FF00\033[0m-\033[38;2;255;255;0mFFFF00\033[0m")
    
    # Gradients with fixed green component
    for b in range(0, 256, 4):
        print(f"\033[48;2;0;255;{b}m \033[0m", end="")
    print(f"\033[38;2;0;255;0m #\033[38;2;0;255;0m00FF00\033[0m-\033[38;2;0;255;255m00FFFF\033[0m")
    
    for b in range(0, 256, 4):
        print(f"\033[48;2;255;255;{b}m \033[0m", end="")
    print(f"\033[38;2;255;255;0m #\033[38;2;255;255;0mFFFF00\033[0m-\033[38;2;255;255;255mFFFFFF\033[0m")
    
    for r in range(0, 256, 4):
        print(f"\033[48;2;{r};0;255m \033[0m", end="")
    print(f"\033[38;2;0;0;255m #\033[38;2;0;0;255m0000FF\033[0m-\033[38;2;255;0;255mFF00FF\033[0m")
    
    for r in range(0, 256, 4):
        print(f"\033[48;2;{r};255;255m \033[0m", end="")
    print(f"\033[38;2;0;255;255m #\033[38;2;0;255;255m00FFFF\033[0m-\033[38;2;255;255;255mFFFFFF\033[0m")
    
    for g in range(0, 256, 4):
        print(f"\033[48;2;0;{g};255m \033[0m", end="")
    print(f"\033[38;2;0;0;255m #\033[38;2;0;0;255m0000FF\033[0m-\033[38;2;0;255;255m00FFFF\033[0m")
    
    for g in range(0, 256, 4):
        print(f"\033[48;2;255;{g};255m \033[0m", end="")
    print(f"\033[38;2;255;0;255m #\033[38;2;255;0;255mFF00FF\033[0m-\033[38;2;255;255;255mFFFFFF\033[0m")

if __name__ == "__main__":
    print_truecolor_gradient()