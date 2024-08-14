# Requests

# Request parsing
# .data
# request.data returns the parsed content of the request body. This is similar to the standard request.POST
# and request.FIELS attributes except that.

# .query_params
# request.query_params is more correctly named synonym for request.GET
# For clarity inside your code, we recommend using request.query_params instead of
# the Django's standard request.GET
# Doing so will help keep your codebase more correct and obvious - any HTTP method type
# include query parameters, not just requests.

# .parsers
# The APIView class or @api_view decorator will ensure that this property is automatically set to a list
# of Parser instances, based on the parser_classes set on the view or based on the DEFAULT_PARSER_CLASSES
# setting.
# You won't typically need to access this property

