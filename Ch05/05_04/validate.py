class Error(ValueError):
    def __init__(self, field, reason):
        super().__init__(f'{field}: {reason}')
        self.field = field
        self.reason = reason


def start_request(request):
    if not request.driver_id:
        raise Error('driver_id', 'empty')
    # TODO: Validate more fields
