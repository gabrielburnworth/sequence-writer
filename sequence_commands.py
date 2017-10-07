#!/usr/bin/env python
"""Sequence commands."""


# JSON building blocks

def _encode_coordinates(x_coord, y_coord, z_coord):
    coords = {}
    coords['x'] = x_coord
    coords['y'] = y_coord
    coords['z'] = z_coord
    return coords


def create_node(kind=None, args=None):
    """Create a kind, args node."""
    node = {}
    node['kind'] = kind
    node['args'] = args
    return node


def create_pair(label=None, value=None):
    """Create a label, value node."""
    pair = {}
    pair['label'] = label
    pair['value'] = value
    return pair


def _saved_location_node(pointer_type, pointer_id):
    args = {}
    if 'tool' in pointer_type.lower():
        location_type = 'tool'
        args['tool_id'] = pointer_id
    else:
        location_type = 'point'
        args['pointer_type'] = pointer_type
        args['pointer_id'] = pointer_id
    saved_location = create_node(kind=location_type, args=args)
    return saved_location


def _coordinate_node(x_coord, y_coord, z_coord):
    coordinates = _encode_coordinates(x_coord, y_coord, z_coord)
    coordinate = create_node(kind='coordinate', args=coordinates)
    return coordinate


# Commands

def move_absolute(location=(0, 0, 0), offset=(0, 0, 0), speed=100):
    """Move Absolute.

    Kind:
        move_absolute
    Arguments:
        Location:
            Coordinate (x, y, z)
            Saved Location
                ['tool', tool_id]
                ['Plant', pointer_id]
                ['GenericPointer', pointer_id]
        Offset:
            Distance (x, y, z)
        Speed:
            Speed (mm/s)
    """
    args = {}
    if len(location) == 2:
        args['location'] = _saved_location_node(
            location[0], location[1])
    if len(location) == 3:
        args['location'] = _coordinate_node(*location)
    args['offset'] = _coordinate_node(*offset)
    args['speed'] = speed
    _move_absolute = create_node(kind='move_absolute', args=args)
    return _move_absolute

def move_relative(distance=(0, 0, 0), speed=100):
    """Move Relative.

    Kind:
        move_relative
    Arguments:
        x distance (mm)
        y distance (mm)
        z distance (mm)
        Speed (mm/s)
    """
    args = _encode_coordinates(*distance)
    args['speed'] = speed
    _move_relative = create_node(kind='move_relative', args=args)
    return _move_relative

def send_message(message='Hello World!', message_type='success', channel=None):
    """Send a message.

    Kind:
        send_message
    Arguments:
        message
        message_type: success, busy, warn, error, info, fun
        channel: toast, email
    """
    args = {}
    args['message'] = message
    args['message_type'] = message_type
    _send_message = create_node(kind='send_message', args=args)
    if channel is not None:
        channels = []
        if isinstance(channel, list):
            for channel_ in channel:
                channels.append(channel_)
        else:
            channels.append(channel)
        body = []
        for channel_ in channels:
            body.append(create_node(kind='channel',
                                    args={"channel_name": channel_}))
        _send_message['body'] = body
    return _send_message

def find_home(axis='all', speed=100):
    """Find home.

    Kind:
        find_home
    Arguments:
        axis: x, y, z, or all
        speed
    """
    args = {}
    args['axis'] = axis
    args['speed'] = speed
    _find_home = create_node(kind='find_home', args=args)
    return _find_home

def if_statement(lhs='x', op='is', rhs=0, _then=None, _else=None):
    """If statement.

    Kind:
        _if
    Arguments:
        lhs
        op
        rhs
        _then
        _else
    """
    args = {}
    args['lhs'] = lhs
    args['op'] = op
    args['rhs'] = rhs
    if _then is None:
        _then_kind = 'nothing'
        _then_args = {}
    else:
        _then_kind = 'execute'
        _then_args = {"sequence_id": _then}
    if _else is None:
        _else_kind = 'nothing'
        _else_args = {}
    else:
        _else_kind = 'execute'
        _else_args = {"sequence_id": _else}
    args['_then'] = create_node(kind=_then_kind, args=_then_args)
    args['_else'] = create_node(kind=_else_kind, args=_else_args)
    _if_statement = create_node(kind='_if', args=args)
    return _if_statement

def write_pin(number=0, value=0, mode=0):
    """Write pin.

    Kind:
        write_pin
    Arguments:
        pin_number: 0
        pin_value: 0
        pin_mode: 0
    """
    args = {}
    args['pin_number'] = number
    args['pin_value'] = value
    args['pin_mode'] = mode
    _write_pin = create_node(kind='write_pin', args=args)
    return _write_pin

def read_pin(number=0, mode=0, label='---'):
    """Read pin.

    Kind:
        read_pin
    Arguments:
        pin_number: 0
        pin_mode: 0
        label: '---'
    """
    args = {}
    args['pin_number'] = number
    args['pin_mode'] = mode
    args['label'] = label
    _read_pin = create_node(kind='read_pin', args=args)
    return _read_pin

def execute_sequence(sequence_id=0):
    """Execute sequence.

    Kind:
        execute
    Arguments:
        sequence_id: 0
    """
    args = {}
    args['sequence_id'] = sequence_id
    _execute_sequence = create_node(kind='execute', args=args)
    return _execute_sequence

def execute_script(label='plant_detection'):
    """Execute script.

    Kind:
        execute_script
    Arguments:
        label: 'plant_detection'
    """
    args = {}
    args['label'] = label
    _execute_script = create_node(kind='execute_script', args=args)
    return _execute_script

def wait(milliseconds=300):
    """Wait.

    Kind:
        wait
    Arguments:
        milliseconds: 0
    """
    args = {}
    args['milliseconds'] = milliseconds
    _wait = create_node(kind='wait', args=args)
    return _wait

def take_photo():
    """Take photo.

    Kind:
        take_photo
    Arguments:
        {}
    """
    args = {}
    _take_photo = create_node(kind='take_photo', args=args)
    return _take_photo
