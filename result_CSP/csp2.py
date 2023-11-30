def main_csp(input_row: int) :
    try :
        curr = 1
        for col in range(input_row):
            urgent = 0
            curr_value = 1
            for row in range(input_row):
                current_value = row + curr
                if current_value > input_row :
                    print(curr_value+urgent, end="   ")
                    urgent += 1
                else :
                    print(current_value, end="   ")
            curr += 1
            print()
    except:
        print("Please Input Number Only !")
        
def main():
    result_value = int(input("Please Input ur Number Cols & Rows : "))
    print("\n")
    print("="*11, "result", "="*10)
    main_csp(result_value)
    print("="*11, "result", "="*10)