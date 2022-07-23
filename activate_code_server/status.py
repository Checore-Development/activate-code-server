from flask import jsonify

class status_code(object):
    def __init__(self):
        pass
    
    def response(self, message, status_code=200):
        return jsonify({'message': message, 'status_code': status_code}), status_code, {'ContentType':'application/json'}
    
    @property
    def HTTP_100_CONTINUE(self):
        return self.response('Continue', 100)
    
    @property
    def HTTP_101_SWITCHING_PROTOCOLS(self):
        return self.response('Switching Protocols', 101)
    
    @property
    def HTTP_102_SWITCHING_PROTOCOLS(self):
        return self.response('Processing', 102)
    
    @property
    def HTTP_103_SWITCHING_PROTOCOLS(self):
        return self.response('Early Hints', 103)
    
    @property
    def HTTP_200_OK(self):
        return self.response('OK', 200)
    
    @property
    def HTTP_201_CREATED(self):
        return self.response('Created', 201)
    
    @property
    def HTTP_202_ACCEPTED(self):
        return self.response('Accepted', 202)
    
    @property
    def HTTP_203_NON_AUTHORITATIVE_INFORMATION(self):
        return self.response('Non-Authoritative Information', 203)
    
    @property
    def HTTP_204_NO_CONTENT(self):
        return self.response('No Content', 204)
    
    @property
    def HTTP_205_RESET_CONTENT(self):
        return self.response('Reset Content', 205)
    
    @property
    def HTTP_206_PARTIAL_CONTENT(self):
        return self.response('Partial Content', 206)
    
    @property
    def HTTP_207_MULTI_STATUS(self):
        return self.response('Multi-Status', 207)
    
    @property
    def HTTP_208_ALREADY_REPORTED(self):
        return self.response('Already Reported', 208)
    
    @property
    def HTTP_226_IM_USED(self):
        return self.response('IM Used', 226)
    
    @property
    def HTTP_300_MULTIPLE_CHOICES(self):
        return self.response('Multiple Choices', 300)
    
    @property
    def HTTP_301_MOVED_PERMANENTLY(self):
        return self.response('Moved Permanently', 301)
    
    @property
    def HTTP_302_FOUND(self):
        return self.response('Found', 302)
    
    @property
    def HTTP_303_SEE_OTHER(self):
        return self.response('See Other', 303)
    
    @property
    def HTTP_304_NOT_MODIFIED(self):
        return self.response('Not Modified', 304)
    
    @property
    def HTTP_305_USE_PROXY(self):
        return self.response('Use Proxy', 305)
    
    @property
    def HTTP_306_SWITCH_PROXY(self):
        return self.response('Switch Proxy', 306)
    
    @property
    def HTTP_307_TEMPORARY_REDIRECT(self):
        return self.response('Temporary Redirect', 307)
    
    @property
    def HTTP_308_PERMANENT_REDIRECT(self):
        return self.response('Permanent Redirect', 308)
    
    @property
    def HTTP_400_BAD_REQUEST(self):
        return self.response('Bad Request', 400)
    
    @property
    def HTTP_401_UNAUTHORIZED(self):
        return self.response('Unauthorized', 401)
    
    @property
    def HTTP_402_PAYMENT_REQUIRED(self):
        return self.response('Payment Required', 402)
    
    @property
    def HTTP_403_FORBIDDEN(self):
        return self.response('Forbidden', 403)
    
    @property
    def HTTP_404_NOT_FOUND(self):
        return self.response('Not Found', 404)
    
    @property
    def HTTP_405_METHOD_NOT_ALLOWED(self):
        return self.response('Method Not Allowed', 405)
    
    @property
    def HTTP_406_METHOD_NOT_ALLOWED(self):
        return self.response('Not Acceptable', 406)
    
    @property
    def HTTP_407_PROXY_AUTHENTICATION_REQUIRED(self):
        return self.response('Proxy Authentication Required', 407)
    
    @property
    def HTTP_408_REQUEST_TIMEOUT(self):
        return self.response('Request Timeout', 408)
    
    @property
    def HTTP_409_CONFLICT(self):
        return self.response('Conflict', 409)
    
    @property
    def HTTP_410_GONE(self):
        return self.response('Gone', 410)
    
    @property
    def HTTP_411_LENGTH_REQUIRED(self):
        return self.response('Length Required', 411)
    
    @property
    def HTTP_412_PRECONDITION_FAILED(self):
        return self.response('Precondition Failed', 412)
    
    @property
    def HTTP_413_REQUEST_ENTITY_TOO_LARGE(self):
        return self.response('Request Entity Too Large', 413)
    
    @property
    def HTTP_414_REQUEST_URI_TOO_LONG(self):
        return self.response('Request-URI Too Long', 414)
    
    @property
    def HTTP_415_UNSUPPORTED_MEDIA_TYPE(self):
        return self.response('Unsupported Media Type', 415)
    
    @property
    def HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE(self):
        return self.response('Requested Range Not Satisfiable', 416)
    
    @property
    def HTTP_417_EXPECTATION_FAILED(self):
        return self.response('Expectation Failed', 417)
    
    @property
    def HTTP_418_IM_A_TEAPOT(self):
        return self.response('I\'m a teapot', 418)
    
    @property
    def HTTP_421_MISDIRECTED_REQUEST(self):
        return self.response('Misdirected Request', 421)
    
    @property
    def HTTP_422_UNPROCESSABLE_ENTITY(self):
        return self.response('Unprocessable Entity', 422)
    
    @property
    def HTTP_423_LOCKED(self):
        return self.response('Locked', 423)
    
    @property
    def HTTP_424_FAILED_DEPENDENCY(self):
        return self.response('Failed Dependency', 424)
    
    @property
    def HTTP_425_UNORDERED_COLLECTION(self):
        return self.response('Unordered Collection', 425)
    
    @property
    def HTTP_426_UPGRADE_REQUIRED(self):
        return self.response('Upgrade Required', 426)
    
    @property
    def HTTP_428_PRECONDITION_REQUIRED(self):
        return self.response('Precondition Required', 428)
    
    @property
    def HTTP_429_TOO_MANY_REQUESTS(self):
        return self.response('Too Many Requests', 429)
    
    @property
    def HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE(self):
        return self.response('Request Header Fields Too Large', 431)
    
    @property
    def HTTP_440_LOGIN_TIMEOUT(self):
        return self.response('Login Timeout', 440)
    
    @property
    def HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS(self):
        return self.response('Unavailable For Legal Reasons', 451)
    
    @property
    def HTTP_500_INTERNAL_SERVER_ERROR(self):
        return self.response('Internal Server Error', 500)
    
    @property
    def HTTP_501_NOT_IMPLEMENTED(self):
        return self.response('Not Implemented', 501)
    
    @property
    def HTTP_502_BAD_GATEWAY(self):
        return self.response('Bad Gateway', 502)
    
    @property
    def HTTP_503_SERVICE_UNAVAILABLE(self):
        return self.response('Service Unavailable', 503)
    
    @property
    def HTTP_504_GATEWAY_TIMEOUT(self):
        return self.response('Gateway Timeout', 504)
    
    @property
    def HTTP_505_HTTP_VERSION_NOT_SUPPORTED(self):
        return self.response('HTTP Version Not Supported', 505)
    
    @property
    def HTTP_506_VARIANT_ALSO_NEGOTIATES(self):
        return self.response('Variant Also Negotiates', 506)
    
    @property
    def HTTP_507_SERVICE_UNAVAILABLE(self):
        return self.response('Insufficient Storage', 507)
    
    @property
    def HTTP_508_LOOP_DETECTED(self):
        return self.response('Loop Detected', 508)
    
    @property
    def HTTP_510_NOT_EXTENDED(self):
        return self.response('Not Extended', 510)
    
    @property
    def HTTP_511_NETWORK_AUTHENTICATION_REQUIRED(self):
        return self.response('Network Authentication Required', 511)