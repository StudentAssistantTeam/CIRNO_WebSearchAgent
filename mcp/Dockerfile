# python server
FROM docker.1ms.run/python:3.13

# Install uv
RUN pip install uv -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

COPY . .

# Give permission to entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 50055
ENTRYPOINT ["./entrypoint.sh"]