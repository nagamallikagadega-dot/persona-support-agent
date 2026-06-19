# API Troubleshooting Guide

## Authentication Issues

### Bearer Token Authentication
To authenticate API requests, include your bearer token in the header:
### Common Authentication Errors
- 401 Unauthorized: Invalid or expired token
- 403 Forbidden: Insufficient permissions
- 429 Too Many Requests: Rate limit exceeded

## API Endpoint Issues

### Connection Timeout
- Check your network connection
- Verify the API endpoint URL is correct
- Ensure firewall settings allow outbound connections

### Invalid Request Format
- Verify JSON payload structure
- Check required fields are included
- Validate data types match API specifications

## Rate Limiting
- Default rate limit: 100 requests per minute
- Use exponential backoff for retry logic
- Contact support for rate limit increases

## Password Reset via API
Send POST request to /auth/reset-password with email field.
Check spam folder for reset email.
Reset link expires in 24 hours.
