


class my_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Hello, world!'
        print("\n\n",response,"\n\n")
        return response

