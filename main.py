def main():
    part_nr = input("Enter number on part: ")
    part_name = input("Name of part: ")
    add_part(part_nr, part_name)
    

def add_part(part_nr, part_name):
    """this function will be responseble for adding parts to the db"""
    print(part_name, part_nr)




if __name__ == "__main__":
    main()