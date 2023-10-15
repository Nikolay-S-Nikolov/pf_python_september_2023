def electron_distribution(available_electrons: int) -> list:
    shell_list = []
    shell_number = 0
    while available_electrons:
        shell_number += 1
        max_electrons_in_shell = 2 * (shell_number ** 2)
        if max_electrons_in_shell < available_electrons:
            shell_list.append(max_electrons_in_shell)
            available_electrons -= max_electrons_in_shell
        else:
            shell_list.append(available_electrons)
            available_electrons = 0
    return shell_list


number_of_electrons = int(input())
result = electron_distribution(number_of_electrons)
print(result)
