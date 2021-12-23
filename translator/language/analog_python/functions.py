def send_command(cmd, params):
    return f'send_command("{cmd}", {", ".join(params)})'