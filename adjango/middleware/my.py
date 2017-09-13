try:
    from django.utils.deprecation import MiddlewareMixin  #django 1.10.x
except ImportError:
    MiddlewareMixin = object  #django 1.4.x-1.9.x
    
class WufangwutiMiddleware(MiddlewareMixin):
    def __init__(self, next_layer=None):
        print('init')
        self.get_response = next_layer
        
    def process_request(self,request):
        print('request')
        
    def process_response(self, request, response):
        print('response')
        return response
    
    def __call__(self, request):
        print("__call__")
        response = self.process_request(request)
        if response is None:
            response = self.get_response(request)
        response = self.process_response(request, response)
        return response
    
    def process_exception(self, request, exception):
        print('middle error')
        print(exception.__class__.__name__)
        return None