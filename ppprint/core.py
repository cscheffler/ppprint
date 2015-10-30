import sys


def _is_simple_list(l):
    return not any([isinstance(x, (list, tuple, dict)) for x in l])


def _is_simple_dict(d):
    return (len(d) < 2) and _is_simple_list(d.itervalues())


def _pformat_recursive(obj, spaces, indent, roll_up_last_line, start_indent=True):
    spacer = ' ' * spaces
    left_margin = spacer * indent
    output = ''
    if start_indent:
        output += left_margin
    if isinstance(obj, dict):
        if _is_simple_dict(obj):
            output += repr(obj)
        else:
            output += '{\n'
            for index, (key, value) in enumerate(sorted(obj.iteritems())):
                output += left_margin + spacer + repr(key) + ': '
                output += _pformat_recursive(
                    value,
                    spaces,
                    indent + 1,
                    roll_up_last_line,
                    start_indent=False)
                if not roll_up_last_line or (index < len(obj) - 1):
                    output += ',\n'
            if not roll_up_last_line:
                output += left_margin
            output += '}'
    elif isinstance(obj, (list, tuple)):
        if _is_simple_list(obj):
            output += repr(obj)
        else:
            if isinstance(obj, list):
                output += '['
            else:
                output += '('
            output += '\n'
            for index, value in enumerate(obj):
                output += left_margin + spacer
                output += _pformat_recursive(
                    value,
                    spaces,
                    indent + 1,
                    roll_up_last_line,
                    start_indent=False)
                if not roll_up_last_line or (index < len(obj) - 1):
                    output += ',\n'
            if not roll_up_last_line:
                output += left_margin
            output += ']'
    else:
        output += repr(obj)
    return output


def pformat(object, spaces=4, roll_up_last_line=True):
    '''
    Format a Python object into a pretty-printed representation.
    '''
    return _pformat_recursive(object, indent=0, spaces=spaces, roll_up_last_line=roll_up_last_line)


def pprint(object, stream=None, spaces=4, roll_up_last_line=True):
    '''
    Pretty-print a Python object to a stream [default is sys.stdout].
    '''
    if stream is None:
        stream = sys.stdout
    stream.write(_pformat_recursive(object, indent=0, spaces=spaces, roll_up_last_line=roll_up_last_line))
    stream.write('\n')
