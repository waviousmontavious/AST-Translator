def send_command(cmd, params):
    return f'SEND {cmd} {", ".join(params)}'