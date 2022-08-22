# 0x0F. Load balancer

## Tasks

### 0. Double the number of webservers
In this first task you need to configure `web-02` to be identical to `web-01`.
Requirements:
- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    - The name of the custom HTTP header must be `X-Served-By`
    - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### 1. Install your load balancer
Requirements:
- Configure HAproxy so that it send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

