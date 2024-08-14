# Creating Response

# Response()

# Signature:
# Response(data, status=None, template_name = None, headers=None, content_type=None)
# You can use REST framework('s Serializer classes to perform this data serialization, '
# or use your own custom serializer.)

# Arguments:
# data: The serialized data for the response.
# status: A status code for the response. Defaults to 200. See also status code.
# template_name: A template name to use if HTMLRender is selected
# headers: A dictionary of HTTP headers to use in the response.
# content_type: The content type of the response. Typically, this will be set automatically by the determined by
# content negotiation, but there may be some cases where you need to specify the content type explicitly.

# Attributes:
# .data - The unrendered, serialized data of the response.
# .status_code - The numeric status code of the HTTP response.
