from interpreters.arithmetic import Interpreter, Lexer


if __name__ == '__main__':
    import traceback

    index = 1

    while True:
        try:
            expression = raw_input('[{}]> '.format(index))
        except EOFError:
            break

        if not expression:
            continue

        try:
            lexer = Lexer(expression)
            result = Interpreter(lexer).parse()
            print result
        except Exception as exc:
            print 'Error! Line {}'.format(index)
            if hasattr(exc, 'text'):
                print exc.text
            print traceback.format_exc().splitlines()[-1]

        index += 1
