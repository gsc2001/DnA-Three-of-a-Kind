import subprocess as sp

cli_path = ["~"]


def createMenu(
        menuName: str,
        options: dict,
        connection,
        cursor,
        wait_at_last: bool = False,
        back_keyword: str = 'Back'):
    while True:
        _ = sp.call('clear', shell=True)

        keys = list(options.keys())
        print(f"============== {menuName} ==================")
        print(f'0. {back_keyword}\n' + '\n'.join([f'{i+1}. {key}' for (i, key) in enumerate(keys)]) + '\n')
        ch = input(f"{'/'.join(cli_path)}>")
        if ch == '0':
            return
        elif ch in map(str, range(1, len(keys) + 1)):
            cli_path.append(keys[int(ch) - 1])
            options[keys[int(ch) - 1]](connection, cursor)
        else:
            cli_path.append('Temp')
            print("Invalid option\n")

        connection.rollback()

        if len(cli_path) > 0:
            cli_path.pop()

        if wait_at_last:
            _ = input('Press any key to continue')
