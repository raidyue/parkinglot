def date_format(date_need_format):
    if date_need_format is None:
        return '0000-00-00 00:00:00'
    return date_need_format.strftime('%Y-%m-%d %H:%M:%S')