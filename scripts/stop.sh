
#!/bin/bash
docker stop student-app 2>/dev/null || true
docker rm student-app 2>/dev/null || true

